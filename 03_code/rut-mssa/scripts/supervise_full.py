"""Supervise the unchanged full experiment, with bounded parallelism and explicit validation."""
import os
os.environ.update(OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', NUMEXPR_NUM_THREADS='1', MPLBACKEND='Agg')
import sys, json, time, subprocess, hashlib, traceback
from pathlib import Path
from datetime import datetime
ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'src'))
from run_all import load_cfg
import pandas as pd
import numpy as np
from rut_mssa.data import material_prior
CFG = load_cfg('configs/full.yaml')
OUT = ROOT/'results'/'full_20261119'
MAX_JOBS = 16

def now(): return datetime.now().astimezone().isoformat(timespec='seconds')

def write_json(path, obj):
    tmp = path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')
    tmp.replace(path)

def validate(folder, exp, seed):
    errors = []
    log = (folder/'log.txt').read_text() if (folder/'log.txt').exists() else ''
    if 'report written:' not in log: errors.append('report completion missing')
    for marker in ['!!', 'non-finite loss', 'WARNING: PyTorch not installed']:
        if marker in log: errors.append('log marker: '+marker)
    if (folder/'failures.csv').exists():
        if len(pd.read_csv(folder/'failures.csv')): errors.append('model failures recorded')
    if exp in ['E1E2','E3','E6_ablation']:
        file = folder/f'main_{exp}.csv'
        if not file.exists(): return errors+['missing main table']
        df = pd.read_csv(file)
        models = CFG['experiments'][exp].get('models') or ['mssa:'+v for v in CFG['experiments'][exp]['variants']]
        nf = 7 if exp=='E3' else 5
        observed = set(zip(df['fold'], df['seed'], df['model']))
        expected = {(f,seed,m) for f in range(nf) for m in models}
        if observed != expected: errors.append('model/fold coverage mismatch')
        scored = df[df['n']>0]
        if not np.isfinite(scored[['RMSE','MAE']].to_numpy()).all(): errors.append('nonfinite scored RMSE/MAE')
    elif exp=='E0':
        p=folder/'E0_identifiability.csv'
        if not p.exists(): return errors+['missing E0 table']
        df=pd.read_csv(p)
        if len(df)!=len(CFG['experiments']['E0']['noise_levels']): errors.append('E0 noise level coverage mismatch')
        if not np.isfinite(df.select_dtypes('number').to_numpy()).all(): errors.append('nonfinite E0 metrics')
    elif exp=='E5':
        for name in ['E5_params','E5_discrepancy','E5_H1_test','E5_hidden_material','E5_hidden_material_summary']:
            if not (folder/(name+'.csv')).exists(): errors.append('missing '+name)
        p=folder/'E5_hidden_material.csv'
        if p.exists() and len(pd.read_csv(p))!=int(material_prior('data')[1].sum()): errors.append('hidden material coverage mismatch')
    return errors

def mem_available_gb():
    for line in Path('/proc/meminfo').read_text().splitlines():
        if line.startswith('MemAvailable:'): return int(line.split()[1])/1024**2
    return 0

def main():
    OUT.mkdir(exist_ok=False)
    manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(ROOT.rglob('*')) if p.is_file() and 'results' not in p.parts and '__pycache__' not in p.parts}
    write_json(OUT/'source_sha256.json',manifest)
    with (OUT/'pip-freeze.txt').open('w') as f: subprocess.run([sys.executable,'-m','pip','freeze'],stdout=f,check=True)
    # Start the longest experiment families first, keeping all seeds independent as in run_parallel.sh.
    order=['E6_ablation','E1E2','E5','E3','E0']
    queue=[dict(experiment=e,seed=s,name=f'{e}_s{s}',state='queued')
           for e in order if e in CFG['experiments']['run'] for s in CFG['seeds']]
    state=dict(state='running',started=now(),workers=MAX_JOBS,device='cpu',pid=os.getpid(),tasks=queue)
    running={}
    while any(t['state'] in ('queued','running') for t in queue):
        for t in queue:
            if t['state']!='queued' or len(running)>=MAX_JOBS: continue
            if mem_available_gb()<3.0: break
            folder=OUT/t['name']; folder.mkdir()
            cmd=[sys.executable,'-u','run_all.py','--config','configs/full.yaml','--only',t['experiment'],
                 '--seeds',str(t['seed']),'--threads','1','--device','cpu','--out',str(folder)]
            handle=(OUT/(t['name']+'.stdout')).open('w')
            proc=subprocess.Popen(cmd,stdout=handle,stderr=subprocess.STDOUT)
            t.update(state='running',pid=proc.pid,started=now(),command=cmd)
            running[t['name']]=(proc,handle)
            print(now(),'START',t['name'],proc.pid,flush=True)
        for t in queue:
            if t['name'] not in running: continue
            proc,handle=running[t['name']]
            rc=proc.poll()
            if rc is None: continue
            handle.close()
            try: errors=validate(OUT/t['name'],t['experiment'],t['seed'])
            except Exception as exc: errors=['validation error: '+str(exc)]
            if rc: errors.insert(0,f'process exit {rc}')
            t.update(state='failed' if errors else 'completed',ended=now(),exit_code=rc,errors=errors)
            write_json(OUT/t['name']/'validation.json',dict(state=t['state'],errors=errors))
            print(now(),t['state'].upper(),t['name'],errors,flush=True)
            del running[t['name']]
        state.update(updated=now(),running=len(running),completed=sum(t['state']=='completed' for t in queue),
                     failed=sum(t['state']=='failed' for t in queue),queued=sum(t['state']=='queued' for t in queue),
                     memory_available_gb=round(mem_available_gb(),2))
        write_json(OUT/'status.json',state)
        if running or state['queued']: time.sleep(10)
    with (OUT/'merge.stdout').open('w') as f:
        rc=subprocess.run([sys.executable,'-u','run_all.py','--merge',*[str(OUT/t['name']) for t in queue],
                           '--out',str(OUT/'merged')],stdout=f,stderr=subprocess.STDOUT).returncode
    state.update(state='completed' if not state['failed'] and rc==0 else 'completed_with_errors',
                 ended=now(),merge_exit_code=rc)
    write_json(OUT/'status.json',state)
    write_json(OUT/'merged'/'RUN_STATUS.json',state)
    report=OUT/'merged'/'REPORT.md'
    if report.exists():
        report.write_text(f'> Run status: {state["state"]}; validated jobs: {state["completed"]}/{len(queue)}; failed jobs: {state["failed"]}.\n\n'+report.read_text())
    print(now(),state['state'].upper(),str(report),flush=True)

if __name__=='__main__':
    try: main()
    except Exception:
        traceback.print_exc()
        if OUT.exists(): (OUT/'supervisor_error.txt').write_text(traceback.format_exc())
        raise
