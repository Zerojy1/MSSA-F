# V3 车辙潜变量补图

- `Fig4-Complete.pdf`：用户图件包原始 Fig. 4(a,b) 加新面板 (c)；`Fig4c-Synthetic-recovery` 为可独立使用的新面板。
- `Real-pavement-decomposition`：真实路面按结构类别留出的 E3 结果。每类固定一个代表结构，自上而下为 STR1、4、7、10、13、15、18。两张新增图均含矢量 PDF、600 dpi TIFF 和 PNG 预览。
- `latent_E0.npz`、`latent_E1E2.npz`、`latent_E3.npz` 为导出文件。E1E2 的 5 折覆盖 15 个测试结构；4 个训练锚点不会出现在其测试集。E3 的 7 折覆盖全部 19 个结构。
- `Fig4c-source.csv`、`Real-source.csv`、`Sublayer-source.csv` 是图中数据，包含调查序号或累计荷载、分量单位和子层深度；`validation.json` 为与原始 V3 运行的数值对照。

**Fig. 4(c) caption.** True and filtered synthetic trajectories for STR1 (seed 0; survey noise SD 0.10 mm). The left panel shows the sum of permanent rut and the datum, the state quantity evaluated in E0; the right panel shows the recoverable component. Survey occasion indexes valid time steps. Panels (a,b) retain the original manuscript results; panel (c) illustrates one replicate, not an average over seeds.

**Real-structure figure caption.** Filtered rut decomposition for one representative of each held-out structure class (E3, seed 0). Left: field surveys and the filtered sum of permanent rut, datum, and recoverable component. Centre: datum and recoverable component. Right: permanent rut accumulated by asphalt sublayer; the shallowest sublayer is stacked first (light) and the deepest last (dark). The x-axis is cumulative ESAL in millions. The difference between survey and filtered total is retained in the source table. These are survey-conditioned estimates from the physics model, not open-loop forecasts, fusion results, or independently measured layer-specific deformation.

**复现。** 在本次 V3 根目录将原始 `export_latent.py` 放在 `scripts/`。使用原实验 CPU 环境、单线程、`configs/full.yaml` 和 seed 0，`latent_jobs.py` 将相互独立的训练折并行，按原折号合并。也可运行原导出脚本串行复算。生成三个 NPZ 后，在本文件夹运行 `python plot_latent.py`；`python verify_latent.py <原始V3结果ZIP>` 校验；`python combine_fig4.py <原始图件ZIP>` 拼合完整 Fig. 4。绘图和校验依赖 NumPy、Matplotlib、Pillow；PDF 合并使用 pypdf。
