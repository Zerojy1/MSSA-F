# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E3_s3`

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.8676 |        nan |     1.4277 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |        nan |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.4273 |        nan |     1.1623 |      0.6538 |      2.8317 |      0.8834 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |        nan |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.3185 |        nan |     1.0141 |    nan      |    nan      |    nan      |             1.1464 |                0.1244 |                        nan |           11.8463 |           nan      |
| gbm_residual |       0.4 |      0.6576 |        nan |     0.5204 |    nan      |    nan      |    nan      |             0.6755 |                0.1534 |                        nan |            1.6775 |            12.9067 |
| gbm_residual |       0.6 |      0.5797 |        nan |     0.4632 |    nan      |    nan      |    nan      |             0.5599 |                0.1413 |                        nan |            1.56   |             7.675  |
| jtg_enkf     |       0.2 |      2.7621 |        nan |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |        nan |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |        nan |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.3263 |        nan |     1.0716 |      0.5243 |      1.9418 |      0.8623 |             1.3566 |                0.0023 |                          0 |           21.8557 |           nan      |
| mssa         |       0.4 |      1.0551 |        nan |     0.8307 |      0.6707 |      1.8925 |      0.6465 |             0.9955 |                0.0091 |                          0 |            6.6625 |            18.68   |
| mssa         |       0.6 |      0.7907 |        nan |     0.619  |      0.7514 |      1.8169 |      0.4673 |             0.7525 |                0.0082 |                          0 |            1.56   |           nan      |
| persistence  |       0.2 |      2.9861 |        nan |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |        nan |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |        nan |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.411  |        nan |     0.2996 |      0.8888 |      1.2453 |      0.2214 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4507 |        nan |     0.3299 |      0.8583 |      1.2453 |      0.2454 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5326 |        nan |     0.3936 |      0.8052 |      1.2453 |      0.2963 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6361 |        nan |     0.4784 |      0.7259 |      1.2453 |      0.3689 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |        nan |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |        nan |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |        nan |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.394  |        nan |     0.2979 |      0.8862 |      1.336  |      0.2197 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5111 |        nan |     0.4031 |      0.8479 |      1.5173 |      0.2944 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6363 |        nan |     0.5094 |      0.795  |      1.6477 |      0.3757 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7802 |        nan |     0.6292 |      0.7323 |      1.7535 |      0.472  |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |        nan |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |        nan |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |        nan |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.411  |        nan |     0.2996 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4224 |        nan |     0.3061 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4437 |        nan |     0.3221 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5145 |        nan |     0.3731 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |        nan |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |        nan |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |        nan |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.394  |        nan |     0.2979 |      0.8862 |      1.336  |      0.2197 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4517 |        nan |     0.3468 |      0.8672 |      1.3953 |      0.255  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5468 |        nan |     0.4256 |      0.8277 |      1.4901 |      0.3145 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6787 |        nan |     0.5328 |      0.7699 |      1.6033 |      0.3982 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |        nan |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |        nan |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4198 |        nan |     0.305  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.429  |        nan |     0.3126 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4989 |        nan |     0.3612 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |        nan |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |        nan |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |        nan |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.418  |        nan |     0.3187 |      0.8767 |      1.343  |      0.2347 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5278 |        nan |     0.4078 |      0.8335 |      1.4561 |      0.3015 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6623 |        nan |     0.5186 |      0.78   |      1.5846 |      0.3869 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |        nan |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |        nan |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |        nan |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.312  |   0.0353 |    0.6045 |                      13 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0755 |  -0.2862 |    0.1303 |                       8 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.3218 |  -0.5174 |   -0.1424 |                       6 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1734 |  -0.3162 |   -0.0281 |                       5 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0085 |  -0.0285 |    0.0526 |                       7 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0648 |  -0.0981 |   -0.0295 |                       4 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1048 |  -0.1463 |   -0.0611 |                       3 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.1435 |  -0.2041 |   -0.0802 |                       3 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0085 |  -0.0294 |    0.052  |                       7 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0331 |  -0.0689 |    0.0059 |                       6 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1016 |  -0.1451 |   -0.0583 |                       3 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1587 |  -0.2075 |   -0.1103 |                       2 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0019 |  -0.0395 |    0.0395 |                       7 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0978 |  -0.1416 |   -0.0527 |                       2 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1583 |  -0.2065 |   -0.1105 |                       2 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3621 |   0.0184 |    0.7456 |                      13 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.3614 |   0.7651 |    1.9739 |                      14 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1159 |  -0.4554 |    0.217  |                       8 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1941 |  -0.4088 |   -0.0021 |                       8 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0341 |  -0.0015 |    0.0608 |                      15 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.015  |  -0.0641 |    0.0244 |                      10 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0479 |  -0.1098 |    0.0087 |                       7 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0267 |  -0.1101 |    0.0525 |                      10 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0341 |  -0.0022 |    0.0607 |                      15 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0069 |  -0.0568 |    0.0294 |                      13 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0707 |  -0.1312 |   -0.0181 |                       7 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.1051 |  -0.191  |   -0.0326 |                       3 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0068 |  -0.0428 |    0.0423 |                      13 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0682 |  -0.1304 |   -0.0148 |                       7 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.1095 |  -0.1916 |   -0.0392 |                       5 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.651  |   3.041  |    4.2026 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.54   |   1.0181 |    2.0463 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.0943 |  -0.0636 |    0.2542 |                      12 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.0175 |  -0.1745 |    0.2093 |                      10 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0069 |  -0.031  |    0.0349 |                      14 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0253 |  -0.026  |    0.0667 |                      14 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.1258 |   0.0418 |    0.1937 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.3309 |   0.2123 |    0.4352 |                      17 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0069 |  -0.0306 |    0.0349 |                      14 |             19 |
| sparse_all        |       2   | persistence  | mssa        |          -0.0027 |  -0.0504 |    0.0309 |                      13 |             19 |
| sparse_all        |       4   | persistence  | mssa        |          -0.0101 |  -0.068  |    0.0346 |                      10 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.0707 |  -0.0235 |    0.1486 |                      15 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0009 |  -0.0491 |    0.0359 |                      15 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.0256 |  -0.0785 |    0.0161 |                       8 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.0539 |  -0.0361 |    0.127  |                      15 |             19 |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8593 |          0.1407 |       0.1814 |
| gbm_residual | temp_plus5 |          0.6852 |          0.3143 |       0.0152 |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.4173 |
| mssa         | temp_plus5 |          1      |          0      |       0.7422 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9623 | 1.8616 | 2.1866 |
| mssa     | native    | 0.8807 | 1.3152 | 2.5058 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7519 |                 9.4835 |
|    0.2 |          10 |           0.2035 |                11.535  |
|    0.4 |           8 |           0.5543 |                 8.8225 |
|    0.4 |          10 |           0.2204 |                 9.07   |
|    0.6 |           8 |           0.4373 |                 5.5833 |
|    0.6 |          10 |           0.1493 |                 6.6525 |
