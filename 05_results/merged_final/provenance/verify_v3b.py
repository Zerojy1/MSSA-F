from pathlib import Path
import hashlib
import json
import shutil
import numpy as np
import pandas as pd

root = Path(__file__).resolve().parents[1]
old, new, merged = [root / d for d in ('full_v3_20261120/merged', 'e3_deep', 'merged_v3b')]
runtime = root / 'e3_deep_runtime'
models = ['lstm','patchtst']
log = (new/'log.txt').read_text()
assert 'report written:' in log and not any(x in log for x in ('!!','non-finite loss','Traceback'))
assert not (new/'failures.csv').exists()
assert 'merged report:' in (root/'merged_v3b.stdout').read_text()
df = pd.read_csv(new/'main_E3.csv')
orig_main = pd.read_csv(old/'main_E3.csv')
reference = orig_main[orig_main.model.eq('mssa')]
keys=['fold','seed','structure','protocol','setting']
refkeys=set(reference[keys].itertuples(index=False,name=None))
assert set(df.model)==set(models)
for m in models:
    sub=df[df.model.eq(m)]
    assert not sub.duplicated(keys).any() and set(sub[keys].itertuples(index=False,name=None))==refkeys, m
    assert sub.fold.nunique()==7 and set(sub.seed)==set(range(5)) and sub.structure.nunique()==19
    assert np.isfinite(sub.loc[sub.n.gt(0),['RMSE','MAE']]).all().all()
assert not orig_main.model.isin(models).any()

def equal(a,b):
    assert set(a.columns)<=set(b.columns)
    assert b[list(set(b.columns)-set(a.columns))].isna().all().all()
    cols=sorted(a.columns)
    # Compare keyed rows independently of merge order; retain every original field.
    sort=[c for c in ['exp','folds','fold','seed','model','protocol','setting','structure','cls','frac','threshold','slot','sig_m_true','horizon','k','delta_T'] if c in cols]
    def order(d):
        d=d[cols]; return (d.sort_values(sort,kind='stable') if sort else d).reset_index(drop=True)
    pd.testing.assert_frame_equal(order(a),order(b),check_dtype=False,check_exact=False,rtol=1e-10,atol=1e-11)

tables=[]
for path in sorted(old.glob('*.csv')):
    name=path.name
    assert (merged/name).is_file(),name
    if name.startswith(('summary_','paired_')): continue
    try:
        a=pd.read_csv(path); b=pd.read_csv(merged/name)
        supplement=new/name
        if supplement.is_file():
            ext=pd.read_csv(supplement); assert 'model' in ext and set(ext.model)<=set(models)
            equal(ext,b[b.model.isin(models)]); b=b[~b.model.isin(models)]
        equal(a,b); tables.append(name)
    except Exception as exc:
        raise AssertionError(name) from exc

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
files=list((old/'pred').glob('*.npz'))
assert files and all(digest(p)==digest(merged/'pred'/p.name) for p in files)
for metric in ['summary_E3.csv','summary_by_seed_E3.csv']:
    assert set(models)<=set(pd.read_csv(merged/metric).model)
txt=(merged/'REPORT.md').read_text(); assert all(m in txt.lower() for m in models)
prov=merged/'provenance'; prov.mkdir(exist_ok=True)
for source,name in [(new/'config_used.yaml','supplement_config_used.yaml'),(runtime/'configs/e3_deep.yaml','e3_deep.yaml'),(new/'environment.json','environment.json'),(new/'log.txt','supplement.log'),(old/'log_merged.txt','original_main.log'),(old/'RUN_STATUS.json','original_main_status.json'),(root/'merged_v3b.stdout','merge.log'),(runtime/'src/rut_mssa/experiments.py','experiments.py'),(runtime/'src/rut_mssa/baselines.py','baselines.py')]:
    shutil.copy2(source,prov/name)
shutil.copy2(__file__,prov/'verify_v3b.py')
status=dict(state='completed',device='cuda',models=models,folds=7,seeds=list(range(5)),structures=19,model_fold_seed_combinations=70,supplement_main_rows=len(df),merged_main_rows=len(pd.read_csv(merged/'main_E3.csv')),original_raw_tables_checked=tables,original_npz_hashes_matched=len(files))
(merged/'RUN_STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
print(json.dumps(status))
