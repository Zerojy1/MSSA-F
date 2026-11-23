# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E1E2_s1`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.3058 |        nan |     1.054  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |        nan |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |        nan |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.1284 |        nan |     4.5576 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.5667 |        nan |     1.1536 |      0.7265 |      3.0507 |      0.8979 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.1474 |        nan |     4.6024 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |        nan |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      0.9419 |        nan |     0.7688 |    nan      |    nan      |    nan      |             0.7917 |                0.1208 |                        nan |           11.2612 |            nan     |
| gbm_residual |       0.4 |      0.5248 |        nan |     0.4223 |    nan      |    nan      |    nan      |             0.4832 |                0.1583 |                        nan |            1.4    |             12.15  |
| gbm_residual |       0.6 |      0.471  |        nan |     0.3596 |    nan      |    nan      |    nan      |             0.3884 |                0.1452 |                        nan |            2.34   |              4.99  |
| jtg_enkf     |       0.2 |      2.1483 |        nan |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |             11.874 |
| jtg_enkf     |       0.4 |      0.9505 |        nan |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |              3.358 |
| jtg_enkf     |       0.6 |      0.5889 |        nan |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |              8.645 |
| jtg_global   |       0.2 |      1.7184 |        nan |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |            nan     |
| jtg_global   |       0.4 |      1.8522 |        nan |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |            nan     |
| jtg_global   |       0.6 |      1.934  |        nan |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |            nan     |
| lstm         |       0.2 |      3.0596 |        nan |     2.5354 |    nan      |    nan      |    nan      |             3.8534 |                0.2757 |                        nan |          nan      |            nan     |
| lstm         |       0.4 |      1.0771 |        nan |     0.8577 |    nan      |    nan      |    nan      |             1.4026 |                0.2347 |                        nan |            8.3    |            nan     |
| lstm         |       0.6 |      0.6617 |        nan |     0.5107 |    nan      |    nan      |    nan      |             0.6688 |                0.2068 |                        nan |          nan      |            nan     |
| mssa         |       0.2 |      1.4073 |        nan |     1.0468 |      0.6017 |      1.9833 |      0.8462 |             1.3397 |                0.0898 |                          0 |           12.9014 |            nan     |
| mssa         |       0.4 |      1.0871 |        nan |     0.8288 |      0.6466 |      1.9279 |      0.6548 |             1.0248 |                0.1014 |                          0 |           11.19   |              2.72  |
| mssa         |       0.6 |      0.6696 |        nan |     0.5257 |      0.8288 |      1.8475 |      0.3839 |             0.6963 |                0.0944 |                          0 |            0.39   |              3.5   |
| patchtst     |       0.2 |      3.0572 |        nan |     2.5492 |    nan      |    nan      |    nan      |             3.9358 |                0.311  |                        nan |          nan      |            nan     |
| patchtst     |       0.4 |      1.0778 |        nan |     0.8584 |    nan      |    nan      |    nan      |             1.485  |                0.2694 |                        nan |           10.4733 |            nan     |
| patchtst     |       0.6 |      0.6459 |        nan |     0.5001 |    nan      |    nan      |    nan      |             0.724  |                0.2379 |                        nan |          nan      |              0.51  |
| persistence  |       0.2 |      3.2132 |        nan |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |            nan     |
| persistence  |       0.4 |      1.1368 |        nan |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |            nan     |
| persistence  |       0.6 |      0.6973 |        nan |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |            nan     |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3645 |        nan |     0.2648 |      0.9177 |      1.2443 |      0.1953 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4009 |        nan |     0.2921 |      0.8866 |      1.2443 |      0.2165 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.469  |        nan |     0.3425 |      0.8487 |      1.2443 |      0.2561 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.5468 |        nan |     0.4013 |      0.7939 |      1.2443 |      0.305  |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |        nan |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |        nan |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |        nan |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |        nan |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |        nan |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |        nan |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4032 |        nan |     0.2868 |      0.8142 |      0.9275 |      0.2186 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4979 |        nan |     0.3538 |      0.7395 |      0.9275 |      0.2766 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.6188 |        nan |     0.442  |      0.6573 |      0.9275 |      0.3552 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.7277 |        nan |     0.5276 |      0.5753 |      0.9275 |      0.4339 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3847 |        nan |     0.2807 |      0.9168 |      1.3583 |      0.2065 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4977 |        nan |     0.3758 |      0.8894 |      1.5531 |      0.2735 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6257 |        nan |     0.4786 |      0.8483 |      1.6915 |      0.3506 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7674 |        nan |     0.5807 |      0.7979 |      1.7989 |      0.4349 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3838 |        nan |     0.2798 |      0.8013 |      0.8741 |      0.212  |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4699 |        nan |     0.3372 |      0.7418 |      0.8741 |      0.2622 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.551  |        nan |     0.403  |      0.6544 |      0.8741 |      0.3213 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.6889 |        nan |     0.5136 |      0.5418 |      0.8741 |      0.4229 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |        nan |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |        nan |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |        nan |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3645 |        nan |     0.2648 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3753 |        nan |     0.2725 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3919 |        nan |     0.2865 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4412 |        nan |     0.3241 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |        nan |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |        nan |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |        nan |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4032 |        nan |     0.2868 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4188 |        nan |     0.2965 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.46   |        nan |     0.3308 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5555 |        nan |     0.3937 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3847 |        nan |     0.2807 |      0.9168 |      1.3583 |      0.2065 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4349 |        nan |     0.325  |      0.9025 |      1.4367 |      0.2372 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5149 |        nan |     0.392  |      0.8738 |      1.5355 |      0.286  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6345 |        nan |     0.4847 |      0.8235 |      1.6542 |      0.3573 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3838 |        nan |     0.2798 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.3977 |        nan |     0.2907 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4764 |        nan |     0.3467 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5911 |        nan |     0.4152 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |        nan |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |        nan |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |        nan |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3723 |        nan |     0.2731 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3753 |        nan |     0.278  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4275 |        nan |     0.3146 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |        nan |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |        nan |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |        nan |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |        nan |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |        nan |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |        nan |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4086 |        nan |     0.2949 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4531 |        nan |     0.327  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5384 |        nan |     0.3847 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4002 |        nan |     0.3    |      0.9078 |      1.382  |      0.2195 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4869 |        nan |     0.3705 |      0.8788 |      1.4998 |      0.2705 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6103 |        nan |     0.4672 |      0.8311 |      1.6348 |      0.3436 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.3855 |        nan |     0.2813 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4692 |        nan |     0.3395 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5693 |        nan |     0.4042 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |        nan |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |        nan |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |        nan |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.0922 |  -0.5353 |    0.3258 |                       8 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.3022 |  -0.6129 |    0.0045 |                       4 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.4159 |  -0.6801 |   -0.1765 |                       4 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.171  |  -0.3308 |    0.0008 |                       3 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0244 |  -0.0461 |   -0.0014 |                       5 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0924 |  -0.1285 |   -0.0573 |                       1 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1425 |  -0.21   |   -0.0805 |                       1 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.191  |  -0.2925 |   -0.0983 |                       1 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0244 |  -0.0456 |   -0.0017 |                       5 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.059  |  -0.0853 |   -0.0344 |                       1 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1154 |  -0.1566 |   -0.0773 |                       1 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1715 |  -0.2441 |   -0.1018 |                       0 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0281 |  -0.0497 |   -0.0055 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1046 |  -0.143  |   -0.0692 |                       0 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1611 |  -0.2319 |   -0.0946 |                       0 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.0705 |  -0.4282 |    0.4735 |                       9 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.7824 |   0.0886 |    1.425  |                      10 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.0366 |  -0.3321 |    0.2608 |                       7 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0554 |  -0.2372 |    0.1196 |                       8 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0373 |   0.0024 |    0.0633 |                      13 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0073 |  -0.0725 |    0.0462 |                      10 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.044  |  -0.1436 |    0.0402 |                       8 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.028  |  -0.1768 |    0.1037 |                       8 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0373 |   0.0029 |    0.0634 |                      13 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.0003 |  -0.0525 |    0.0407 |                      12 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0477 |  -0.122  |    0.012  |                       8 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0796 |  -0.1995 |    0.0149 |                       9 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0134 |  -0.0298 |    0.0448 |                      13 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0346 |  -0.0995 |    0.0178 |                       8 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0723 |  -0.1835 |    0.0202 |                       9 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |           0.1057 |  -0.3888 |    0.5609 |                       8 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.3052 |  -0.2    |    0.7709 |                       9 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.6391 |   0.1482 |    1.1146 |                      10 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           1.0077 |   0.5241 |    1.5054 |                      13 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0163 |   0.6599 |    1.4057 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.9155 |   0.5607 |    1.2976 |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.8065 |   0.4499 |    1.1863 |                      13 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.7036 |   0.3205 |    1.0989 |                      10 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0163 |   0.6522 |    1.4051 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.972  |   0.616  |    1.3579 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.9017 |   0.5583 |    1.2563 |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.8008 |   0.4678 |    1.1548 |                      14 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           1.004  |   0.6475 |    1.391  |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9294 |   0.587  |    1.2979 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.8237 |   0.4853 |    1.1902 |                      14 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.6758 |   2.8041 |    4.5016 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.6565 |   1.0141 |    2.2703 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.0979 |  -0.225  |    0.3896 |                       9 |             15 |
| early_life        |       0.6 | lstm         | mssa        |           0.0291 |  -0.147  |    0.1865 |                       9 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.0154 |  -0.0223 |    0.0564 |                       7 |             15 |
| horizon           |       3   | lstm         | mssa        |          -0.0034 |  -0.059  |    0.0622 |                       6 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.0166 |  -0.1266 |    0.118  |                       7 |             15 |
| horizon           |      12   | lstm         | mssa        |          -0.0364 |  -0.1778 |    0.1372 |                       5 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.0154 |  -0.023  |    0.0555 |                       7 |             15 |
| sparse_all        |       2   | lstm         | mssa        |          -0.0153 |  -0.0622 |    0.0291 |                       8 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.0414 |  -0.1093 |    0.017  |                       6 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.0485 |  -0.1568 |    0.0411 |                       7 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0082 |  -0.0389 |    0.0516 |                       9 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.0215 |  -0.0927 |    0.0371 |                       7 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.0418 |  -0.1482 |    0.0464 |                       7 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.6983 |   2.8224 |    4.4953 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.6605 |   1.0466 |    2.2994 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.0934 |  -0.2229 |    0.3772 |                       9 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |           0.0194 |  -0.1347 |    0.1638 |                       8 |             15 |
| horizon           |       1   | patchtst     | mssa        |          -0.0013 |  -0.0375 |    0.0333 |                       7 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.0263 |  -0.0872 |    0.0449 |                       6 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.0637 |  -0.1479 |    0.0305 |                       4 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.0624 |  -0.1986 |    0.0943 |                       5 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.0013 |  -0.0383 |    0.0342 |                       7 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.033  |  -0.0827 |    0.0128 |                       5 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.0219 |  -0.0913 |    0.04   |                       6 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.0137 |  -0.1286 |    0.085  |                       9 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.0134 |  -0.0611 |    0.0296 |                       7 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0021 |  -0.0713 |    0.0573 |                       9 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.0103 |  -0.1197 |    0.0829 |                       9 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.8533 |   2.9836 |    4.6542 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.811  |   1.1725 |    2.4446 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.1526 |  -0.1647 |    0.4397 |                      10 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.0497 |  -0.1233 |    0.2087 |                       9 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0251 |  -0.0192 |    0.0603 |                      12 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0534 |  -0.0225 |    0.1173 |                      11 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.1643 |   0.0368 |    0.2776 |                      12 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.3999 |   0.2111 |    0.5703 |                      13 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0251 |  -0.0196 |    0.0601 |                      12 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0227 |  -0.035  |    0.071  |                      10 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.0352 |  -0.0483 |    0.1057 |                      10 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.145  |  -0.0084 |    0.2794 |                      12 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0263 |  -0.03   |    0.0727 |                      12 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0275 |  -0.0462 |    0.0913 |                      11 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1337 |  -0.0125 |    0.2616 |                      12 |             15 |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8574 |          0.1426 |       0.1648 |
| gbm_residual | temp_plus5 |          0.6668 |          0.3327 |      -0.0106 |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.798  |          0.202  |       0.6781 |
| lstm         | temp_plus5 |          0.7898 |          0.2102 |       0.1602 |
| mssa         | load_x2    |          1      |          0      |       0.4625 |
| mssa         | temp_plus5 |          1      |          0      |       0.9174 |
| patchtst     | load_x2    |          0.686  |          0.314  |       0.301  |
| patchtst     | temp_plus5 |          0.8434 |          0.1566 |       0.1918 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.9653 | 1.8863 | 2.2659 |
| mssa     | native    | 0.9125 | 1.3514 | 2.2596 |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.8208 |                 7.5333 |
|    0.2 |          10 |           0.5604 |                10.8925 |
|    0.4 |           8 |           0.6686 |                 5.1675 |
|    0.4 |          10 |           0.4704 |                 7.215  |
|    0.6 |           8 |           0.6165 |                 6.4225 |
|    0.6 |          10 |           0.3115 |                 4.99   |
