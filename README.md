# MSSA-F

**Code-grounded dual-state Kalman model with physics–data fusion for rut-depth forecasting on RIOHTrack.**

This research archive contains model code, experiment configurations, input tables, figures, and results for 19 pavement structures and 2,753 rut-depth surveys (2016–2021).

| Contents | Location |
| --- | --- |
| Model, dependencies, configurations and runner | [03_code/rut-mssa](03_code/rut-mssa/) |
| Input tables, raw deflection records and supplementary data | [04_data](04_data/) |
| Final merged experiment report, including E3 deep baselines | [REPORT.md](05_results/merged_final/REPORT.md) |
| Figures in PDF, PNG and TIFF | [02_figures/final](02_figures/final/) |
| Filtered latent states and decomposition outputs | [05_results/latent_states](05_results/latent_states/) |

## Run the experiments

From the repository root, in a Python environment with the dependencies installed:

```bash
cd 03_code/rut-mssa
python -m pip install -r requirements.txt
python run_all.py --config configs/smoke.yaml --out results/smoke
python run_all.py --config configs/full.yaml --out results/main
python run_all.py --config configs/e3_deep.yaml --out results/e3_deep
python run_all.py --merge results/main results/e3_deep --out results/merged
```

See the [experiment documentation](03_code/rut-mssa/README.md) and [recorded provenance](05_results/merged_final/provenance/). The archived plotting scripts retain environment-specific paths and refer to an external ensemble cache; use the exported figures for the archived outputs.
