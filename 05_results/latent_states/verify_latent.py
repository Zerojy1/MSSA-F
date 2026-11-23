"""Verify supplement NPZs against the original V3 results ZIP."""
from pathlib import Path
import csv, io, json, sys, zipfile
import numpy as np

root=Path(__file__).resolve().parent
res={}
with zipfile.ZipFile(sys.argv[1]) as archive:
    prefix='full_v3_20261120/merged/'
    for tag, count, folds in [('E1E2',15,5),('E3',19,7)]:
        stats={'survey_points':0,'max_abs_delta':{k:0.0 for k in ('N','y','r','d0','Rperm','sublayer_sum')}}
        ids=set()
        with np.load(root/f'latent_{tag}.npz') as z:
            for f in range(folds):
                path=prefix+f'pred/{tag}_f{f}_s0_mssa.npz'
                with np.load(io.BytesIO(archive.read(path))) as saved:
                    for b,n in enumerate(saved['names']):
                        assert n not in ids; ids.add(n); key=lambda k:z[f'{n}__{k}']; T=len(key('y')); assert key('fold')==f
                        stats['survey_points']+=T
                        for k in ('N','y','r','d0','Rperm','sublayer_sum'):
                            v,w=(key('R_layer').sum(axis=1),key('Rperm')) if k=='sublayer_sum' else (key(k),saved[k][b,:T]); assert np.isfinite(v).all() and np.isfinite(w).all()
                            stats['max_abs_delta'][k]=max(stats['max_abs_delta'][k],float(np.abs(v-w).max()))
                            np.testing.assert_allclose(v,w,rtol=1e-6,atol=1e-7,err_msg=f'{tag} {n} {k}')
            assert len(ids)==count and ids=={s.split('__')[0] for s in z.files}
        res[tag]=dict(structures=len(ids),**stats)
    with np.load(root/'latent_E0.npz') as z:
        ok=z['tmask']>0; row=next(r for r in csv.DictReader(io.StringIO(archive.read(prefix+'E0_identifiability.csv').decode())) if int(r['seed'])==0 and float(r['sig_m_true'])==0.1)
        res['E0']={'valid_points':int(ok.sum())}
        for field,k in [('permanent_plus_datum','Rperm'),('recoverable','rev')]:
            rmse=float(np.sqrt(np.mean((z[k+'_true'][ok]-z[k+'_hat'][ok])**2))); old=float(row[k+'_rmse']); np.testing.assert_allclose(rmse,old,rtol=1e-6,atol=1e-7); res['E0'][field]={'rmse_mm':rmse,'archived_rmse_mm':old}
(root/'validation.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8'); print(json.dumps(res,indent=2))
