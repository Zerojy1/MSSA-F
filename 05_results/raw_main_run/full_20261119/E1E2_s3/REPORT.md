# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E1E2_s3`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.3586 |        nan |     1.0905 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |        nan |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |        nan |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      4.9835 |        nan |     4.3778 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.7735 |        nan |     1.387  |      0.5278 |      2.6948 |      1.1267 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.068  |        nan |     4.4695 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |        nan |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      0.9616 |        nan |     0.7815 |    nan      |    nan      |    nan      |             0.8472 |                0.1179 |                        nan |           11.3438 |           nan      |
| gbm_residual |       0.4 |      0.5242 |        nan |     0.4205 |    nan      |    nan      |    nan      |             0.48   |                0.17   |                        nan |            5.8533 |            11.9475 |
| gbm_residual |       0.6 |      0.4763 |        nan |     0.3674 |    nan      |    nan      |    nan      |             0.3862 |                0.1405 |                        nan |            2.34   |             4.7333 |
| jtg_enkf     |       0.2 |      2.1483 |        nan |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |        nan |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |        nan |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |        nan |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |        nan |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |        nan |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      2.9619 |        nan |     2.4481 |    nan      |    nan      |    nan      |             3.7666 |                0.3022 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.001  |        nan |     0.7755 |    nan      |    nan      |    nan      |             1.3158 |                0.2578 |                        nan |            9.8833 |             0.31   |
| lstm         |       0.6 |      0.6272 |        nan |     0.4783 |    nan      |    nan      |    nan      |             0.5944 |                0.2182 |                        nan |          nan      |            11.1    |
| mssa         |       0.2 |      1.4247 |        nan |     1.105  |      0.5043 |      1.8237 |      0.9021 |             1.3279 |                0.0673 |                          0 |           12.25   |             1.94   |
| mssa         |       0.4 |      1.0792 |        nan |     0.8308 |      0.5771 |      1.7704 |      0.6618 |             0.9667 |                0.0682 |                          0 |            5.265  |             6.67   |
| mssa         |       0.6 |      0.6696 |        nan |     0.5388 |      0.8082 |      1.6938 |      0.3875 |             0.6729 |                0.0537 |                          0 |            2.34   |             6.67   |
| patchtst     |       0.2 |      3.0345 |        nan |     2.5066 |    nan      |    nan      |    nan      |             3.8736 |                0.3121 |                        nan |            0      |           nan      |
| patchtst     |       0.4 |      1.045  |        nan |     0.8244 |    nan      |    nan      |    nan      |             1.4228 |                0.264  |                        nan |           13.4967 |           nan      |
| patchtst     |       0.6 |      0.6443 |        nan |     0.4889 |    nan      |    nan      |    nan      |             0.6691 |                0.2298 |                        nan |          nan      |            11.1    |
| persistence  |       0.2 |      3.2132 |        nan |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |        nan |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |        nan |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3611 |        nan |     0.2629 |      0.9233 |      1.2522 |      0.1934 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.3961 |        nan |     0.2879 |      0.895  |      1.2522 |      0.2134 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.466  |        nan |     0.3393 |      0.853  |      1.2522 |      0.2534 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.541  |        nan |     0.3985 |      0.8004 |      1.2522 |      0.3018 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |        nan |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |        nan |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |        nan |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |        nan |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |        nan |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |        nan |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4046 |        nan |     0.2903 |      0.8216 |      0.9433 |      0.2198 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4829 |        nan |     0.3471 |      0.7502 |      0.9433 |      0.269  |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5771 |        nan |     0.4182 |      0.6817 |      0.9433 |      0.3316 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.738  |        nan |     0.5348 |      0.5858 |      0.9433 |      0.44   |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3966 |        nan |     0.2907 |      0.8896 |      1.2688 |      0.2151 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.522  |        nan |     0.3977 |      0.8482 |      1.4412 |      0.291  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6613 |        nan |     0.5085 |      0.8023 |      1.5616 |      0.3765 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.8224 |        nan |     0.6277 |      0.7359 |      1.6559 |      0.4765 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3973 |        nan |     0.2821 |      0.8249 |      0.9138 |      0.2151 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4848 |        nan |     0.3452 |      0.7357 |      0.9138 |      0.2697 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.586  |        nan |     0.4275 |      0.6563 |      0.9138 |      0.3412 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.754  |        nan |     0.5464 |      0.5608 |      0.9138 |      0.452  |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |        nan |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |        nan |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |        nan |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3611 |        nan |     0.2629 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3698 |        nan |     0.2691 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3858 |        nan |     0.2823 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4379 |        nan |     0.3208 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |        nan |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |        nan |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |        nan |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4046 |        nan |     0.2903 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4173 |        nan |     0.2989 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4338 |        nan |     0.3144 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.4957 |        nan |     0.3552 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3966 |        nan |     0.2907 |      0.8896 |      1.2688 |      0.2151 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4457 |        nan |     0.3332 |      0.8734 |      1.324  |      0.2448 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5333 |        nan |     0.4047 |      0.8392 |      1.4132 |      0.2983 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6637 |        nan |     0.5088 |      0.7893 |      1.5193 |      0.3797 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3973 |        nan |     0.2821 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4195 |        nan |     0.2959 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4298 |        nan |     0.3085 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5192 |        nan |     0.3707 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |        nan |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |        nan |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |        nan |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3683 |        nan |     0.2713 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3705 |        nan |     0.2741 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4226 |        nan |     0.3099 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |        nan |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |        nan |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |        nan |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |        nan |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |        nan |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |        nan |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4085 |        nan |     0.2979 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.423  |        nan |     0.3086 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.4803 |        nan |     0.3463 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4093 |        nan |     0.306  |      0.8774 |      1.2741 |      0.2253 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5063 |        nan |     0.3824 |      0.8449 |      1.3812 |      0.2825 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6406 |        nan |     0.4919 |      0.7937 |      1.5021 |      0.3663 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4076 |        nan |     0.2903 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.415  |        nan |     0.2996 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5005 |        nan |     0.3612 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |        nan |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |        nan |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |        nan |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.2822 |  -0.7285 |    0.162  |                       7 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.3427 |  -0.6511 |   -0.0393 |                       5 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.4119 |  -0.7009 |   -0.1438 |                       5 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1725 |  -0.3128 |   -0.025  |                       4 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0418 |  -0.0804 |    0.0034 |                       2 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.1275 |  -0.181  |   -0.0764 |                       2 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1888 |  -0.2693 |   -0.1111 |                       1 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.2607 |  -0.3713 |   -0.1546 |                       0 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0418 |  -0.0785 |    0.0042 |                       2 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0789 |  -0.1231 |   -0.0341 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1442 |  -0.2032 |   -0.0879 |                       2 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.2136 |  -0.2949 |   -0.1371 |                       0 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0443 |  -0.0853 |    0.0012 |                       3 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1319 |  -0.1897 |   -0.0783 |                       2 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.2054 |  -0.2857 |   -0.1296 |                       0 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |          -0.1619 |  -0.703  |    0.3378 |                       8 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.7291 |   0.1219 |    1.2889 |                      11 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.0346 |  -0.3206 |    0.2598 |                       6 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0643 |  -0.2342 |    0.0916 |                       9 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0232 |   0.0059 |    0.0393 |                      11 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0373 |  -0.0836 |    0.0065 |                       8 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.087  |  -0.1647 |   -0.0136 |                       6 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0939 |  -0.2137 |    0.0201 |                       5 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0232 |   0.0058 |    0.0397 |                      11 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0143 |  -0.0468 |    0.0145 |                       8 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0704 |  -0.1253 |   -0.0232 |                       4 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.1182 |  -0.2048 |   -0.0399 |                       5 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0015 |  -0.0255 |    0.0249 |                      10 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0569 |  -0.1094 |   -0.0116 |                       5 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.1117 |  -0.1934 |   -0.0367 |                       4 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |          -0.1267 |  -0.6144 |    0.3647 |                       8 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.2519 |  -0.2417 |    0.7263 |                       8 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.6411 |   0.1333 |    1.1414 |                      11 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           0.9988 |   0.4911 |    1.5255 |                      13 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0022 |   0.6396 |    1.4008 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.8855 |   0.5238 |    1.2774 |                      14 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.7635 |   0.3986 |    1.1506 |                      12 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.6378 |   0.2486 |    1.0468 |                      10 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0022 |   0.6333 |    1.4017 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.9574 |   0.5929 |    1.3582 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.8789 |   0.5266 |    1.2526 |                      14 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.7623 |   0.4109 |    1.135  |                      12 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           0.992  |   0.6307 |    1.3908 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9071 |   0.5538 |    1.2868 |                      14 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.7844 |   0.4288 |    1.1732 |                      12 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.2995 |   2.5287 |    4.0747 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.512  |   0.9175 |    2.1255 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.0166 |  -0.3261 |    0.3296 |                      10 |             15 |
| early_life        |       0.6 | lstm         | mssa        |          -0.0093 |  -0.1697 |    0.1499 |                       9 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.0035 |  -0.0277 |    0.0383 |                       5 |             15 |
| horizon           |       3   | lstm         | mssa        |          -0.0422 |  -0.0944 |    0.0143 |                       4 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.0891 |  -0.1706 |    0.0008 |                       3 |             15 |
| horizon           |      12   | lstm         | mssa        |          -0.0937 |  -0.2319 |    0.0579 |                       4 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.0035 |  -0.0282 |    0.0379 |                       5 |             15 |
| sparse_all        |       2   | lstm         | mssa        |          -0.0305 |  -0.0674 |    0.0079 |                       4 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.0921 |  -0.145  |   -0.0428 |                       2 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.1468 |  -0.2338 |   -0.0668 |                       1 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |          -0.0019 |  -0.0395 |    0.0364 |                       7 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.0751 |  -0.1308 |   -0.026  |                       3 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.1393 |  -0.2248 |   -0.0637 |                       3 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.3772 |   2.5684 |    4.1495 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.571  |   0.9628 |    2.2304 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.0682 |  -0.2677 |    0.3844 |                       9 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |           0.0021 |  -0.1838 |    0.1798 |                       8 |             15 |
| horizon           |       1   | patchtst     | mssa        |          -0.0066 |  -0.0454 |    0.0346 |                       6 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.0469 |  -0.1062 |    0.0144 |                       6 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.0813 |  -0.1695 |    0.0167 |                       4 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.0899 |  -0.2295 |    0.0724 |                       4 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.0066 |  -0.046  |    0.035  |                       6 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.0305 |  -0.0693 |    0.0076 |                       6 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.0995 |  -0.1507 |   -0.0515 |                       2 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.1274 |  -0.2065 |   -0.0492 |                       4 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.0064 |  -0.0457 |    0.034  |                       7 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0865 |  -0.138  |   -0.0383 |                       4 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.1217 |  -0.198  |   -0.0468 |                       4 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.6209 |   2.8435 |    4.3801 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.7578 |   1.155  |    2.3955 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.1546 |  -0.1799 |    0.4705 |                      10 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.0408 |  -0.1374 |    0.2129 |                       8 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.011  |  -0.0192 |    0.0406 |                       9 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0234 |  -0.0348 |    0.0803 |                       8 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.1213 |   0.017  |    0.2196 |                      11 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.3341 |   0.1792 |    0.4796 |                      13 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.011  |  -0.0189 |    0.0399 |                       9 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0081 |  -0.0316 |    0.0483 |                       7 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.0124 |  -0.0488 |    0.0727 |                       7 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.1065 |  -0.0133 |    0.2202 |                      12 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0144 |  -0.0245 |    0.0521 |                       8 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0052 |  -0.0519 |    0.0627 |                       6 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.0944 |  -0.0169 |    0.205  |                      12 |             15 |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8704 |          0.1296 |       0.1922 |
| gbm_residual | temp_plus5 |          0.6713 |          0.3287 |       0.0106 |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.7705 |          0.2295 |       0.5005 |
| lstm         | temp_plus5 |          0.6979 |          0.3021 |       0.126  |
| mssa         | load_x2    |          1      |          0      |       0.4992 |
| mssa         | temp_plus5 |          1      |          0      |       0.8764 |
| patchtst     | load_x2    |          0.743  |          0.257  |       0.4982 |
| patchtst     | temp_plus5 |          0.743  |          0.257  |       0.1183 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.9636 | 1.9825 | 2.3135 |
| mssa     | native    | 0.8885 | 1.2592 | 2.4919 |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.8497 |                 8.7956 |
|    0.2 |          10 |           0.4707 |                13.945  |
|    0.4 |           8 |           0.688  |                 2.7425 |
|    0.4 |          10 |           0.482  |                14.292  |
|    0.6 |           8 |           0.6798 |                 0.19   |
|    0.6 |          10 |           0.3952 |                 3.57   |
