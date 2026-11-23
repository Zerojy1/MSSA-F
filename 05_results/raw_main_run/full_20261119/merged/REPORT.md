> Run status: completed_with_errors; validated jobs: 23/25; failed jobs: 2.

# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/merged`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.3629 |     0.0372 |     1.086  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |     0      |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |     0      |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.0852 |     0.0606 |     4.5183 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.6092 |     0.2747 |     1.2234 |      0.6462 |      2.779  |      0.9708 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.1003 |     0.0332 |     4.5235 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |     0      |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      0.9699 |     0.0303 |     0.791  |    nan      |    nan      |    nan      |             0.8367 |                0.1188 |                        nan |           11.4815 |             2.34   |
| gbm_residual |       0.4 |      0.5179 |     0.0066 |     0.4172 |    nan      |    nan      |    nan      |             0.473  |                0.1568 |                        nan |            4.9347 |            12.224  |
| gbm_residual |       0.6 |      0.4743 |     0.0122 |     0.3645 |    nan      |    nan      |    nan      |             0.3913 |                0.1419 |                        nan |            2.416  |             4.6807 |
| jtg_enkf     |       0.2 |      2.1483 |     0      |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |     0      |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |     0      |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |     0      |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |     0      |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |     0      |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      3.0204 |     0.0396 |     2.5058 |    nan      |    nan      |    nan      |             3.8922 |                0.2973 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.0651 |     0.0402 |     0.8377 |    nan      |    nan      |    nan      |             1.4414 |                0.2521 |                        nan |           10.6493 |             0.59   |
| lstm         |       0.6 |      0.651  |     0.014  |     0.5    |    nan      |    nan      |    nan      |             0.7024 |                0.2172 |                        nan |            1.56   |             9.55   |
| mssa         |       0.2 |      1.4233 |     0.1942 |     1.0883 |      0.5555 |      1.9324 |      0.8809 |             1.3516 |                0.0666 |                          0 |           13.8935 |             1.94   |
| mssa         |       0.4 |      1.1012 |     0.1185 |     0.8564 |      0.6115 |      1.881  |      0.6763 |             1.0324 |                0.0774 |                          0 |            7.4543 |            13.992  |
| mssa         |       0.6 |      0.6993 |     0.0634 |     0.547  |      0.7966 |      1.7992 |      0.4021 |             0.6977 |                0.0648 |                          0 |            1.168  |             9.9275 |
| patchtst     |       0.2 |      3.0452 |     0.0167 |     2.5259 |    nan      |    nan      |    nan      |             3.9384 |                0.3198 |                        nan |           15.33   |           nan      |
| patchtst     |       0.4 |      1.0577 |     0.0193 |     0.837  |    nan      |    nan      |    nan      |             1.4876 |                0.2844 |                        nan |           11.6927 |           nan      |
| patchtst     |       0.6 |      0.6387 |     0.0111 |     0.4926 |    nan      |    nan      |    nan      |             0.7324 |                0.2538 |                        nan |          nan      |             8.4425 |
| persistence  |       0.2 |      3.2132 |     0      |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |     0      |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |     0      |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.363  |     0.0043 |     0.2637 |      0.9211 |      1.2501 |      0.1943 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.3977 |     0.0037 |     0.2896 |      0.8933 |      1.2501 |      0.2144 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.4652 |     0.0047 |     0.3393 |      0.857  |      1.2501 |      0.2531 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.5423 |     0.0038 |     0.3976 |      0.7992 |      1.2501 |      0.3019 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |     0      |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |     0      |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |     0      |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |     0      |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |     0      |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |     0      |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |     0      |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |     0      |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4083 |     0.0082 |     0.2917 |      0.8058 |      0.925  |      0.2223 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4897 |     0.0069 |     0.3507 |      0.7406 |      0.925  |      0.2733 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5819 |     0.0241 |     0.4211 |      0.6702 |      0.925  |      0.3352 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.7314 |     0.01   |     0.5315 |      0.5743 |      0.925  |      0.4373 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3884 |     0.0092 |     0.2838 |      0.9037 |      1.3014 |      0.2098 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5059 |     0.0226 |     0.3845 |      0.8701 |      1.4969 |      0.2809 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6388 |     0.0381 |     0.4903 |      0.8235 |      1.6368 |      0.3619 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7918 |     0.06   |     0.6037 |      0.7625 |      1.7472 |      0.4559 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3887 |     0.0096 |     0.2791 |      0.8121 |      0.8887 |      0.2121 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4799 |     0.0119 |     0.3429 |      0.7361 |      0.8887 |      0.2675 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.5844 |     0.0225 |     0.423  |      0.6533 |      0.8887 |      0.3389 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.7221 |     0.0264 |     0.5262 |      0.5637 |      0.8887 |      0.4346 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |     0      |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |     0      |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |     0      |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |     0      |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.363  |     0.0043 |     0.2637 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3723 |     0.0035 |     0.2701 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3876 |     0.0036 |     0.2833 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.437  |     0.0037 |     0.3213 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |     0      |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |     0      |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |     0      |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |     0      |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |     0      |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |     0      |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |     0      |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |     0      |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4083 |     0.0082 |     0.2917 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4279 |     0.0124 |     0.3053 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4534 |     0.012  |     0.3269 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5339 |     0.0234 |     0.3799 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3884 |     0.0092 |     0.2838 |      0.9037 |      1.3014 |      0.2098 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4406 |     0.0145 |     0.3294 |      0.8841 |      1.3745 |      0.2418 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5266 |     0.0297 |     0.4005 |      0.8505 |      1.4726 |      0.2946 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6593 |     0.0482 |     0.5028 |      0.7941 |      1.5901 |      0.3752 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3887 |     0.0096 |     0.2791 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4125 |     0.01   |     0.295  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4509 |     0.0182 |     0.3244 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5493 |     0.0286 |     0.3874 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |     0      |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |     0      |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |     0      |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |     0      |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3702 |     0.0033 |     0.2715 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.373  |     0.0031 |     0.2754 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4236 |     0.0037 |     0.3117 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |     0      |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |     0      |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |     0      |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |     0      |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |     0      |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |     0      |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4198 |     0.0128 |     0.3028 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4456 |     0.0133 |     0.3217 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.517  |     0.0224 |     0.3707 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4056 |     0.0099 |     0.3033 |      0.8894 |      1.3192 |      0.2233 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4988 |     0.0273 |     0.3783 |      0.8565 |      1.4365 |      0.2786 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6359 |     0.0468 |     0.4856 |      0.8002 |      1.5704 |      0.3616 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4006 |     0.0112 |     0.2892 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4385 |     0.0211 |     0.3161 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5283 |     0.0281 |     0.377  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |     0      |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |     0      |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |     0      |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.1247 |  -0.4838 |    0.2204 |                       6 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.3183 |  -0.565  |   -0.0615 |                       3 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.4476 |  -0.6832 |   -0.2308 |                       2 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1883 |  -0.3367 |   -0.0261 |                       3 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0307 |  -0.0598 |    0.0034 |                       3 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.1065 |  -0.1404 |   -0.0736 |                       1 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1628 |  -0.2198 |   -0.1111 |                       0 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.2236 |  -0.3056 |   -0.1477 |                       0 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0307 |  -0.0584 |    0.0035 |                       3 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0695 |  -0.1002 |   -0.0388 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.132  |  -0.1703 |   -0.0957 |                       1 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.2008 |  -0.262  |   -0.1415 |                       0 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0377 |  -0.0668 |   -0.0062 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1197 |  -0.1558 |   -0.0856 |                       1 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.191  |  -0.25   |   -0.1337 |                       0 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.001  |  -0.4542 |    0.3877 |                       8 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.7433 |   0.0923 |    1.3583 |                      11 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.064  |  -0.3269 |    0.2098 |                       6 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0776 |  -0.2625 |    0.0944 |                       5 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0327 |   0.0083 |    0.0522 |                      13 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0179 |  -0.0694 |    0.0243 |                      10 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0603 |  -0.1426 |    0.0076 |                       7 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0576 |  -0.1802 |    0.0487 |                       7 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0327 |   0.0086 |    0.0525 |                      13 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0067 |  -0.0485 |    0.0262 |                      11 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0599 |  -0.1226 |   -0.0078 |                       6 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.1048 |  -0.2128 |   -0.0194 |                       4 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0064 |  -0.0265 |    0.0326 |                      10 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0469 |  -0.1015 |    0.0001 |                       7 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0985 |  -0.1975 |   -0.0153 |                       5 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |           0.0361 |  -0.371  |    0.3973 |                       9 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.2661 |  -0.1678 |    0.6655 |                       9 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.6117 |   0.1717 |    1.0516 |                      11 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           0.9855 |   0.514  |    1.4702 |                      13 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0117 |   0.6526 |    1.4057 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.9049 |   0.55   |    1.2881 |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.7901 |   0.4398 |    1.1646 |                      12 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.6741 |   0.3044 |    1.0532 |                      10 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0117 |   0.6449 |    1.4078 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.965  |   0.6069 |    1.3564 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.8895 |   0.5483 |    1.2468 |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.7757 |   0.448  |    1.1228 |                      13 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           0.997  |   0.6412 |    1.3887 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9171 |   0.5743 |    1.2842 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.7975 |   0.465  |    1.1583 |                      13 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.5694 |   2.8267 |    4.2783 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.5876 |   1.0081 |    2.1415 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.0528 |  -0.2136 |    0.2887 |                       8 |             15 |
| early_life        |       0.6 | lstm         | mssa        |           0.0033 |  -0.1379 |    0.1336 |                       8 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.0141 |  -0.0184 |    0.0521 |                       5 |             15 |
| horizon           |       3   | lstm         | mssa        |          -0.022  |  -0.0703 |    0.0405 |                       4 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.0605 |  -0.143  |    0.0407 |                       4 |             15 |
| horizon           |      12   | lstm         | mssa        |          -0.0688 |  -0.1966 |    0.0978 |                       4 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.0141 |  -0.018  |    0.0522 |                       5 |             15 |
| sparse_all        |       2   | lstm         | mssa        |          -0.015  |  -0.0528 |    0.0285 |                       5 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.0631 |  -0.1167 |   -0.01   |                       4 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.0964 |  -0.1882 |   -0.0205 |                       5 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0108 |  -0.0262 |    0.0532 |                       7 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.0448 |  -0.0978 |    0.0078 |                       4 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.0904 |  -0.1798 |   -0.0168 |                       5 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.5752 |   2.7878 |    4.2781 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.5999 |   1.0059 |    2.1913 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.0495 |  -0.2027 |    0.2828 |                       8 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |          -0.01   |  -0.1625 |    0.1217 |                       8 |             15 |
| horizon           |       1   | patchtst     | mssa        |          -0.003  |  -0.0355 |    0.0302 |                       7 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.03   |  -0.086  |    0.0356 |                       5 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.0583 |  -0.145  |    0.0465 |                       6 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.0737 |  -0.1954 |    0.0816 |                       5 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.003  |  -0.0355 |    0.0312 |                       7 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.0274 |  -0.0659 |    0.0116 |                       7 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.064  |  -0.1223 |   -0.0108 |                       5 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.0836 |  -0.185  |   -0.004  |                       5 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.0062 |  -0.0431 |    0.0306 |                       7 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0498 |  -0.1074 |    0.0025 |                       5 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.0803 |  -0.1755 |   -0.0034 |                       7 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.7838 |   3.0199 |    4.5009 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.7719 |   1.1611 |    2.3577 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.1252 |  -0.1343 |    0.3636 |                       9 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.0275 |  -0.1412 |    0.1731 |                       9 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0205 |  -0.0144 |    0.05   |                      11 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0429 |  -0.0197 |    0.0955 |                      11 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.148  |   0.0347 |    0.2428 |                      13 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.3704 |   0.2011 |    0.5153 |                      13 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0205 |  -0.015  |    0.0495 |                      11 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0157 |  -0.0305 |    0.0555 |                      10 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.023  |  -0.047  |    0.0814 |                      10 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.1199 |  -0.0207 |    0.2374 |                      12 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0193 |  -0.0253 |    0.0578 |                      12 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0152 |  -0.0454 |    0.0679 |                      10 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1075 |  -0.025  |    0.2182 |                      12 |             15 |

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.8295 |     0.0398 |     1.4137 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |     0      |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.4293 |     0.0579 |     1.1348 |      0.694  |      2.9001 |      0.8641 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |     0      |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.3097 |     0.0098 |     1.0231 |    nan      |    nan      |    nan      |             1.1539 |                0.125  |                        nan |           10.1256 |           nan      |
| gbm_residual |       0.4 |      0.6741 |     0.0143 |     0.5367 |    nan      |    nan      |    nan      |             0.708  |                0.1505 |                        nan |            3.8235 |            12.954  |
| gbm_residual |       0.6 |      0.596  |     0.013  |     0.4751 |    nan      |    nan      |    nan      |             0.5622 |                0.1444 |                        nan |            1.008  |             7.714  |
| jtg_enkf     |       0.2 |      2.7621 |     0      |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |     0      |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |     0      |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.3208 |     0.0219 |     1.0616 |      0.5225 |      1.9371 |      0.8551 |             1.3454 |                0.0025 |                          0 |           21.6533 |            19.43   |
| mssa         |       0.4 |      1.0526 |     0.0396 |     0.8368 |      0.6324 |      1.8877 |      0.6521 |             1.019  |                0.0101 |                          0 |            8.703  |            16.625  |
| mssa         |       0.6 |      0.7712 |     0.0473 |     0.6101 |      0.7667 |      1.8106 |      0.4551 |             0.7448 |                0.0082 |                          0 |            2.6788 |           nan      |
| persistence  |       0.2 |      2.9861 |     0      |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |     0      |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |     0      |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4162 |     0.0082 |     0.3066 |      0.8845 |      1.2445 |      0.226  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4592 |     0.0105 |     0.338  |      0.8484 |      1.2445 |      0.2516 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5436 |     0.0103 |     0.403  |      0.7971 |      1.2445 |      0.304  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6475 |     0.0112 |     0.4878 |      0.7213 |      1.2445 |      0.3769 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |     0      |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |     0      |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |     0      |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |     0      |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3883 |     0.0177 |     0.2928 |      0.8914 |      1.3006 |      0.2153 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5007 |     0.0239 |     0.3942 |      0.8536 |      1.4926 |      0.2875 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.622  |     0.0244 |     0.4974 |      0.7989 |      1.6317 |      0.3661 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7601 |     0.0251 |     0.6116 |      0.7388 |      1.7439 |      0.4579 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |     0      |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |     0      |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |     0      |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |     0      |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4162 |     0.0082 |     0.3066 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4277 |     0.0086 |     0.3127 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4497 |     0.0094 |     0.3292 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5172 |     0.008  |     0.3788 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |     0      |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |     0      |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |     0      |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |     0      |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3883 |     0.0177 |     0.2928 |      0.8914 |      1.3006 |      0.2153 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4429 |     0.028  |     0.3398 |      0.8735 |      1.3713 |      0.2494 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5328 |     0.0382 |     0.4156 |      0.8364 |      1.4692 |      0.306  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6602 |     0.0424 |     0.5184 |      0.7705 |      1.5869 |      0.3872 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |     0      |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |     0      |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |     0      |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |     0      |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4235 |     0.0081 |     0.3112 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4333 |     0.0094 |     0.3192 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5014 |     0.0082 |     0.367  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |     0      |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |     0      |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |     0      |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4104 |     0.027  |     0.3136 |      0.883  |      1.3169 |      0.2303 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5134 |     0.0391 |     0.398  |      0.8425 |      1.4336 |      0.2932 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6429 |     0.0438 |     0.504  |      0.7803 |      1.5673 |      0.3757 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |     0      |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |     0      |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |     0      |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.313  |   0.0797 |    0.5635 |                      14 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0595 |  -0.2532 |    0.1234 |                       8 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.315  |  -0.4749 |   -0.1652 |                       4 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1555 |  -0.2772 |   -0.0295 |                       5 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0178 |  -0.0164 |    0.0596 |                       8 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.048  |  -0.0757 |   -0.0166 |                       3 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.0828 |  -0.1173 |   -0.044  |                       4 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.1158 |  -0.1698 |   -0.0593 |                       3 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0178 |  -0.0165 |    0.0596 |                       8 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0212 |  -0.0508 |    0.0113 |                       5 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.0835 |  -0.1147 |   -0.0521 |                       2 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.138  |  -0.1734 |   -0.1037 |                       0 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0067 |  -0.0256 |    0.0434 |                       7 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0811 |  -0.1116 |   -0.0508 |                       3 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1368 |  -0.1717 |   -0.1052 |                       0 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3844 |   0.0575 |    0.7406 |                      13 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.369  |   0.7907 |    1.9624 |                      15 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1214 |  -0.453  |    0.2055 |                       9 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1886 |  -0.3827 |   -0.011  |                       8 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0377 |   0.012  |    0.0587 |                      15 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0068 |  -0.0469 |    0.0271 |                      12 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0356 |  -0.0901 |    0.0128 |                      10 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0081 |  -0.0884 |    0.0648 |                      11 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0377 |   0.0121 |    0.0583 |                      15 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0009 |  -0.0386 |    0.0295 |                      11 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.059  |  -0.1099 |   -0.0128 |                       7 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0874 |  -0.1642 |   -0.0202 |                       5 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0106 |  -0.0248 |    0.0397 |                      12 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0566 |  -0.1073 |   -0.0103 |                       9 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0913 |  -0.166  |   -0.0266 |                       5 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.6733 |   3.0336 |    4.2653 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.5476 |   1.0123 |    2.0666 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.0887 |  -0.0628 |    0.2289 |                      12 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.023  |  -0.146  |    0.1992 |                      10 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0105 |  -0.0215 |    0.0365 |                      14 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0335 |  -0.0166 |    0.0755 |                      15 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.1381 |   0.0516 |    0.2106 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.3494 |   0.2231 |    0.4593 |                      16 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0105 |  -0.0217 |    0.0366 |                      14 |             19 |
| sparse_all        |       2   | persistence  | mssa        |           0.0032 |  -0.0372 |    0.0354 |                      14 |             19 |
| sparse_all        |       4   | persistence  | mssa        |           0.0017 |  -0.0511 |    0.0455 |                      13 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.0884 |  -0.0086 |    0.1727 |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0048 |  -0.0356 |    0.0378 |                      14 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.014  |  -0.0594 |    0.0246 |                      12 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.0721 |  -0.0189 |    0.151  |                      16 |             19 |

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.7294 |     0.2587 |     1.326  |      0.6504 |      3.1022 |      1.0484 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      2.1191 |     0.513  |     1.7003 |      0.7335 |      4.5354 |      1.2542 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.626  |     0.2859 |     1.2248 |      0.6591 |      2.8159 |      0.9723 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.688  |     0.2005 |     1.293  |      0.6606 |      3.1691 |      1.0279 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.5643 |     0.2521 |     1.2129 |      0.6425 |      2.7844 |      0.9547 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.672  |     0.2337 |     1.3008 |      0.5873 |      2.6162 |      1.0364 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.6686 |     0.2884 |     1.3062 |      0.6072 |      2.6239 |      1.0378 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.5136 |     0.1735 |     1.1731 |      0.5386 |      2.0079 |      0.9518 |             1.4865 |                0.0815 |                          0 |           13.9775 |             1.55   |
| mssa:fixed_mat  |       0.4 |      1.1659 |     0.0992 |     0.9176 |      0.6014 |      1.9521 |      0.7268 |             1.1382 |                0.092  |                          0 |            8.9343 |            11.5183 |
| mssa:fixed_mat  |       0.6 |      0.7384 |     0.044  |     0.5815 |      0.8068 |      1.8638 |      0.426  |             0.7603 |                0.0803 |                          0 |            1.165  |             1.94   |
| mssa:neural_ssm |       0.2 |      1.4744 |     0.0778 |     1.1099 |      0.7407 |      3.0944 |      0.8475 |             1.3865 |                0.1471 |                          0 |           16.0917 |           nan      |
| mssa:neural_ssm |       0.4 |      1.003  |     0.0513 |     0.7707 |      0.8907 |      2.9391 |      0.5586 |             0.9776 |                0.169  |                          0 |            6.9027 |            14.2093 |
| mssa:neural_ssm |       0.6 |      0.7787 |     0.0506 |     0.5797 |      0.9183 |      2.7682 |      0.4218 |             0.7641 |                0.1874 |                          0 |            4.554  |             1.708  |
| mssa:no_defl    |       0.2 |      1.4679 |     0.1958 |     1.1129 |      0.5677 |      1.9973 |      0.9046 |             1.4056 |                0.0775 |                          0 |           11.8097 |             2.135  |
| mssa:no_defl    |       0.4 |      1.1347 |     0.1069 |     0.8803 |      0.6289 |      1.9474 |      0.6975 |             1.0744 |                0.0903 |                          0 |            5.676  |            11.715  |
| mssa:no_defl    |       0.6 |      0.7291 |     0.0542 |     0.5598 |      0.8    |      1.8602 |      0.4165 |             0.721  |                0.0835 |                          0 |            1.086  |             2.7133 |
| mssa:no_disc    |       0.2 |      1.4799 |     0.1524 |     1.1358 |      0.5741 |      2.088  |      0.9183 |             1.4583 |                0.0697 |                          0 |           15.5468 |           nan      |
| mssa:no_disc    |       0.4 |      1.1455 |     0.0981 |     0.8952 |      0.6354 |      2.0353 |      0.7056 |             1.1152 |                0.0844 |                          0 |            5.4197 |           nan      |
| mssa:no_disc    |       0.6 |      0.7571 |     0.0483 |     0.5961 |      0.7906 |      1.9383 |      0.4403 |             0.7725 |                0.0753 |                          0 |            1.755  |           nan      |
| mssa:no_ms      |       0.2 |      1.335  |     0.2248 |     1.0394 |      0.5396 |      1.8181 |      0.8449 |             1.2879 |                0.0801 |                          0 |           13.245  |             1.925  |
| mssa:no_ms      |       0.4 |      1.0186 |     0.182  |     0.7947 |      0.6128 |      1.7676 |      0.6294 |             0.9542 |                0.094  |                          0 |            4.9133 |            12.66   |
| mssa:no_ms      |       0.6 |      0.6751 |     0.0921 |     0.5234 |      0.8009 |      1.6907 |      0.388  |             0.6621 |                0.0786 |                          0 |            1.25   |             6.315  |
| mssa:no_proj    |       0.2 |      1.4176 |     0.1809 |     1.1037 |      0.4646 |      1.7187 |      0.9074 |             1.3793 |                0.0518 |                          0 |           12.5073 |            10.6358 |
| mssa:no_proj    |       0.4 |      1.1182 |     0.1195 |     0.8954 |      0.5058 |      1.6695 |      0.7172 |             1.1105 |                0.0554 |                          0 |            4.3478 |            11.7665 |
| mssa:no_proj    |       0.6 |      0.7397 |     0.0579 |     0.5821 |      0.7103 |      1.5882 |      0.4396 |             0.736  |                0.0397 |                          0 |            2.058  |             7.6512 |
| mssa:no_rev     |       0.2 |      1.4347 |     0.2148 |     1.1209 |      0.4378 |      1.5813 |      0.9373 |             1.4272 |                0      |                          0 |           15.726  |           nan      |
| mssa:no_rev     |       0.4 |      1.086  |     0.1483 |     0.8623 |      0.5377 |      1.5566 |      0.6946 |             1.0459 |                0      |                          0 |            8.924  |            21.37   |
| mssa:no_rev     |       0.6 |      0.6636 |     0.0419 |     0.5209 |      0.7411 |      1.4733 |      0.3913 |             0.6235 |                0      |                          0 |            2.51   |           nan      |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3919 |     0.0147 |     0.2871 |      0.9114 |      1.3335 |      0.2116 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.5135 |     0.0278 |     0.391  |      0.876  |      1.538  |      0.2851 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.6523 |     0.0403 |     0.5009 |      0.8259 |      1.6862 |      0.3698 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.8122 |     0.0589 |     0.6229 |      0.7628 |      1.8054 |      0.4695 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3714 |     0.0088 |     0.2666 |      0.9296 |      1.3807 |      0.1981 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4753 |     0.0153 |     0.3586 |      0.9347 |      1.819  |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.6105 |     0.023  |     0.4691 |      0.9245 |      2.1894 |      0.3377 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.7813 |     0.0314 |     0.6058 |      0.907  |      2.5542 |      0.435  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3891 |     0.008  |     0.2849 |      0.9088 |      1.3119 |      0.21   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.5074 |     0.0207 |     0.3857 |      0.8739 |      1.5214 |      0.2818 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.6422 |     0.0368 |     0.4923 |      0.8256 |      1.6748 |      0.3639 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.7951 |     0.0606 |     0.6052 |      0.7658 |      1.7986 |      0.4574 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3867 |     0.0052 |     0.283  |      0.9052 |      1.31   |      0.2093 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.5059 |     0.0081 |     0.3857 |      0.8749 |      1.5404 |      0.2816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6445 |     0.0185 |     0.4963 |      0.8254 |      1.7127 |      0.366  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.8061 |     0.0341 |     0.6175 |      0.7678 |      1.8559 |      0.4653 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3879 |     0.0122 |     0.284  |      0.8966 |      1.2467 |      0.2101 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.5006 |     0.025  |     0.3805 |      0.8537 |      1.4229 |      0.2799 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.6254 |     0.0416 |     0.4807 |      0.7994 |      1.5464 |      0.3578 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.7698 |     0.0647 |     0.5915 |      0.7413 |      1.6431 |      0.4488 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3867 |     0.0127 |     0.2829 |      0.8865 |      1.2092 |      0.2097 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.4987 |     0.0262 |     0.3779 |      0.8387 |      1.3542 |      0.2789 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.6235 |     0.0411 |     0.4787 |      0.7844 |      1.4541 |      0.3576 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.7676 |     0.0627 |     0.5896 |      0.7118 |      1.5338 |      0.4508 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5275 |     0.0301 |     0.412  |      0.8032 |      1.3589 |      0.305  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.5804 |     0.0386 |     0.454  |      0.7706 |      1.3727 |      0.3392 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.6492 |     0.0516 |     0.5057 |      0.7304 |      1.3921 |      0.3823 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.7525 |     0.0749 |     0.5791 |      0.6797 |      1.4242 |      0.4468 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3919 |     0.0147 |     0.2871 |      0.9114 |      1.3335 |      0.2116 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4476 |     0.0192 |     0.3353 |      0.8902 |      1.4088 |      0.2455 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.54   |     0.0316 |     0.4113 |      0.8563 |      1.5116 |      0.3023 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.681  |     0.0505 |     0.5215 |      0.7943 |      1.6359 |      0.389  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3714 |     0.0088 |     0.2666 |      0.9296 |      1.3807 |      0.1981 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4201 |     0.0136 |     0.3094 |      0.9287 |      1.5215 |      0.2268 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4987 |     0.0231 |     0.3774 |      0.9204 |      1.7227 |      0.272  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6244 |     0.0305 |     0.4746 |      0.9071 |      1.9885 |      0.3413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3891 |     0.008  |     0.2849 |      0.9088 |      1.3119 |      0.21   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4454 |     0.0128 |     0.3332 |      0.8852 |      1.3919 |      0.2445 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5356 |     0.0261 |     0.4074 |      0.8502 |      1.4957 |      0.2997 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6728 |     0.0424 |     0.5129 |      0.7945 |      1.621  |      0.3833 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3867 |     0.0052 |     0.283  |      0.9052 |      1.31   |      0.2093 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4409 |     0.0061 |     0.3303 |      0.8836 |      1.3967 |      0.2427 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5299 |     0.0079 |     0.4046 |      0.8499 |      1.5094 |      0.2974 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.669  |     0.0138 |     0.5119 |      0.7945 |      1.6471 |      0.382  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3879 |     0.0122 |     0.284  |      0.8966 |      1.2467 |      0.2101 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4396 |     0.0206 |     0.3298 |      0.8717 |      1.3153 |      0.2428 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5254 |     0.0312 |     0.4014 |      0.8338 |      1.4048 |      0.2966 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6507 |     0.0534 |     0.4976 |      0.7697 |      1.5123 |      0.3747 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3867 |     0.0127 |     0.2829 |      0.8865 |      1.2092 |      0.2097 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4362 |     0.0178 |     0.3256 |      0.8643 |      1.2692 |      0.2405 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5146 |     0.0288 |     0.3894 |      0.8265 |      1.3433 |      0.2891 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6256 |     0.0444 |     0.4774 |      0.7754 |      1.4361 |      0.3584 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5275 |     0.0301 |     0.412  |      0.8032 |      1.3589 |      0.305  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5793 |     0.0461 |     0.4527 |      0.7634 |      1.3862 |      0.3388 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.644  |     0.0569 |     0.5048 |      0.7292 |      1.4259 |      0.382  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.7477 |     0.0791 |     0.5847 |      0.6786 |      1.4814 |      0.4501 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.4115 |     0.0147 |     0.3081 |      0.896  |      1.3509 |      0.2262 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5113 |     0.0296 |     0.3885 |      0.8609 |      1.4736 |      0.2856 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.657  |     0.0497 |     0.5033 |      0.8017 |      1.615  |      0.3747 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3897 |     0.0125 |     0.2883 |      0.9259 |      1.3991 |      0.2113 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.472  |     0.0238 |     0.3557 |      0.9193 |      1.6355 |      0.2573 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.5972 |     0.0312 |     0.4547 |      0.911  |      1.9347 |      0.3264 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4101 |     0.0084 |     0.3066 |      0.8924 |      1.3327 |      0.2254 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5064 |     0.0237 |     0.3841 |      0.8564 |      1.4567 |      0.2828 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6485 |     0.0407 |     0.4945 |      0.8024 |      1.5994 |      0.3687 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4062 |     0.0069 |     0.3038 |      0.8881 |      1.3319 |      0.2241 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5017 |     0.0096 |     0.382  |      0.8562 |      1.4663 |      0.2811 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6448 |     0.0122 |     0.4934 |      0.8019 |      1.6227 |      0.3676 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4054 |     0.0168 |     0.3043 |      0.8785 |      1.2656 |      0.2242 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.502  |     0.0284 |     0.3818 |      0.8409 |      1.3728 |      0.2825 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6302 |     0.0517 |     0.4821 |      0.777  |      1.4949 |      0.3624 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4036 |     0.0133 |     0.302  |      0.875  |      1.2283 |      0.2229 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4918 |     0.0285 |     0.3708 |      0.8347 |      1.3171 |      0.2755 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6048 |     0.0441 |     0.4614 |      0.7823 |      1.422  |      0.3458 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5562 |     0.0454 |     0.4353 |      0.7725 |      1.3821 |      0.3247 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6308 |     0.0557 |     0.4937 |      0.7338 |      1.422  |      0.3733 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.735  |     0.0787 |     0.5747 |      0.684  |      1.4781 |      0.4419 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8639 |          0.1361 |       0.1706 |
| gbm_residual | temp_plus5 |          0.6684 |          0.3302 |       0.0038 |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.7932 |          0.2068 |       0.5763 |
| lstm         | temp_plus5 |          0.7141 |          0.2859 |       0.1258 |
| mssa         | load_x2    |          1      |          0      |       0.4751 |
| mssa         | temp_plus5 |          1      |          0      |       0.8936 |
| patchtst     | load_x2    |          0.738  |          0.262  |       0.4417 |
| patchtst     | temp_plus5 |          0.8063 |          0.1937 |       0.1539 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8572 |          0.1428 |       0.1589 |
| gbm_residual | temp_plus5 |          0.6757 |          0.3238 |       0.0154 |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.4265 |
| mssa         | temp_plus5 |          1      |          0      |       0.7824 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.4604 |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.8773 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.44   |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       1.0594 |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.4651 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.9355 |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.4333 |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.8827 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.4908 |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.8189 |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.4943 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.8229 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3547 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       0.9435 |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.965  | 1.9089 | 2.2662 |
| mssa     | native    | 0.8998 | 1.2937 | 2.3699 |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9642 | 1.837  | 2.1677 |
| mssa     | native    | 0.8856 | 1.2889 | 2.4364 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.965  | 1.9047 | 2.2575 |
| mssa:fixed_mat  | native    | 0.9077 | 1.3249 | 2.3345 |
| mssa:neural_ssm | aci       | 0.9715 | 1.8412 | 2.1446 |
| mssa:neural_ssm | native    | 0.93   | 1.3798 | 2.1772 |
| mssa:no_defl    | aci       | 0.9649 | 1.9034 | 2.2643 |
| mssa:no_defl    | native    | 0.9043 | 1.3051 | 2.3438 |
| mssa:no_disc    | aci       | 0.9653 | 1.8893 | 2.2335 |
| mssa:no_disc    | native    | 0.9012 | 1.3038 | 2.3479 |
| mssa:no_ms      | aci       | 0.9656 | 1.9042 | 2.2499 |
| mssa:no_ms      | native    | 0.8927 | 1.241  | 2.4115 |
| mssa:no_proj    | aci       | 0.9644 | 1.9166 | 2.2532 |
| mssa:no_proj    | native    | 0.8832 | 1.2036 | 2.4564 |
| mssa:no_rev     | aci       | 0.953  | 2.258  | 2.6794 |
| mssa:no_rev     | native    | 0.7952 | 1.3469 | 3.692  |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.8183 |                 8.5266 |
|    0.2 |          10 |           0.4923 |                10.105  |
|    0.4 |           8 |           0.6935 |                 6.2184 |
|    0.4 |          10 |           0.4464 |                 8.58   |
|    0.6 |           8 |           0.636  |                 3.9905 |
|    0.6 |          10 |           0.3413 |                 5.376  |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7561 |                 8.7977 |
|    0.2 |          10 |           0.2184 |                10.1568 |
|    0.4 |           8 |           0.5775 |                 8.474  |
|    0.4 |          10 |           0.2284 |                 7.8872 |
|    0.6 |           8 |           0.4481 |                 5.0933 |
|    0.6 |          10 |           0.1592 |                 6.6805 |

## E0 synthetic identifiability

| exp   |   seed |   sig_m_true |   beta_true |   beta_hat |   gamma_true |   gamma_hat |   phi_true |   phi_hat |   sig_m_hat |   sig_r_true |   sig_r_hat |   u_spearman |   u_rmse |   Rperm_rmse |   rev_rmse |   rev_sd_true |
|:------|-------:|-------------:|------------:|-----------:|-------------:|------------:|-----------:|----------:|------------:|-------------:|------------:|-------------:|---------:|-------------:|-----------:|--------------:|
| E0    |      0 |          0.1 |         0.4 |     0.3954 |          3.2 |      3.3261 |        0.6 |    0.6324 |      0.1017 |         0.08 |      0.0711 |       0.5804 |   0.1328 |       0.0477 |     0.0761 |        0.2982 |
| E0    |      0 |          0.2 |         0.4 |     0.3962 |          3.2 |      3.3296 |        0.6 |    0.632  |      0.1869 |         0.08 |      0.0911 |       0.5245 |   0.1368 |       0.0589 |     0.0917 |        0.2982 |
| E0    |      1 |          0.1 |         0.4 |     0.3953 |          3.2 |      3.3026 |        0.6 |    0.6184 |      0.1011 |         0.08 |      0.0741 |       0.7343 |   0.0884 |       0.0395 |     0.0727 |        0.2941 |
| E0    |      1 |          0.2 |         0.4 |     0.3914 |          3.2 |      3.335  |        0.6 |    0.6064 |      0.1844 |         0.08 |      0.0971 |       0.7552 |   0.0942 |       0.0508 |     0.0923 |        0.2941 |
| E0    |      2 |          0.1 |         0.4 |     0.3959 |          3.2 |      3.315  |        0.6 |    0.6208 |      0.1034 |         0.08 |      0.0764 |       0.4895 |   0.2095 |       0.0489 |     0.073  |        0.3005 |
| E0    |      2 |          0.2 |         0.4 |     0.3976 |          3.2 |      3.3132 |        0.6 |    0.6173 |      0.1887 |         0.08 |      0.0995 |       0.6154 |   0.2099 |       0.0639 |     0.0906 |        0.3005 |
| E0    |      3 |          0.1 |         0.4 |     0.3978 |          3.2 |      3.2944 |        0.6 |    0.6055 |      0.1047 |         0.08 |      0.0752 |       0.5804 |   0.2601 |       0.0459 |     0.0738 |        0.2966 |
| E0    |      3 |          0.2 |         0.4 |     0.4039 |          3.2 |      3.2702 |        0.6 |    0.6102 |      0.1885 |         0.08 |      0.1018 |       0.5524 |   0.2729 |       0.0591 |     0.0925 |        0.2966 |
| E0    |      4 |          0.1 |         0.4 |     0.3945 |          3.2 |      3.316  |        0.6 |    0.6276 |      0.1002 |         0.08 |      0.0752 |       0.7692 |   0.1915 |       0.0396 |     0.0706 |        0.2978 |
| E0    |      4 |          0.2 |         0.4 |     0.395  |          3.2 |      3.3336 |        0.6 |    0.6167 |      0.1886 |         0.08 |      0.0939 |       0.7483 |   0.1906 |       0.0521 |     0.088  |        0.2978 |

## E5 learned parameters

| exp   |   seed |   beta_hat |   gamma_hat |   wu_load_exp_min |   wu_load_exp_max |   wu_temp_exp_min |   wu_temp_exp_max |   R0eff_Surf_AC13_I_SBS |   R0eff_Surf_AC13_II_SBS |   R0eff_Surf_SMA13 |   R0eff_Surf_PAC13 |   R0eff_Mid_AC20_AH30 |   R0eff_Mid_AC20_SBS |   R0eff_Mid_AC20_AH50 |   R0eff_Bot_AC25_AH30 |   R0eff_Bot_AC25_AH50 |   R0eff_Bot_AC25_AH70 |   R0eff_Bot_AC25_Re_AH70 |   R0eff_Bot_AC10_SBS |   scale_I_SemiRigid_12cmAC |   scale_II_RigidComposite_12cmAC |   scale_III_SemiRigid_16_18cmAC |   scale_IV_Inverted_24_28cmAC |   scale_V_ThickAC_I_24_28cm |   scale_VI_ThickAC_II_36cm |   scale_VII_FullDepth_48_52cm |
|:------|-------:|-----------:|------------:|------------------:|------------------:|------------------:|------------------:|------------------------:|-------------------------:|-------------------:|-------------------:|----------------------:|---------------------:|----------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|---------------------:|---------------------------:|---------------------------------:|--------------------------------:|------------------------------:|----------------------------:|---------------------------:|------------------------------:|
| E5    |      0 |     0.3929 |      3.2658 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.5617 |                   1.7239 |             1.7809 |             1.7638 |                1.6511 |               1.6073 |                2.3729 |                1.533  |                2.6079 |                3.0516 |                   2.0302 |               2.3428 |                     0.4611 |                           0.296  |                          0.4535 |                        0.4396 |                      0.4282 |                     0.4437 |                        0.4011 |
| E5    |      1 |     0.3696 |      3.3523 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.7272 |                   1.8885 |             1.6771 |             1.5319 |                1.5335 |               1.7359 |                2.5309 |                1.3234 |                2.4805 |                3.2972 |                   2.1366 |               2.3391 |                     0.4843 |                           0.2754 |                          0.5097 |                        0.4601 |                      0.4122 |                     0.4357 |                        0.3674 |
| E5    |      2 |     0.4354 |      3.0635 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.8354 |                   1.9892 |             1.486  |             1.7293 |                1.399  |               1.5504 |                2.2368 |                1.6027 |                2.4897 |                3.4622 |                   2.2756 |               1.9069 |                     0.4161 |                           0.3065 |                          0.4928 |                        0.4945 |                      0.4489 |                     0.3692 |                        0.324  |
| E5    |      3 |     0.3937 |      3.1898 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.8416 |                   1.8679 |             1.602  |             1.3842 |                1.4588 |               1.6107 |                2.5829 |                1.3049 |                2.9155 |                3.7005 |                   2.2344 |               2.3077 |                     0.4509 |                           0.2847 |                          0.483  |                        0.4803 |                      0.4309 |                     0.4297 |                        0.3597 |
| E5    |      4 |     0.4424 |      3.0286 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.7695 |                   1.4687 |             1.6    |             1.7457 |                1.4395 |               1.5384 |                2.6154 |                1.6375 |                2.2297 |                3.3615 |                   2.2934 |               2.0067 |                     0.3778 |                           0.3399 |                          0.4786 |                        0.4872 |                      0.4677 |                     0.3536 |                        0.3991 |

## E5 hidden-material recovery

|   seed |   spearman |   n |
|-------:|-----------:|----:|
|      0 |     0.0182 |  10 |
|      1 |    -0.0667 |  10 |
|      2 |    -0.2848 |  10 |
|      3 |    -0.1152 |  10 |
|      4 |    -0.2485 |  10 |

## E5 H1 discrepancy test

|   seed |   mean_abs_g_II_VII |   mean_abs_g_others |   U |   p_one_sided |
|-------:|--------------------:|--------------------:|----:|--------------:|
|      0 |              0.9146 |              0.6882 |  47 |        0.0501 |
|      1 |              0.6761 |              0.5852 |  39 |        0.2054 |
|      2 |              0.0969 |              0.219  |   8 |        0.9902 |
|      3 |              0.6088 |              0.714  |  23 |        0.7655 |
|      4 |              0.1486 |              0.1234 |  40 |        0.1785 |
