# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E3_s4`

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.8111 |        nan |     1.4096 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |        nan |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.5272 |        nan |     1.1925 |      0.6026 |      2.531  |      0.941  |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |        nan |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.3213 |        nan |     1.0307 |    nan      |    nan      |    nan      |             1.1555 |                0.1263 |                        nan |           10.285  |           nan      |
| gbm_residual |       0.4 |      0.6835 |        nan |     0.5416 |    nan      |    nan      |    nan      |             0.7114 |                0.146  |                        nan |            5.27   |            13.5433 |
| gbm_residual |       0.6 |      0.5946 |        nan |     0.4735 |    nan      |    nan      |    nan      |             0.5432 |                0.136  |                        nan |            0.38   |             7.095  |
| jtg_enkf     |       0.2 |      2.7621 |        nan |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |        nan |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |        nan |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.304  |        nan |     1.0663 |      0.4757 |      1.804  |      0.8706 |             1.3785 |                0.0032 |                          0 |           22.9325 |           nan      |
| mssa         |       0.4 |      1.0245 |        nan |     0.841  |      0.5577 |      1.7602 |      0.6642 |             1.0672 |                0.011  |                          0 |           13.21   |            22.93   |
| mssa         |       0.6 |      0.7239 |        nan |     0.59   |      0.7432 |      1.6874 |      0.4403 |             0.7543 |                0.0092 |                          0 |            3.895  |           nan      |
| persistence  |       0.2 |      2.9861 |        nan |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |        nan |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |        nan |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4182 |        nan |     0.3068 |      0.8808 |      1.2428 |      0.2267 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4634 |        nan |     0.3404 |      0.8461 |      1.2428 |      0.2536 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5482 |        nan |     0.4048 |      0.7965 |      1.2428 |      0.3061 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6561 |        nan |     0.4911 |      0.7204 |      1.2428 |      0.3807 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |        nan |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |        nan |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |        nan |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3892 |        nan |     0.2941 |      0.872  |      1.2176 |      0.2169 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5013 |        nan |     0.3935 |      0.8279 |      1.398  |      0.2898 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6207 |        nan |     0.4947 |      0.7696 |      1.5276 |      0.3688 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7578 |        nan |     0.6082 |      0.6943 |      1.6308 |      0.4627 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |        nan |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |        nan |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |        nan |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4182 |        nan |     0.3068 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4307 |        nan |     0.3134 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4544 |        nan |     0.3314 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5221 |        nan |     0.3803 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |        nan |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |        nan |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |        nan |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3892 |        nan |     0.2941 |      0.872  |      1.2176 |      0.2169 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4416 |        nan |     0.3397 |      0.8478 |      1.2891 |      0.2511 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5329 |        nan |     0.4174 |      0.8014 |      1.38   |      0.3105 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6577 |        nan |     0.5205 |      0.7217 |      1.4891 |      0.3946 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |        nan |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |        nan |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4268 |        nan |     0.3119 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4385 |        nan |     0.3214 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5071 |        nan |     0.369  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |        nan |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |        nan |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |        nan |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4087 |        nan |     0.315  |      0.8629 |      1.2382 |      0.2317 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5158 |        nan |     0.4019 |      0.8057 |      1.3469 |      0.2992 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6411 |        nan |     0.5071 |      0.7299 |      1.471  |      0.3837 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |        nan |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |        nan |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |        nan |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.2569 |  -0.0242 |    0.5644 |                      12 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0564 |  -0.2737 |    0.1512 |                      10 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.3163 |  -0.4694 |   -0.1674 |                       4 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1411 |  -0.2654 |   -0.0089 |                       4 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0173 |  -0.0229 |    0.0705 |                       6 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0473 |  -0.084  |   -0.0015 |                       3 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.0811 |  -0.1265 |   -0.0313 |                       4 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.1124 |  -0.1859 |   -0.0373 |                       5 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0173 |  -0.0231 |    0.0707 |                       6 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0201 |  -0.0584 |    0.0295 |                       4 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.0825 |  -0.1287 |   -0.0279 |                       2 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.136  |  -0.1896 |   -0.0809 |                       1 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0078 |  -0.0313 |    0.0594 |                       7 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0817 |  -0.1275 |   -0.0292 |                       2 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1351 |  -0.1873 |   -0.08   |                       1 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3285 |  -0.1102 |    0.7755 |                      10 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.3672 |   0.7942 |    1.9469 |                      16 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1256 |  -0.4464 |    0.1913 |                       9 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1726 |  -0.3461 |   -0.0013 |                       7 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0359 |   0.0134 |    0.0572 |                      14 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0092 |  -0.0428 |    0.0217 |                      13 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0374 |  -0.0826 |    0.0048 |                       9 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0102 |  -0.0802 |    0.0539 |                      12 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0359 |   0.0128 |    0.0568 |                      14 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0021 |  -0.0343 |    0.0279 |                      13 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0611 |  -0.1156 |   -0.0125 |                       8 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0882 |  -0.1576 |   -0.0249 |                       8 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0089 |  -0.0211 |    0.0371 |                      12 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0608 |  -0.1168 |   -0.0103 |                       8 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.093  |  -0.1638 |   -0.0278 |                       7 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.6174 |   3.0511 |    4.1733 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.5458 |   1.0374 |    2.0417 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.0845 |  -0.0602 |    0.2166 |                      12 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.0389 |  -0.1182 |    0.2108 |                       9 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0087 |  -0.021  |    0.0338 |                      12 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0311 |  -0.015  |    0.0729 |                      13 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.1363 |   0.0589 |    0.2058 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.3473 |   0.2318 |    0.4552 |                      17 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0087 |  -0.021  |    0.0341 |                      12 |             19 |
| sparse_all        |       2   | persistence  | mssa        |           0.0021 |  -0.0351 |    0.033  |                      13 |             19 |
| sparse_all        |       4   | persistence  | mssa        |          -0.0004 |  -0.0502 |    0.043  |                      13 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.0877 |   0.0002 |    0.1676 |                      15 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0031 |  -0.0316 |    0.0321 |                      11 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.0183 |  -0.065  |    0.0218 |                      10 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.0705 |  -0.0126 |    0.1471 |                      15 |             19 |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.865  |          0.135  |       0.1675 |
| gbm_residual | temp_plus5 |          0.6784 |          0.3205 |       0.0169 |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.4418 |
| mssa         | temp_plus5 |          1      |          0      |       0.7761 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9674 | 1.8114 | 2.137  |
| mssa     | native    | 0.8655 | 1.2125 | 2.5473 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7873 |                 9.581  |
|    0.2 |          10 |           0.1949 |                11.8067 |
|    0.4 |           8 |           0.6502 |                 8.9525 |
|    0.4 |          10 |           0.1824 |                 7.2225 |
|    0.6 |           8 |           0.454  |                 5.5067 |
|    0.6 |          10 |           0.1392 |                 7.81   |
