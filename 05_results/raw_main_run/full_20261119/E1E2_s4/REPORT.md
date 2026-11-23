# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E1E2_s4`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.3754 |        nan |     1.1021 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |        nan |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |        nan |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.1273 |        nan |     4.586  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.1701 |        nan |     0.9059 |      0.6911 |      2.4321 |      0.7019 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.07   |        nan |     4.4977 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |        nan |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      0.9807 |        nan |     0.7972 |    nan      |    nan      |    nan      |             0.8383 |                0.1191 |                        nan |           12.5975 |           nan      |
| gbm_residual |       0.4 |      0.5178 |        nan |     0.4193 |    nan      |    nan      |    nan      |             0.4476 |                0.1538 |                        nan |            5.67   |            11.95   |
| gbm_residual |       0.6 |      0.4579 |        nan |     0.3474 |    nan      |    nan      |    nan      |             0.3702 |                0.1383 |                        nan |            2.34   |             4.3533 |
| jtg_enkf     |       0.2 |      2.1483 |        nan |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |        nan |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |        nan |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |        nan |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |        nan |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |        nan |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      3.0506 |        nan |     2.5509 |    nan      |    nan      |    nan      |             3.9208 |                0.2907 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.11   |        nan |     0.8668 |    nan      |    nan      |    nan      |             1.47   |                0.2447 |                        nan |           10.61   |           nan      |
| lstm         |       0.6 |      0.6561 |        nan |     0.5029 |    nan      |    nan      |    nan      |             0.7257 |                0.2091 |                        nan |            1.56   |             6.49   |
| mssa         |       0.2 |      1.1297 |        nan |     0.9002 |      0.5771 |      1.8762 |      0.7104 |             1.1514 |                0.0376 |                          0 |           13.7262 |           nan      |
| mssa         |       0.4 |      0.9354 |        nan |     0.7487 |      0.6153 |      1.8303 |      0.5822 |             0.9163 |                0.0502 |                          0 |            4.2967 |            22.93   |
| mssa         |       0.6 |      0.6641 |        nan |     0.5069 |      0.7454 |      1.7541 |      0.3844 |             0.631  |                0.0302 |                          0 |            1.17   |            14.19   |
| patchtst     |       0.2 |      3.0217 |        nan |     2.5011 |    nan      |    nan      |    nan      |             3.923  |                0.3307 |                        nan |           30.66   |           nan      |
| patchtst     |       0.4 |      1.0536 |        nan |     0.8177 |    nan      |    nan      |    nan      |             1.4722 |                0.3074 |                        nan |           14.9033 |           nan      |
| patchtst     |       0.6 |      0.6378 |        nan |     0.4864 |    nan      |    nan      |    nan      |             0.7278 |                0.2789 |                        nan |          nan      |           nan      |
| persistence  |       0.2 |      3.2132 |        nan |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |        nan |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |        nan |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3575 |        nan |     0.2602 |      0.9247 |      1.2524 |      0.1918 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.3935 |        nan |     0.287  |      0.8936 |      1.2524 |      0.2122 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.4585 |        nan |     0.3338 |      0.864  |      1.2524 |      0.2489 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.5367 |        nan |     0.3928 |      0.8094 |      1.2524 |      0.2981 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |        nan |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |        nan |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |        nan |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |        nan |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |        nan |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |        nan |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4145 |        nan |     0.297  |      0.7911 |      0.917  |      0.2274 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4958 |        nan |     0.3568 |      0.7376 |      0.917  |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5908 |        nan |     0.4251 |      0.6687 |      0.917  |      0.34   |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.7413 |        nan |     0.5425 |      0.5558 |      0.917  |      0.4474 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3749 |        nan |     0.273  |      0.8946 |      1.2514 |      0.2031 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4718 |        nan |     0.3626 |      0.8669 |      1.4569 |      0.2652 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.5807 |        nan |     0.4521 |      0.8205 |      1.6027 |      0.3335 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7056 |        nan |     0.5445 |      0.7549 |      1.7133 |      0.4108 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3742 |        nan |     0.2696 |      0.8184 |      0.8902 |      0.2039 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4675 |        nan |     0.3337 |      0.7446 |      0.8902 |      0.2593 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.5893 |        nan |     0.4144 |      0.6778 |      0.8902 |      0.3324 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.7019 |        nan |     0.4992 |      0.6073 |      0.8902 |      0.4098 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |        nan |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |        nan |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |        nan |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3575 |        nan |     0.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3685 |        nan |     0.2677 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3845 |        nan |     0.2804 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4334 |        nan |     0.3175 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |        nan |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |        nan |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |        nan |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4145 |        nan |     0.297  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4411 |        nan |     0.3147 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4645 |        nan |     0.3335 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5462 |        nan |     0.3872 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3749 |        nan |     0.273  |      0.8946 |      1.2514 |      0.2031 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4202 |        nan |     0.3142 |      0.8775 |      1.3301 |      0.2322 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4895 |        nan |     0.3752 |      0.848  |      1.4298 |      0.2761 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.602  |        nan |     0.4633 |      0.7907 |      1.5474 |      0.3455 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3742 |        nan |     0.2696 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4068 |        nan |     0.2894 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4391 |        nan |     0.3137 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5383 |        nan |     0.3777 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |        nan |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |        nan |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |        nan |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3671 |        nan |     0.2683 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3714 |        nan |     0.2736 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4216 |        nan |     0.3085 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |        nan |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |        nan |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |        nan |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |        nan |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |        nan |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |        nan |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4346 |        nan |     0.3114 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4565 |        nan |     0.3267 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5264 |        nan |     0.3773 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3928 |        nan |     0.2925 |      0.8783 |      1.2722 |      0.2171 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4671 |        nan |     0.3561 |      0.8542 |      1.3922 |      0.2625 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.5819 |        nan |     0.4486 |      0.7963 |      1.5272 |      0.3336 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.3919 |        nan |     0.2828 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4238 |        nan |     0.3038 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5115 |        nan |     0.3658 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |        nan |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |        nan |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |        nan |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.2103 |  -0.1196 |    0.5415 |                       9 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.1261 |  -0.3316 |    0.0984 |                       5 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.3447 |  -0.5579 |   -0.1427 |                       4 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1682 |  -0.3424 |    0.0096 |                       3 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0229 |  -0.0559 |    0.0129 |                       4 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0819 |  -0.1152 |   -0.0507 |                       1 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.123  |  -0.1702 |   -0.077  |                       1 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.1641 |  -0.234  |   -0.0945 |                       2 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0229 |  -0.0547 |    0.0118 |                       4 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0553 |  -0.0893 |   -0.0225 |                       4 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1052 |  -0.1485 |   -0.0663 |                       0 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1609 |  -0.2251 |   -0.0985 |                       1 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.029  |  -0.0628 |    0.0061 |                       6 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0961 |  -0.1386 |   -0.057  |                       1 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1522 |  -0.2161 |   -0.091  |                       1 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3189 |  -0.0406 |    0.6901 |                       9 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.932  |   0.4005 |    1.4671 |                      12 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |           0.0374 |  -0.2458 |    0.3171 |                       8 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0403 |  -0.2583 |    0.1673 |                       6 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0444 |   0.0233 |    0.0637 |                      14 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |           0.0095 |  -0.0317 |    0.0442 |                       9 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0156 |  -0.0754 |    0.0337 |                       7 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.0064 |  -0.0817 |    0.0863 |                       8 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0444 |   0.0238 |    0.064  |                      14 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.01   |  -0.0256 |    0.0399 |                      10 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.031  |  -0.0818 |    0.0157 |                       6 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0623 |  -0.1547 |    0.0126 |                       6 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0166 |  -0.0127 |    0.0424 |                      10 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0225 |  -0.068  |    0.0215 |                       7 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0588 |  -0.1461 |    0.0165 |                       7 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |           0.354  |   0.1253 |    0.5987 |                      10 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.4549 |   0.1419 |    0.7677 |                      11 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.7131 |   0.3073 |    1.1094 |                      12 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           1.0228 |   0.5547 |    1.4878 |                      13 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0234 |   0.6605 |    1.419  |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.9323 |   0.5807 |    1.3137 |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.8348 |   0.4903 |    1.1981 |                      13 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.7381 |   0.3904 |    1.102  |                      12 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0234 |   0.6561 |    1.4218 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.9817 |   0.6222 |    1.3744 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.9184 |   0.5799 |    1.275  |                      14 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.8182 |   0.4952 |    1.1515 |                      14 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           1.0072 |   0.6467 |    1.4008 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9415 |   0.5971 |    1.3122 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.8372 |   0.5122 |    1.1881 |                      14 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.9382 |   3.3134 |    4.5553 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.8139 |   1.2359 |    2.4087 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.1873 |  -0.0051 |    0.3656 |                      10 |             15 |
| early_life        |       0.6 | lstm         | mssa        |           0.0494 |  -0.0917 |    0.1824 |                       8 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.028  |  -0.0185 |    0.0819 |                       6 |             15 |
| horizon           |       3   | lstm         | mssa        |           0.0097 |  -0.0514 |    0.0796 |                       6 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.0102 |  -0.0963 |    0.0934 |                       5 |             15 |
| horizon           |      12   | lstm         | mssa        |           0.0058 |  -0.1327 |    0.1818 |                       6 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.028  |  -0.0191 |    0.083  |                       6 |             15 |
| sparse_all        |       2   | lstm         | mssa        |           0.0097 |  -0.042  |    0.0717 |                       5 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.0292 |  -0.0872 |    0.0372 |                       6 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.0462 |  -0.12   |    0.0305 |                       5 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0304 |  -0.0193 |    0.0879 |                       8 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.0175 |  -0.0807 |    0.0505 |                       5 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.0464 |  -0.1205 |    0.0328 |                       5 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.8641 |   3.1726 |    4.5177 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.764  |   1.1575 |    2.4086 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.1416 |  -0.0485 |    0.3246 |                       9 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |           0.0225 |  -0.1408 |    0.1622 |                      10 |             15 |
| horizon           |       1   | patchtst     | mssa        |          -0.0037 |  -0.0389 |    0.0377 |                       6 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.0143 |  -0.0804 |    0.0683 |                       6 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.0166 |  -0.1221 |    0.1218 |                       6 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.0364 |  -0.1817 |    0.1596 |                       4 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.0037 |  -0.0394 |    0.0391 |                       6 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.0162 |  -0.0658 |    0.0433 |                       5 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.0477 |  -0.1134 |    0.0267 |                       6 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.0514 |  -0.1504 |    0.0401 |                       6 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.0036 |  -0.0468 |    0.0467 |                       8 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0422 |  -0.1096 |    0.0354 |                       6 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.0552 |  -0.1499 |    0.0321 |                       5 |             15 |
| cold_start        |       0   | persistence  | mssa        |           4.1016 |   3.4044 |    4.7689 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.9607 |   1.3282 |    2.5853 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.2266 |   0.0265 |    0.4163 |                      10 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.0648 |  -0.1345 |    0.2372 |                      10 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0322 |   0.0009 |    0.059  |                      12 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0703 |   0.0137 |    0.1181 |                      12 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.1927 |   0.087  |    0.2814 |                      13 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.4343 |   0.2721 |    0.5736 |                      14 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0322 |   0.0014 |    0.0586 |                      12 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0324 |  -0.006  |    0.0659 |                      12 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.0519 |  -0.0104 |    0.1052 |                      11 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.1624 |   0.0314 |    0.2712 |                      13 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0295 |  -0.0076 |    0.0632 |                      11 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0396 |  -0.013  |    0.0884 |                      11 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1472 |   0.0257 |    0.2514 |                      13 |             15 |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8664 |          0.1336 |       0.1736 |
| gbm_residual | temp_plus5 |          0.6678 |          0.3297 |       0.0026 |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.8453 |          0.1547 |       0.5609 |
| lstm         | temp_plus5 |          0.6443 |          0.3557 |       0.0993 |
| mssa         | load_x2    |          1      |          0      |       0.5249 |
| mssa         | temp_plus5 |          1      |          0      |       0.9319 |
| patchtst     | load_x2    |          0.7462 |          0.2538 |       0.4542 |
| patchtst     | temp_plus5 |          0.8665 |          0.1335 |       0.1895 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.9661 | 1.8548 | 2.2244 |
| mssa     | native    | 0.8888 | 1.2463 | 2.3485 |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.8572 |                 5.3189 |
|    0.2 |          10 |           0.4877 |                10.066  |
|    0.4 |           8 |           0.7014 |                 7.85   |
|    0.4 |          10 |           0.4813 |                 8.048  |
|    0.6 |           8 |           0.6032 |                 2.105  |
|    0.6 |          10 |           0.3583 |                 5.12   |
