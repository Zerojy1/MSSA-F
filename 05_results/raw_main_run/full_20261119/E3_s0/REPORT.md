# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E3_s0`

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.7871 |        nan |     1.3962 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |        nan |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.375  |        nan |     1.0915 |      0.7762 |      3.2144 |      0.8029 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |        nan |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.3067 |        nan |     1.0267 |    nan      |    nan      |    nan      |             1.1377 |                0.1286 |                        nan |            6.6986 |           nan      |
| gbm_residual |       0.4 |      0.6814 |        nan |     0.5484 |    nan      |    nan      |    nan      |             0.7493 |                0.1533 |                        nan |            5.27   |            12.77   |
| gbm_residual |       0.6 |      0.5969 |        nan |     0.4748 |    nan      |    nan      |    nan      |             0.5902 |                0.1561 |                        nan |            0.38   |             8.255  |
| jtg_enkf     |       0.2 |      2.7621 |        nan |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |        nan |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |        nan |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.3238 |        nan |     1.0732 |      0.5615 |      2.174  |      0.8399 |             1.3731 |                0.0018 |                          0 |           21.4333 |           nan      |
| mssa         |       0.4 |      1.0294 |        nan |     0.8259 |      0.7148 |      2.1126 |      0.6195 |             0.9965 |                0.0109 |                          0 |            8.27   |           nan      |
| mssa         |       0.6 |      0.7425 |        nan |     0.5751 |      0.8698 |      2.024  |      0.4198 |             0.6783 |                0.0082 |                          0 |          nan      |           nan      |
| persistence  |       0.2 |      2.9861 |        nan |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |        nan |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |        nan |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4244 |        nan |     0.314  |      0.8786 |      1.2447 |      0.2316 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4692 |        nan |     0.3459 |      0.8386 |      1.2447 |      0.2582 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5526 |        nan |     0.412  |      0.7897 |      1.2447 |      0.3112 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6528 |        nan |     0.4946 |      0.7121 |      1.2447 |      0.3826 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |        nan |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |        nan |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |        nan |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3662 |        nan |     0.272  |      0.9316 |      1.3944 |      0.1993 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4701 |        nan |     0.3685 |      0.9165 |      1.6252 |      0.2633 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.5907 |        nan |     0.473  |      0.8715 |      1.7994 |      0.3379 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7311 |        nan |     0.5896 |      0.8234 |      1.9436 |      0.4271 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |        nan |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |        nan |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |        nan |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4244 |        nan |     0.314  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4359 |        nan |     0.3201 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4588 |        nan |     0.337  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5231 |        nan |     0.386  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |        nan |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |        nan |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |        nan |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3662 |        nan |     0.272  |      0.9316 |      1.3944 |      0.1993 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4094 |        nan |     0.3114 |      0.929  |      1.4701 |      0.2248 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4874 |        nan |     0.3796 |      0.9064 |      1.587  |      0.2717 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6112 |        nan |     0.4818 |      0.8515 |      1.7282 |      0.3477 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |        nan |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |        nan |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4308 |        nan |     0.3181 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4409 |        nan |     0.326  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5075 |        nan |     0.3743 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |        nan |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |        nan |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |        nan |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3782 |        nan |     0.286  |      0.9322 |      1.4042 |      0.2077 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4662 |        nan |     0.3608 |      0.9129 |      1.5432 |      0.2587 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.5918 |        nan |     0.4662 |      0.8601 |      1.7035 |      0.3357 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |        nan |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |        nan |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |        nan |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.3392 |   0.1064 |    0.5835 |                      13 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0632 |  -0.2193 |    0.0912 |                       7 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.2897 |  -0.4497 |   -0.1415 |                       2 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1172 |  -0.2297 |   -0.0031 |                       6 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0446 |   0.0015 |    0.1    |                       9 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0128 |  -0.0499 |    0.0347 |                       6 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.047  |  -0.091  |    0.004  |                       5 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.0835 |  -0.1412 |   -0.0221 |                       4 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0446 |   0.0014 |    0.1008 |                       9 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |           0.0144 |  -0.0268 |    0.0657 |                       8 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.0368 |  -0.0825 |    0.0172 |                       5 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.0917 |  -0.1441 |   -0.0342 |                       3 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0403 |  -0.0034 |    0.095  |                       9 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0342 |  -0.0773 |    0.0174 |                       5 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.0888 |  -0.1393 |   -0.0329 |                       3 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.4327 |   0.0983 |    0.8036 |                      14 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.3607 |   0.7686 |    1.9658 |                      15 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1075 |  -0.4439 |    0.2093 |                       8 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1518 |  -0.3591 |    0.0405 |                       7 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0568 |   0.0406 |    0.0723 |                      17 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |           0.0189 |  -0.0125 |    0.0477 |                      13 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0089 |  -0.0612 |    0.0375 |                      10 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.0171 |  -0.0703 |    0.0964 |                      11 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0568 |   0.0402 |    0.0721 |                      17 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.0268 |   0.0038 |    0.0482 |                      13 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0213 |  -0.063  |    0.0173 |                      12 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0478 |  -0.1115 |    0.0071 |                       7 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0371 |   0.0168 |    0.0569 |                      14 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0175 |  -0.0598 |    0.0214 |                      12 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0503 |  -0.1119 |    0.0042 |                       8 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.7216 |   3.0292 |    4.3651 |                      18 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.5392 |   1.0171 |    2.0266 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.1026 |  -0.0829 |    0.2722 |                      12 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.0598 |  -0.0925 |    0.2162 |                      11 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0296 |   0.0059 |    0.0493 |                      15 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0592 |   0.0128 |    0.099  |                      15 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.1648 |   0.0813 |    0.2385 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.3747 |   0.2406 |    0.4939 |                      17 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0296 |   0.006  |    0.0493 |                      15 |             19 |
| sparse_all        |       2   | persistence  | mssa        |           0.0309 |   0.0027 |    0.0541 |                      15 |             19 |
| sparse_all        |       4   | persistence  | mssa        |           0.0394 |  -0.0027 |    0.0752 |                      14 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.128  |   0.0438 |    0.2041 |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0312 |   0.0062 |    0.0524 |                      16 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0251 |  -0.0126 |    0.0563 |                      14 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1131 |   0.0342 |    0.1853 |                      16 |             19 |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8588 |          0.1412 |       0.1621 |
| gbm_residual | temp_plus5 |          0.6772 |          0.3228 |       0.0278 |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.4006 |
| mssa         | temp_plus5 |          1      |          0      |       0.8288 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9652 | 1.808  | 2.1374 |
| mssa     | native    | 0.9272 | 1.3737 | 2.1018 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7588 |                 7.331  |
|    0.2 |          10 |           0.2316 |                 7.1    |
|    0.4 |           8 |           0.5792 |                 8.0875 |
|    0.4 |          10 |           0.2346 |                 4.62   |
|    0.6 |           8 |           0.4407 |                 4.97   |
|    0.6 |          10 |           0.1575 |                 6.415  |
