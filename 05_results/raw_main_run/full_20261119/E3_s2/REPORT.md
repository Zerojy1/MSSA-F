# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E3_s2`

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.8056 |        nan |     1.3956 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |        nan |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.4091 |        nan |     1.1302 |      0.6989 |      2.8136 |      0.8584 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |        nan |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.2988 |        nan |     1.0179 |    nan      |    nan      |    nan      |             1.144  |                0.1258 |                        nan |            9.1143 |           nan      |
| gbm_residual |       0.4 |      0.6597 |        nan |     0.5264 |    nan      |    nan      |    nan      |             0.6898 |                0.1514 |                        nan |            5.13   |            13.1633 |
| gbm_residual |       0.6 |      0.593  |        nan |     0.4709 |    nan      |    nan      |    nan      |             0.5488 |                0.1488 |                        nan |            2.34   |             7.675  |
| jtg_enkf     |       0.2 |      2.7621 |        nan |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |        nan |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |        nan |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.3529 |        nan |     1.055  |      0.498  |      1.7566 |      0.8707 |             1.2963 |                0.0023 |                          0 |           21.1062 |            19.43   |
| mssa         |       0.4 |      1.1202 |        nan |     0.8601 |      0.5921 |      1.7166 |      0.6909 |             1.0536 |                0.0097 |                          0 |            6.4625 |             3.12   |
| mssa         |       0.6 |      0.8436 |        nan |     0.6695 |      0.67   |      1.6455 |      0.5122 |             0.8295 |                0.0073 |                          0 |            4.47   |           nan      |
| persistence  |       0.2 |      2.9861 |        nan |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |        nan |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |        nan |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4048 |        nan |     0.3023 |      0.8881 |      1.2448 |      0.2219 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4455 |        nan |     0.3304 |      0.8531 |      1.2448 |      0.2454 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5322 |        nan |     0.3964 |      0.7984 |      1.2448 |      0.2983 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6347 |        nan |     0.4799 |      0.7255 |      1.2448 |      0.3695 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |        nan |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |        nan |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |        nan |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.4135 |        nan |     0.3148 |      0.8409 |      1.2055 |      0.234  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5333 |        nan |     0.4192 |      0.7819 |      1.3694 |      0.3139 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6538 |        nan |     0.5193 |      0.7275 |      1.4855 |      0.3945 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7903 |        nan |     0.6318 |      0.6693 |      1.5794 |      0.4874 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |        nan |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |        nan |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |        nan |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4048 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4154 |        nan |     0.3078 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4362 |        nan |     0.323  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5042 |        nan |     0.3725 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |        nan |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |        nan |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |        nan |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.4135 |        nan |     0.3148 |      0.8409 |      1.2055 |      0.234  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.484  |        nan |     0.371  |      0.808  |      1.2726 |      0.2788 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5879 |        nan |     0.4529 |      0.7663 |      1.3573 |      0.3445 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.7207 |        nan |     0.5539 |      0.7052 |      1.4598 |      0.4283 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |        nan |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |        nan |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.411  |        nan |     0.3062 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4187 |        nan |     0.3131 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4881 |        nan |     0.3611 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |        nan |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |        nan |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |        nan |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4507 |        nan |     0.3432 |      0.8213 |      1.2269 |      0.2579 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5688 |        nan |     0.4352 |      0.7736 |      1.3276 |      0.3312 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.7049 |        nan |     0.5398 |      0.7157 |      1.4435 |      0.4168 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |        nan |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |        nan |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |        nan |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.2811 |   0.0006 |    0.5825 |                      11 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0645 |  -0.3342 |    0.1912 |                       9 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.354  |  -0.5882 |   -0.1586 |                       5 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.2212 |  -0.398  |   -0.048  |                       5 |             19 |
| horizon           |       1   | gbm_residual | mssa        |          -0.01   |  -0.0381 |    0.0213 |                       7 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0835 |  -0.1193 |   -0.047  |                       1 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.116  |  -0.1592 |   -0.07   |                       1 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.1493 |  -0.2159 |   -0.0816 |                       3 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.01   |  -0.0384 |    0.0213 |                       7 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0605 |  -0.0984 |   -0.0237 |                       5 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1337 |  -0.19   |   -0.088  |                       1 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1901 |  -0.2612 |   -0.133  |                       1 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0313 |  -0.067  |    0.0047 |                       6 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1318 |  -0.1873 |   -0.0853 |                       1 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1891 |  -0.2629 |   -0.1325 |                       0 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3763 |   0.0862 |    0.6937 |                      12 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.3647 |   0.757  |    1.9879 |                      16 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1488 |  -0.5144 |    0.2153 |                       9 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.2499 |  -0.4636 |   -0.0609 |                       6 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.016  |  -0.0288 |    0.0498 |                      14 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0333 |  -0.0985 |    0.017  |                       9 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.061  |  -0.14   |    0.0034 |                       8 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0326 |  -0.1368 |    0.0572 |                      10 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.016  |  -0.03   |    0.0495 |                      14 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0332 |  -0.104  |    0.0186 |                      10 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.1006 |  -0.194  |   -0.0289 |                       5 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.1301 |  -0.2637 |   -0.0327 |                       5 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |          -0.0202 |  -0.0876 |    0.0285 |                      12 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0983 |  -0.1898 |   -0.0284 |                       5 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.1345 |  -0.2615 |   -0.0387 |                       4 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.6652 |   3.0073 |    4.2704 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.5433 |   0.9156 |    2.1522 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.0613 |  -0.1303 |    0.2395 |                      12 |             19 |
| early_life        |       0.6 | persistence  | mssa        |          -0.0383 |  -0.2655 |    0.1829 |                       8 |             19 |
| horizon           |       1   | persistence  | mssa        |          -0.0112 |  -0.0626 |    0.0293 |                      13 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0069 |  -0.0651 |    0.0654 |                      14 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.1127 |   0.0049 |    0.1966 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.325  |   0.1813 |    0.4444 |                      17 |             19 |
| sparse_all        |       1   | persistence  | mssa        |          -0.0112 |  -0.0637 |    0.0296 |                      13 |             19 |
| sparse_all        |       2   | persistence  | mssa        |          -0.0291 |  -0.1016 |    0.0278 |                      12 |             19 |
| sparse_all        |       4   | persistence  | mssa        |          -0.04   |  -0.1399 |    0.0348 |                      12 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.0457 |  -0.1035 |    0.1635 |                      15 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |          -0.0261 |  -0.0997 |    0.0301 |                      12 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.0558 |  -0.1478 |    0.0145 |                       9 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.029  |  -0.1181 |    0.1412 |                      15 |             19 |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8523 |          0.1477 |       0.14   |
| gbm_residual | temp_plus5 |          0.6698 |          0.3297 |       0.012  |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.444  |
| mssa         | temp_plus5 |          1      |          0      |       0.719  |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9608 | 1.8944 | 2.2286 |
| mssa     | native    | 0.8323 | 1.2001 | 2.9103 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7372 |                 8.952  |
|    0.2 |          10 |           0.226  |                10.342  |
|    0.4 |           8 |           0.542  |                 7.1225 |
|    0.4 |          10 |           0.27   |                 8.7017 |
|    0.6 |           8 |           0.4427 |                 3.6367 |
|    0.6 |          10 |           0.1701 |                 6.16   |
