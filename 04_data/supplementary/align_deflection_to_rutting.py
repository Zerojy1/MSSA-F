"""Align RIOHTrack FWD deflection observations to rutting observations.

Usage: python align_deflection_to_rutting.py deflection_long.csv rutting_long.csv out.csv
rutting_long.csv needs columns: STR (or STR_name), Cum_Load_10k, plus your existing fields.
Rule: for each rutting observation, take the most recent FWD test of the same structure
with Cum_Load_10k <= the rutting Cum_Load_10k (no look-ahead). Merged cycles such as
'N16-17' are kept as one test at their recorded cumulative load.
"""
import sys, pandas as pd

defl = pd.read_csv(sys.argv[1])
rut = pd.read_csv(sys.argv[2]) if sys.argv[2].endswith('.csv') else pd.read_excel(sys.argv[2])
if 'STR' not in rut.columns and 'STR_name' in rut.columns:
    rut = rut.rename(columns={'STR_name': 'STR'})

# one row per (STR, test): D0 and basin area at each drop load, temperatures shared
wide = defl.pivot_table(index=['STR', 'Cycle_ID', 'Cum_Load_10k', 'T_surface_C', 'T_air_C'],
                        columns='FWD_Load_kN', values=['D0_0.01mm', 'basin_area_mm2']).reset_index()
wide.columns = [f'{a}_{int(b)}kN' if b != '' else a for a, b in wide.columns]
wide = wide.rename(columns={'Cycle_ID': 'FWD_Cycle_ID', 'Cum_Load_10k': 'FWD_Cum_Load_10k',
                            'T_surface_C': 'FWD_T_surface_C', 'T_air_C': 'FWD_T_air_C'})

out = []
for s, g in rut.groupby('STR'):
    w = wide[wide.STR == s].sort_values('FWD_Cum_Load_10k').drop(columns='STR')
    g = g.sort_values('Cum_Load_10k')
    a = pd.merge_asof(g, w, left_on='Cum_Load_10k', right_on='FWD_Cum_Load_10k', direction='backward')
    a['FWD_lag_10k'] = a['Cum_Load_10k'] - a['FWD_Cum_Load_10k']
    out.append(a)
res = pd.concat(out).sort_index()
res.to_csv(sys.argv[3], index=False, encoding='utf-8-sig')
print(res[['FWD_lag_10k']].describe())
print('rutting rows without a prior FWD test:', res['FWD_Cum_Load_10k'].isna().sum())
