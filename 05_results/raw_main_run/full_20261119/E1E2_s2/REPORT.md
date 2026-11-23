# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E1E2_s2`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.3662 |        nan |     1.0784 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |        nan |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |        nan |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.076  |        nan |     4.5161 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.8899 |        nan |     1.4937 |      0.5516 |      2.6839 |      1.1911 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.1152 |        nan |     4.5324 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |        nan |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      0.9481 |        nan |     0.7712 |    nan      |    nan      |    nan      |             0.7952 |                0.1122 |                        nan |           12.3237 |             2.34   |
| gbm_residual |       0.4 |      0.5108 |        nan |     0.4106 |    nan      |    nan      |    nan      |             0.4735 |                0.146  |                        nan |            5.54   |            12.63   |
| gbm_residual |       0.6 |      0.4743 |        nan |     0.3636 |    nan      |    nan      |    nan      |             0.3946 |                0.1394 |                        nan |            2.72   |             4.8567 |
| jtg_enkf     |       0.2 |      2.1483 |        nan |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |        nan |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |        nan |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |        nan |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |        nan |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |        nan |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      3.0017 |        nan |     2.4835 |    nan      |    nan      |    nan      |             3.9548 |                0.3041 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.0593 |        nan |     0.8287 |    nan      |    nan      |    nan      |             1.504  |                0.2517 |                        nan |            7.37   |             0.87   |
| lstm         |       0.6 |      0.6596 |        nan |     0.5055 |    nan      |    nan      |    nan      |             0.7568 |                0.2197 |                        nan |            1.56   |            10.69   |
| mssa         |       0.2 |      1.6692 |        nan |     1.2811 |      0.4636 |      1.8436 |      1.057  |             1.5555 |                0.0726 |                          0 |           17.444  |           nan      |
| mssa         |       0.4 |      1.2637 |        nan |     0.9851 |      0.5588 |      1.803  |      0.7895 |             1.1962 |                0.0914 |                          0 |            8.89   |            18.04   |
| mssa         |       0.6 |      0.8122 |        nan |     0.6169 |      0.7842 |      1.7185 |      0.4581 |             0.8234 |                0.0781 |                          0 |            1.56   |           nan      |
| patchtst     |       0.2 |      3.0616 |        nan |     2.5537 |    nan      |    nan      |    nan      |             4.0064 |                0.3301 |                        nan |          nan      |           nan      |
| patchtst     |       0.4 |      1.0773 |        nan |     0.8533 |    nan      |    nan      |    nan      |             1.5556 |                0.2926 |                        nan |            6.3567 |           nan      |
| patchtst     |       0.6 |      0.6458 |        nan |     0.5062 |    nan      |    nan      |    nan      |             0.7946 |                0.2601 |                        nan |          nan      |            11.47   |
| persistence  |       0.2 |      3.2132 |        nan |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |        nan |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |        nan |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.363  |        nan |     0.2626 |      0.9228 |      1.2517 |      0.1936 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.396  |        nan |     0.2882 |      0.8988 |      1.2517 |      0.2131 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.4627 |        nan |     0.3378 |      0.8631 |      1.2517 |      0.251  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.5443 |        nan |     0.3973 |      0.7989 |      1.2517 |      0.3021 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |        nan |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |        nan |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |        nan |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |        nan |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |        nan |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |        nan |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.3998 |        nan |     0.2904 |      0.8027 |      0.9232 |      0.2199 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4883 |        nan |     0.3504 |      0.7395 |      0.9232 |      0.2723 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5597 |        nan |     0.4087 |      0.6735 |      0.9232 |      0.3228 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.716  |        nan |     0.5234 |      0.5843 |      0.9232 |      0.4299 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3971 |        nan |     0.2923 |      0.8928 |      1.2451 |      0.2155 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5293 |        nan |     0.4029 |      0.8519 |      1.4235 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6799 |        nan |     0.5217 |      0.7918 |      1.551  |      0.388  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.8651 |        nan |     0.6644 |      0.7214 |      1.6543 |      0.5067 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.393  |        nan |     0.2801 |      0.8087 |      0.8741 |      0.2137 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4803 |        nan |     0.3444 |      0.732  |      0.8741 |      0.2691 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.5819 |        nan |     0.4264 |      0.6419 |      0.8741 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.7286 |        nan |     0.5355 |      0.5503 |      0.8741 |      0.4442 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |        nan |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |        nan |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |        nan |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.363  |        nan |     0.2626 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3715 |        nan |     0.2684 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3847 |        nan |     0.281  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4329 |        nan |     0.3187 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |        nan |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |        nan |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |        nan |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.3998 |        nan |     0.2904 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4209 |        nan |     0.3052 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4511 |        nan |     0.3292 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.529  |        nan |     0.3817 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3971 |        nan |     0.2923 |      0.8928 |      1.2451 |      0.2155 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4598 |        nan |     0.3465 |      0.8623 |      1.316  |      0.2544 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.571  |        nan |     0.434  |      0.8096 |      1.4059 |      0.323  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.7326 |        nan |     0.5561 |      0.7477 |      1.515  |      0.4218 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.393  |        nan |     0.2801 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4174 |        nan |     0.2972 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4488 |        nan |     0.3228 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5331 |        nan |     0.3777 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |        nan |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |        nan |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |        nan |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3681 |        nan |     0.2694 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3705 |        nan |     0.273  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4192 |        nan |     0.3092 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |        nan |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |        nan |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |        nan |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |        nan |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |        nan |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |        nan |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4148 |        nan |     0.3013 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4459 |        nan |     0.3238 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5125 |        nan |     0.372  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4191 |        nan |     0.3167 |      0.8719 |      1.2659 |      0.2324 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5405 |        nan |     0.4099 |      0.8154 |      1.3734 |      0.3051 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.7078 |        nan |     0.5369 |      0.752  |      1.4973 |      0.4065 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4107 |        nan |     0.2954 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4382 |        nan |     0.3158 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5155 |        nan |     0.3685 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |        nan |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |        nan |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |        nan |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.4055 |  -0.7968 |   -0.0577 |                       5 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.5283 |  -0.8929 |   -0.1753 |                       3 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.5849 |  -0.8964 |   -0.2892 |                       2 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.2642 |  -0.4803 |   -0.054  |                       4 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0393 |  -0.0708 |   -0.0017 |                       3 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.1307 |  -0.1702 |   -0.0943 |                       0 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.2042 |  -0.2647 |   -0.1463 |                       0 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.2902 |  -0.3921 |   -0.1941 |                       0 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0393 |  -0.0704 |   -0.0016 |                       3 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0889 |  -0.127  |   -0.0537 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.173  |  -0.2259 |   -0.123  |                       0 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.265  |  -0.3554 |   -0.1819 |                       0 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.053  |  -0.0877 |   -0.0172 |                       3 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1587 |  -0.2121 |   -0.1098 |                       1 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.2548 |  -0.3424 |   -0.1718 |                       0 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |          -0.2737 |  -0.8192 |    0.1781 |                       5 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.5499 |  -0.2302 |    1.2836 |                      10 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.194  |  -0.5353 |    0.1536 |                       6 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1533 |  -0.3882 |    0.0652 |                       6 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0243 |  -0.0029 |    0.0476 |                      12 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0401 |  -0.0991 |    0.0087 |                       6 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0989 |  -0.1963 |   -0.0198 |                       5 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.1261 |  -0.277  |    0.0041 |                       5 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0243 |  -0.0028 |    0.0478 |                      12 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0249 |  -0.0728 |    0.0148 |                       8 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0982 |  -0.183  |   -0.0281 |                       5 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.1648 |  -0.3101 |   -0.0477 |                       5 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |          -0.0068 |  -0.045  |    0.0251 |                       8 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0834 |  -0.1592 |   -0.0176 |                       6 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.1579 |  -0.2924 |   -0.0472 |                       5 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |          -0.2386 |  -0.7046 |    0.1385 |                       5 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.0727 |  -0.3905 |    0.4792 |                      10 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.4817 |   0.0773 |    0.9022 |                      12 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           0.9098 |   0.4782 |    1.3656 |                      12 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0033 |   0.6434 |    1.397  |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.8827 |   0.5331 |    1.2635 |                      14 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.7516 |   0.4086 |    1.1147 |                      12 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.6056 |   0.2567 |    0.9615 |                      10 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0033 |   0.6344 |    1.4003 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.9468 |   0.5896 |    1.3363 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.8512 |   0.5183 |    1.1975 |                      14 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.7157 |   0.3984 |    1.0472 |                      13 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           0.9838 |   0.6286 |    1.3764 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.8806 |   0.5464 |    1.2394 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.7381 |   0.4189 |    1.079  |                      13 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.2877 |   2.5597 |    3.9442 |                      14 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.3773 |   0.7904 |    1.8604 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |          -0.081  |  -0.373  |    0.1827 |                       6 |             15 |
| early_life        |       0.6 | lstm         | mssa        |          -0.0636 |  -0.2402 |    0.0992 |                       7 |             15 |
| horizon           |       1   | lstm         | mssa        |          -0.0014 |  -0.0324 |    0.0369 |                       4 |             15 |
| horizon           |       3   | lstm         | mssa        |          -0.0476 |  -0.1234 |    0.0377 |                       3 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.1173 |  -0.233  |   -0.0029 |                       3 |             15 |
| horizon           |      12   | lstm         | mssa        |          -0.1585 |  -0.3175 |    0.0228 |                       3 |             15 |
| sparse_all        |       1   | lstm         | mssa        |          -0.0014 |  -0.0321 |    0.036  |                       4 |             15 |
| sparse_all        |       2   | lstm         | mssa        |          -0.0387 |  -0.0839 |    0.0093 |                       3 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.1025 |  -0.1758 |   -0.0349 |                       3 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.1593 |  -0.2865 |   -0.0641 |                       1 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |          -0.0064 |  -0.0496 |    0.0421 |                       5 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.08   |  -0.1477 |   -0.0137 |                       4 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.1511 |  -0.2717 |   -0.0567 |                       2 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.3188 |   2.5626 |    3.9726 |                      14 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.4295 |   0.845  |    1.9245 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |          -0.0679 |  -0.3335 |    0.1836 |                       6 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |          -0.0746 |  -0.2531 |    0.0907 |                       6 |             15 |
| horizon           |       1   | patchtst     | mssa        |          -0.0076 |  -0.0415 |    0.0242 |                       6 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.0523 |  -0.1156 |    0.0108 |                       3 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.1002 |  -0.1917 |   -0.0005 |                       2 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.1382 |  -0.2728 |    0.0174 |                       2 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.0076 |  -0.0415 |    0.0242 |                       6 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.04   |  -0.079  |   -0.0023 |                       4 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.1035 |  -0.1807 |   -0.0389 |                       3 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.1598 |  -0.2926 |   -0.0622 |                       1 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.0083 |  -0.0488 |    0.0331 |                       6 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0863 |  -0.1634 |   -0.0187 |                       4 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.1532 |  -0.2839 |   -0.0545 |                       1 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.509  |   2.7584 |    4.1714 |                      14 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.5786 |   0.9577 |    2.0949 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |          -0.0048 |  -0.2723 |    0.2478 |                       8 |             15 |
| early_life        |       0.6 | persistence  | mssa        |          -0.0482 |  -0.2391 |    0.1229 |                       7 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0121 |  -0.0218 |    0.0401 |                      11 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0207 |  -0.0435 |    0.0718 |                      10 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.1094 |  -0.0089 |    0.2043 |                      12 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.3018 |   0.1205 |    0.4521 |                      13 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0121 |  -0.0228 |    0.0397 |                      11 |             15 |
| sparse_all        |       2   | persistence  | mssa        |          -0.0025 |  -0.052  |    0.0392 |                      10 |             15 |
| sparse_all        |       4   | persistence  | mssa        |          -0.0153 |  -0.1006 |    0.0504 |                      11 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.0599 |  -0.1033 |    0.1846 |                      12 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0062 |  -0.0414 |    0.0452 |                      10 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.0213 |  -0.095  |    0.0366 |                      10 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.0481 |  -0.1042 |    0.1648 |                      12 |             15 |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8679 |          0.1321 |       0.1493 |
| gbm_residual | temp_plus5 |          0.6648 |          0.3312 |      -0.001  |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.7811 |          0.2189 |       0.581  |
| lstm         | temp_plus5 |          0.7356 |          0.2644 |       0.125  |
| mssa         | load_x2    |          1      |          0      |       0.4314 |
| mssa         | temp_plus5 |          1      |          0      |       0.8125 |
| patchtst     | load_x2    |          0.7733 |          0.2267 |       0.4482 |
| patchtst     | temp_plus5 |          0.7811 |          0.2189 |       0.1342 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.9649 | 1.9334 | 2.2568 |
| mssa     | native    | 0.8889 | 1.2401 | 2.4718 |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7996 |                12.3988 |
|    0.2 |          10 |           0.3804 |                11.7933 |
|    0.4 |           8 |           0.7374 |                 8.2367 |
|    0.4 |          10 |           0.3255 |                 8.38   |
|    0.6 |           8 |           0.6688 |                 4.705  |
|    0.6 |          10 |           0.2823 |                 7.6967 |
