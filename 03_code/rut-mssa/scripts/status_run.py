from pathlib import Path
import json
root=Path('/home/zyl105/Zerojy/projects/rut-mssa-20261119')
status=root/'results/full_20261119/status.json'
if not status.exists():
    print('Full experiment not yet started; preflight gate is running or needs attention.')
    for file in [root/'results/smoke_remaining.stdout',root/'results/full-supervisor.log']:
        if file.exists():
            print('\n'+file.name)
            print('\n'.join(file.read_text(errors='replace').splitlines()[-8:]))
else:
    s=json.loads(status.read_text())
    print(json.dumps({k:v for k,v in s.items() if k!='tasks'},ensure_ascii=False,indent=2))
    for t in s['tasks']:
        p=root/'results/full_20261119'/t['name']/'log.txt'
        lines=p.read_text(errors='replace').splitlines() if p.exists() else []
        meaningful=[line for line in lines if line.startswith('[')]
        print(t['name']+': '+t['state']+' | '+(meaningful[-1] if meaningful else ''))
    for p in (root/'results/full_20261119').glob('*/log.txt'):
        bad=[line for line in p.read_text(errors='replace').splitlines() if '!!' in line or 'non-finite' in line]
        for line in bad: print('ATTENTION',p.parent.name,line)
