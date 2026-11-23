"""Data loading, layer tables, deflection alignment and fold definitions."""
from __future__ import annotations

import os
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

SLOTS = ['Surf_AC13_I_SBS', 'Surf_AC13_II_SBS', 'Surf_SMA13', 'Surf_PAC13',
         'Mid_AC20_AH30', 'Mid_AC20_SBS', 'Mid_AC20_AH50',
         'Bot_AC25_AH30', 'Bot_AC25_AH50', 'Bot_AC25_AH70', 'Bot_AC25_Re_AH70', 'Bot_AC10_SBS',
         'Base_CBG_A', 'Base_CBG_B', 'Base_CS', 'Base_CC', 'Base_LCC', 'Base_GA']
AC_SLOTS = [s for s in SLOTS if not s.startswith('Base')]
# top-down order of asphalt slots inside a structure (AC10 SBS is the lowest asphalt layer)
AC_ORDER = AC_SLOTS
CLASSES = ['I_SemiRigid_12cmAC', 'II_RigidComposite_12cmAC', 'III_SemiRigid_16_18cmAC',
           'IV_Inverted_24_28cmAC', 'V_ThickAC_I_24_28cm', 'VI_ThickAC_II_36cm', 'VII_FullDepth_48_52cm']

# five structure-grouped folds of the original manuscript (Table 3); anchors always train
MANUSCRIPT_FOLDS = [['STR1', 'STR8', 'STR19'], ['STR3', 'STR7', 'STR17'], ['STR6', 'STR11', 'STR13'],
                    ['STR2', 'STR12', 'STR18'], ['STR10', 'STR15', 'STR16']]
ANCHORS = ['STR4', 'STR5', 'STR9', 'STR14']


@dataclass
class Sublayer:
    slot_idx: int        # index into AC_SLOTS
    h_mm: float          # sublayer thickness
    z_top_mm: float      # depth of sublayer top
    z_mid_mm: float      # depth of sublayer midpoint


@dataclass
class Structure:
    name: str
    cls: str
    cls_idx: int
    thickness_cm: np.ndarray            # 18 slots
    ha_mm: float                        # total asphalt thickness
    sublayers: list = field(default_factory=list)
    # time series (length T)
    N: np.ndarray = None                # cumulative ESAL (count)
    dN: np.ndarray = None               # increment since previous observation
    T_air: np.ndarray = None            # average air temperature over the interval (deg C)
    y: np.ndarray = None                # rut depth (mm)
    d0n: np.ndarray = None              # normalized FWD centre deflection (as-of aligned), 1 = structure mean


def build_sublayers(th_cm: np.ndarray, cfg: dict) -> list:
    """Split asphalt layers into computation sublayers (JTG D50-2017 style layered summation).

    Rule (configurable, verify against JTG D50-2017 Appendix B): the first `first_max_mm` mm of the
    asphalt surface is split into sublayers no thicker than `first_sub_mm`; deeper material into
    sublayers no thicker than `deep_sub_mm`.
    """
    first_max = cfg.get('first_max_mm', 40.0)
    first_sub = cfg.get('first_sub_mm', 20.0)
    deep_sub = cfg.get('deep_sub_mm', 100.0)
    subs, z = [], 0.0
    for s in AC_ORDER:
        h = float(th_cm[SLOTS.index(s)]) * 10.0
        if h <= 0:
            continue
        top, bottom = z, z + h
        cur = top
        while cur < bottom - 1e-6:
            if cur < first_max - 1e-6:
                nxt = min(bottom, cur + first_sub, first_max)
            else:
                nxt = min(bottom, cur + deep_sub)
            subs.append(Sublayer(AC_SLOTS.index(s), nxt - cur, cur, 0.5 * (cur + nxt)))
            cur = nxt
        z = bottom
    return subs


def load_structures(data_dir: str, cfg: dict) -> dict:
    rut = pd.read_csv(os.path.join(data_dir, 'rutting_long.csv'))
    st = pd.read_csv(os.path.join(data_dir, 'structures.csv'))
    out = {}
    defl = None
    if cfg.get('use_deflection', True) and os.path.exists(os.path.join(data_dir, 'deflection_long.csv')):
        d = pd.read_csv(os.path.join(data_dir, 'deflection_long.csv'))
        defl = d[d.FWD_Load_kN == cfg.get('fwd_load_kN', 50)].dropna(subset=['D0_0.01mm'])
    for _, row in st.iterrows():
        name = row.STR
        th = row[SLOTS].to_numpy(dtype=float)
        g = rut[rut.STR == name].sort_values('Observation_Order')
        N = g.Cum_Load_10k.to_numpy(float) * 1e4
        dN = np.diff(np.concatenate([[0.0], N]))
        s = Structure(name=name, cls=row.Struct_Class, cls_idx=CLASSES.index(row.Struct_Class),
                      thickness_cm=th, ha_mm=float(th[:len(AC_SLOTS)].sum() * 10.0))
        s.sublayers = build_sublayers(th, cfg.get('sublayers', {}))
        s.N, s.dN = N, dN
        s.T_air = g.Avg_Temp_C.to_numpy(float)
        s.y = g.Rutting_Depth_mm.to_numpy(float)
        s.d0n = np.ones_like(s.y)
        if defl is not None:
            dd = defl[defl.STR == name].sort_values('Cum_Load_10k')
            if len(dd):
                load10k = dd.Cum_Load_10k.to_numpy(float)
                d0 = dd['D0_0.01mm'].to_numpy(float)
                d0 = d0 / np.nanmean(d0)
                idx = np.searchsorted(load10k, g.Cum_Load_10k.to_numpy(float), side='right') - 1
                v = np.where(idx >= 0, d0[np.clip(idx, 0, len(d0) - 1)], 1.0)  # as-of, no look-ahead
                s.d0n = v
        out[name] = s
    return out


def material_prior(data_dir: str) -> tuple:
    """Lab R0 (mm) per asphalt slot; NaN where not reported. Returns (R0_prior, known_mask)."""
    m = pd.read_csv(os.path.join(data_dir, 'material_R0.csv')).set_index('slot')
    r0 = np.array([m.loc[s, 'R0_lab_60C_mm'] if s in m.index else np.nan for s in AC_SLOTS], float)
    known = ~np.isnan(r0)
    return r0, known


def surface_air_offset(data_dir: str) -> float:
    """Mean (surface - air) temperature from FWD records; prior for the layer-temperature model."""
    p = os.path.join(data_dir, 'deflection_long.csv')
    if not os.path.exists(p):
        return 4.0
    d = pd.read_csv(p).dropna(subset=['T_surface_C', 'T_air_C'])
    return float((d.T_surface_C - d.T_air_C).mean())


def folds(kind: str = 'manuscript', structures: dict = None) -> list:
    """Return list of (train_names, test_names)."""
    names = sorted(structures.keys(), key=lambda s: int(s[3:]))
    res = []
    if kind == 'manuscript':
        for test in MANUSCRIPT_FOLDS:
            res.append(([n for n in names if n not in test], list(test)))
    elif kind == 'leave_class_out':
        for c in CLASSES:
            test = [n for n in names if structures[n].cls == c]
            res.append(([n for n in names if n not in test], test))
    elif kind == 'all':
        res.append((names, []))
    else:
        raise ValueError(kind)
    return res


def pad_batch(structs: list, kmax: int = None):
    """Stack structures into padded numpy arrays (time-major padding at the tail)."""
    B = len(structs)
    T = max(len(s.y) for s in structs)
    K = kmax or max(len(s.sublayers) for s in structs)
    arr = {k: np.zeros((B, T)) for k in ['N', 'dN', 'T_air', 'y', 'd0n', 'tmask']}
    lay = {k: np.zeros((B, K)) for k in ['h', 'ztop', 'zmid', 'lmask']}
    slot = np.zeros((B, K), dtype=int)
    for b, s in enumerate(structs):
        n = len(s.y)
        arr['N'][b, :n] = s.N
        arr['N'][b, n:] = s.N[-1]
        arr['dN'][b, :n] = s.dN
        arr['T_air'][b, :n] = s.T_air
        arr['T_air'][b, n:] = s.T_air[-1]
        arr['y'][b, :n] = s.y
        arr['d0n'][b, :n] = s.d0n
        arr['d0n'][b, n:] = 1.0
        arr['tmask'][b, :n] = 1.0
        for k, sl in enumerate(s.sublayers[:K]):
            lay['h'][b, k] = sl.h_mm
            lay['ztop'][b, k] = sl.z_top_mm
            lay['zmid'][b, k] = sl.z_mid_mm
            lay['lmask'][b, k] = 1.0
            slot[b, k] = sl.slot_idx
    ha = np.array([s.ha_mm for s in structs])
    cls = np.array([s.cls_idx for s in structs])
    thick = np.stack([s.thickness_cm for s in structs])
    return dict(**arr, **lay, slot=slot, ha=ha, cls=cls, thickness=thick, names=[s.name for s in structs])
