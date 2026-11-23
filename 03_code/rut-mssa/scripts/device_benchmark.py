import os, sys, time, json, copy
from pathlib import Path
root = Path('/home/zyl105/Zerojy/projects/rut-mssa-20261119')
os.chdir(root)
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / 'src'))
import torch, numpy as np
from run_all import load_cfg
from rut_mssa.experiments import Ctx, inner_split
from rut_mssa.data import folds, pad_batch
from rut_mssa.model import MSSA, calibrate_scale
torch.set_num_threads(1)
cfg = load_cfg('configs/full.yaml')
ctx = Ctx(cfg, str(root/'results'), print)
train, test = folds('manuscript', ctx.S)[0]
train, val = inner_split(train, 2, 0)
structs = [ctx.S[n] for n in train]
batch = pad_batch(structs)
mc = dict(cfg['model'], **cfg['train'])
mu = float(np.mean([s.y[0] for s in structs]))
mc['log_scale_init'] = calibrate_scale(mc, structs, ctx.r0, ctx.known, ctx.t_off, mu)
torch.manual_seed(0)
original = MSSA(mc, ctx.r0, ctx.known, ctx.t_off, mu)
results = []
for dev in ['cpu', 'cuda']:
    model = copy.deepcopy(original).to(dev)
    timing, losses = [], []
    for k in range(4):
        model.zero_grad()
        if dev == 'cuda': torch.cuda.synchronize()
        start = time.perf_counter()
        loss, _ = model.loss(batch, dev, rng=np.random.default_rng(k))
        loss.backward()
        if dev == 'cuda': torch.cuda.synchronize()
        timing.append(time.perf_counter() - start)
        losses.append(float(loss.detach().cpu()))
        assert torch.isfinite(loss) and all(p.grad is None or torch.isfinite(p.grad).all() for p in model.parameters())
    results.append(dict(device=dev, seconds_per_forward_backward=float(np.median(timing[1:])), losses=losses,
                        peak_cuda_mb=torch.cuda.max_memory_allocated()/1024**2 if dev=='cuda' else None))
print(json.dumps(results, indent=2))
(root/'results'/'device_benchmark.json').write_text(json.dumps(results, indent=2))
