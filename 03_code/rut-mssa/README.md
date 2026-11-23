# MSSA-Rut v3（相对 v2 的改动）

v2 诊断：MSSA 在已见结构类型的长步预测上仍落后于 GBM。长步误差既不是季节性偏差，也不是结构级的固定偏差（只占均方误差的 13%）。试过结构专属的增长指数 η，长步反而变差，所以没有采用。MSSA 与 GBM 的误差相关系数约 0.7，两者有互补信息。v3 的改动：

1. **事后种子集成与物理-数据融合**（`posthoc.py`，在 `--merge` 时自动运行）：
   - `mssa_ens`：5 个种子的 MSSA 集成，按混合分布计算均值和方差（Lakshminarayanan 等 2017）。
   - `gbm_ens`：对 GBM 做同样的集成，保证比较公平。
   - `fusion`：`mssa_ens` 与 `gbm_ens` **等权**平均（Bates & Granger 1969）。不估计任何权重，因此不用任何数据，也不接触测试结构。
   - 三者用与单模型完全相同的协议代码评估。
2. **基准项 d0 改为随机游走**（局部水平分量），噪声 q_d0 由训练学出。消融变体 `no_rw` 可关闭。
3. **反事实检验修正**：只扰动 40% 预测起点之后的输入，历史数据、观测和已同化的状态都不变。
4. 删除 MSSA-H（交叉拟合的残差分布与最终模型不一致，导致修正器过度修正）。
5. 配对比较改为：每个结构先对种子取平均，再在结构层面做 bootstrap。报告给出相对 `fusion`、`mssa_ens`、`mssa` 三个参照的比较。

**注意**：
- 合并后的 `main_*.csv` 中 `seed = -1` 的行就是集成和融合的结果。
- 你服务器上 `launch_full.sh` 里的冒烟检查断言 `E6 nunique()==7`，需要按新的变体数修改（full 配置为 9 个变体），项目路径也需要改成 v3 的目录。

---

# MSSA-Rut v2（相对首轮运行的改动）

首轮完整运行（2026-11-19）的诊断：MSSA 的增长速率只能按结构类型共享，滤波器无法根据测值修正单个结构的速率，所以在多步预测、稀疏同化、早期外推上落后于 `gbm_residual` 和 `jtg_enkf`。v2 的改动：

1. **结构专属对数速率状态 θ**（`physics.propagate`）。θ 作为随机游走加入状态向量，由约束 EKF 与状态联合估计。线性化用的导数 ∂R′/∂θ = e^g·A·(N_eq+ΔN)^(β−1)·ΔN 为解析式，已用有限差分校验，误差约 4×10⁻¹¹。消融变体 `no_rate` 可关闭此项。
2. **损失加入点精度项** `lambda_mse`（单步和多步均方误差），原来只有负对数似然。
3. **混合模型 MSSA-H**（`experiments.HybridMSSA`）。MSSA 的状态和预测作为特征，加上与 `gbm_residual` 相同的特征，训练一个 GBM 残差修正器。修正器的训练残差由交叉拟合得到：用 3 组中的 2 组训练结构训练 MSSA，去预测剩下 1 组，所以修正器从不接触样本内预测，也从不接触测试结构。区间方差按间隔分箱、用组外残差校准。
   - `mssa_h`：修正器对轴载增量和温度施加单调约束，保证物理一致性。
   - `mssa_h:free`：修正器不加约束。两者共用同一套交叉拟合。
   - "GBM 对 MSSA-H"的比较，直接衡量的是物理状态带来的增益。

运行方式不变：`bash scripts/smoke.sh`，然后 `bash scripts/run_parallel.sh 8`，或者用你服务器上的 `launch_full.sh`。v2 在 E1E2 和 E3 里每个折、每个种子多训练 3 次 MSSA（交叉拟合），预计总耗时比首轮多约 30–60 分钟。

`no_proj` 消融仍可能出现非有限损失，这本身是一条结果（说明投影约束是必需的），会被运行检查标记出来。

---

# MSSA-Rut：设计规范骨架的车辙状态空间同化实验包

本包实现增强方案中的全部模块和实验，**一个总开关跑完所有实验**，结束后自动生成汇总报告。

## 1. 快速开始（服务器上）

```bash
pip install -r requirements.txt          # torch 用 CPU 版即可
bash scripts/smoke.sh                    # 第一步：冒烟测试，5–15 分钟，跑通所有代码路径
bash scripts/run_parallel.sh 16          # 正式实验：16 个进程并行，结束后自动合并报告
# 或单进程顺序跑：  bash scripts/run_all.sh
```

**总开关是 `configs/full.yaml` 里的 `experiments.run`**，删掉某项就跳过对应实验。命令行也可以临时覆盖：

```bash
python run_all.py --only E1E2,E6_ablation --seeds 0,1 --device cpu
python run_all.py --report-only results/<run_dir>             # 只重新生成报告
python run_all.py --merge dirA dirB --out results/merged      # 手动合并多个运行目录
```

结果在 `results/<时间戳>/`（并行运行时在 `results/parallel_<时间戳>/merged/`）：

| 文件 | 内容 |
|---|---|
| `REPORT.md` | 汇总报告：所有表格，以及与 MSSA 的配对 bootstrap 比较 |
| `main_*.csv` | 逐结构的原始指标（模型 × 种子 × 折 × 协议 × 设置） |
| `summary_*.csv` | 跨种子的 mean ± sd |
| `paired_vs_mssa_*.csv` | 结构层面的 RMSE 差值及 95% bootstrap 置信区间 |
| `figures/*.png` | 各协议的 RMSE 曲线 |
| `pred/*.npz` | MSSA 的预测、永久分量、可逆分量、d0 轨迹，可直接画论文图 |
| `fpt_mc_*.csv` | 越限时间（8 mm / 10 mm）的蒙特卡洛分布 |
| `E0_*.csv`, `E5_*.csv` | 可辨识性检验；参数与文献对照；隐藏材料反演；失准图谱 |
| `log.txt`, `config_used.yaml`, `environment.json` | 运行日志、实际使用的配置、运行环境，用于复现 |

## 2. 实验与方案的对应关系

| 开关 | 内容 | 输出 |
|---|---|---|
| `E0` | 合成数据可辨识性：用已知参数生成轨迹，检验能否恢复 β、γ、φ、σ_m、材料偏移，以及永久/可逆分量的分解 | `E0_identifiability.csv` |
| `E1E2` | 原稿的 5 折结构分组验证，跑全部模型和协议（见下） | `main_E1E2.csv` 等 |
| `E3` | 留一结构类型验证（7 类） | `main_E3.csv` |
| `E5` | 全部 19 个结构训练：学到的指数对照 Wu 等（2022）区间；逐一隐藏 10 种材料的室内 R0，检验反演排序（Spearman）；失准图谱，以及 H1 检验（II、VII 类的 \|g\| 更大） | `E5_*.csv` |
| `E6_ablation` | 7 个消融：`no_disc` `no_rev` `no_proj` `no_defl` `fixed_mat` `neural_ssm` `no_ms` | `main_E6_ablation.csv` |

`E1E2`、`E3`、`E6` 统一使用以下评估协议：

- `horizon`：多步预测，h = 1/3/6/12
- `sparse_all` / `sparse_unobserved`：每 k = 1/2/4/8 期才同化一次测值
- `early_life`：只给前 20%/40%/60% 的数据，外推剩余寿命；同时统计终点误差、单调违背率、越限时间误差
- `cold_start`：完全不给测值
- `counterfactual`（E4）：温度 +5 °C、轴载 ×2 后，预测是否按物理方向变化
- `aci`：原生高斯区间与 ACI 在线保覆盖区间的对比

**模型清单：**
- `mssa`：本文模型
- `persistence`：原稿基线
- `gbm_residual`：原稿的残差目标 XGBoost 对照，扩展到多步和稀疏情形
- `jtg_global`：规范模型，全局标定 β，不同化测值（Wu 等 2022 的形式）
- `jtg_enkf`：规范模型加 EnKF 参数更新（Haddad 等 2023）
- `lstm`、`patchtst`：序列网络基线

## 3. 模型结构（`src/rut_mssa/physics.py`、`model.py`）

状态向量 x = [R_1..R_K, d0, r]：
- R_k：沥青亚层永久变形，按 JTG D50-2017 分层模型计算，变温用时间硬化法处理，乘以神经差异项 exp(g)
- d0：初始变形 / 测量基准
- r：温度和弯沉驱动的可逆 AR(1) 分量

观测方程：y = ΣR_k + d0 + r + v。

模型用约束 EKF 做同化（永久分量投影到不递减），训练目标是滤波似然加多步预测 NLL，端到端优化。物理部分写成 numpy 和 torch 都能跑的形式：同一套方程，numpy 用来测试和做蒙特卡洛，torch 用来训练。

## 4. 数据（`data/`）

| 文件 | 来源 |
|---|---|
| `rutting_long.csv`, `structures.csv` | 你仓库里的 `rutting dataset.xlsx`（2,753 条观测，19 个结构） |
| `deflection_long.csv` | ScienceDB 弯沉数据集 doi:10.57760/sciencedb.10782（CC BY 4.0）。模型只用 50 kN 那一级，按"同一结构、累计轴载不超过车辙观测的最近一次检测"对齐，不会用到未来信息 |
| `material_R0.csv` | Wu 等（2022）表 1 的室内车辙变形量。槽位对应关系是按名称匹配的，请核对 |
| `wu2022_jtg_correction.csv` | Wu 等（2022）逐结构的修正系数，作为 E5 的对照 |
| `li2021_lab_vs_field_rut.csv` | Li 等（2021）的室内/现场车辙对照。注意：原文的"结构 1–3"按材料对照，对应 **STR15–17** |

## 5. 已验证与未验证的部分（请先跑冒烟测试）

- **本地已跑通**：数据处理；物理方程和约束 EKF 的 numpy 版本（数量级合理，永久分量单调）；`persistence`、`gbm_residual`（sklearn 后备）、`jtg_global`、`jtg_enkf` 四个基线的全部协议；报告生成；结果合并。
- **本地未执行**：打包环境里没有 PyTorch，所以 MSSA 的训练、`lstm` 和 `patchtst` 的代码只做了语法检查，没有实际运行过。`scripts/smoke.sh` 会把这些路径各跑一遍；如果有报错，`log.txt` 里会标 `!!`。任何单个模型失败都不会中断整次运行，会记入 `failures.csv`。
- **需要你核对的假设**（都在 `configs/full.yaml` 里，可以改）：
  - 亚层划分规则（规范附录 B）
  - JTG 公式的系数
  - 沥青模量 E20：只有比值影响结果
  - 标准轴 BZZ-100 的轮胎几何：0.70 MPa、单圆直径 213 mm、双圆中心距 1.5d

## 6. 运行时间（粗估，未实测）

单次 MSSA 训练在 CPU 上预计需要几分钟。full 配置大约要训练 300 次左右的 MSSA，加上各基线。单进程顺序跑可能要十几到二十几个小时；用 `run_parallel.sh` 按核数并行（每个进程 1 个线程）会快得多。可以先只开 `E1E2` 看结果，再决定是否跑全部。
