# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E1E2_s0`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.4085 |        nan |     1.1048 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |        nan |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |        nan |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.1108 |        nan |     4.5538 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.646  |        nan |     1.1766 |      0.7338 |      3.0337 |      0.9365 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.1006 |        nan |     4.5153 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |        nan |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.017  |        nan |     0.8365 |    nan      |    nan      |    nan      |             0.9109 |                0.1237 |                        nan |            9.8814 |           nan      |
| gbm_residual |       0.4 |      0.5119 |        nan |     0.4133 |    nan      |    nan      |    nan      |             0.4806 |                0.1561 |                        nan |            6.21   |            12.4425 |
| gbm_residual |       0.6 |      0.4919 |        nan |     0.3843 |    nan      |    nan      |    nan      |             0.4172 |                0.1463 |                        nan |            2.34   |             4.47   |
| jtg_enkf     |       0.2 |      2.1483 |        nan |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |        nan |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |        nan |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |        nan |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |        nan |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |        nan |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      3.0281 |        nan |     2.5112 |    nan      |    nan      |    nan      |             3.9654 |                0.3138 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.0782 |        nan |     0.8596 |    nan      |    nan      |    nan      |             1.5146 |                0.2717 |                        nan |           17.0833 |           nan      |
| lstm         |       0.6 |      0.6504 |        nan |     0.5025 |    nan      |    nan      |    nan      |             0.7662 |                0.2321 |                        nan |          nan      |             9.92   |
| mssa         |       0.2 |      1.4854 |        nan |     1.1084 |      0.6309 |      2.1351 |      0.8886 |             1.3834 |                0.0656 |                          0 |           13.1457 |           nan      |
| mssa         |       0.4 |      1.1408 |        nan |     0.8883 |      0.6595 |      2.0734 |      0.6934 |             1.058  |                0.076  |                          0 |            7.63   |            19.6    |
| mssa         |       0.6 |      0.681  |        nan |     0.5467 |      0.8162 |      1.9819 |      0.3968 |             0.6647 |                0.0677 |                          0 |            0.38   |            15.35   |
| patchtst     |       0.2 |      3.0508 |        nan |     2.5191 |    nan      |    nan      |    nan      |             3.9533 |                0.315  |                        nan |          nan      |           nan      |
| patchtst     |       0.4 |      1.0348 |        nan |     0.8314 |    nan      |    nan      |    nan      |             1.5025 |                0.2888 |                        nan |           13.2333 |           nan      |
| patchtst     |       0.6 |      0.6197 |        nan |     0.4815 |    nan      |    nan      |    nan      |             0.7464 |                0.2625 |                        nan |          nan      |            10.69   |
| persistence  |       0.2 |      3.2132 |        nan |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |        nan |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |        nan |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3692 |        nan |     0.2678 |      0.9168 |      1.2496 |      0.1976 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4022 |        nan |     0.2929 |      0.8927 |      1.2496 |      0.2169 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.4697 |        nan |     0.343  |      0.8559 |      1.2496 |      0.2559 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.5426 |        nan |     0.398  |      0.7934 |      1.2496 |      0.3024 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4757 |        nan |     0.361  |      0.6884 |      0.8973 |      0.2787 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5539 |        nan |     0.4283 |      0.6285 |      0.9948 |      0.3333 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.6931 |        nan |     0.5249 |      0.5968 |      1.1886 |      0.4119 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |      0.9085 |      5.9958 |      0.9127 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      1.6085 |        nan |     1.266  |      0.9072 |      5.9958 |      0.9168 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      1.6193 |        nan |     1.2735 |      0.9052 |      5.9959 |      0.9238 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      1.6457 |        nan |     1.297  |      0.901  |      5.9959 |      0.9413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4191 |        nan |     0.2942 |      0.7994 |      0.9141 |      0.2258 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4837 |        nan |     0.3453 |      0.7362 |      0.9141 |      0.2697 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5631 |        nan |     0.4115 |      0.6697 |      0.9141 |      0.3263 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.7338 |        nan |     0.5292 |      0.5703 |      0.9141 |      0.4353 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3888 |        nan |     0.2824 |      0.9247 |      1.3837 |      0.2087 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.5086 |        nan |     0.3837 |      0.8941 |      1.6099 |      0.2794 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6461 |        nan |     0.4907 |      0.8545 |      1.7774 |      0.3607 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7986 |        nan |     0.6012 |      0.8024 |      1.9137 |      0.4507 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3951 |        nan |     0.2839 |      0.8073 |      0.8914 |      0.2159 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.497  |        nan |     0.3537 |      0.7263 |      0.8914 |      0.2774 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.614  |        nan |     0.4436 |      0.6362 |      0.8914 |      0.3576 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.7368 |        nan |     0.5362 |      0.5583 |      0.8914 |      0.444  |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5398 |        nan |     0.3814 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.771  |        nan |     0.548  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1315 |        nan |     0.792  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.3692 |        nan |     0.2678 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3765 |        nan |     0.2726 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3909 |        nan |     0.2862 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4397 |        nan |     0.3253 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4181 |        nan |     0.3111 |      0.7398 |      0.8482 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4254 |        nan |     0.3192 |      0.7454 |      0.8908 |      0.2434 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4485 |        nan |     0.3353 |      0.7579 |      0.9537 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5215 |        nan |     0.3858 |      0.7472 |      1.0687 |      0.2918 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6021 |        nan |     1.2622 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4191 |        nan |     0.2942 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4417 |        nan |     0.3112 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4576 |        nan |     0.3265 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5431 |        nan |     0.3817 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3888 |        nan |     0.2824 |      0.9247 |      1.3837 |      0.2087 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4424 |        nan |     0.3281 |      0.9048 |      1.4656 |      0.2405 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5244 |        nan |     0.3967 |      0.8817 |      1.5784 |      0.2896 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6637 |        nan |     0.5014 |      0.8193 |      1.7145 |      0.372  |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3951 |        nan |     0.2839 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4213 |        nan |     0.3017 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4603 |        nan |     0.3301 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5646 |        nan |     0.396  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4082 |        nan |     0.2792 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4522 |        nan |     0.3102 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.54   |        nan |     0.3652 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7638 |        nan |     0.4987 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.3749 |        nan |     0.2752 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3773 |        nan |     0.2785 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4273 |        nan |     0.3163 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |        nan |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |        nan |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |        nan |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |        nan |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |        nan |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |        nan |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4325 |        nan |     0.3085 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4498 |        nan |     0.3226 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5273 |        nan |     0.3731 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4069 |        nan |     0.3013 |      0.9115 |      1.4016 |      0.222  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4932 |        nan |     0.3726 |      0.8892 |      1.536  |      0.2725 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6386 |        nan |     0.4835 |      0.828  |      1.6908 |      0.3578 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4072 |        nan |     0.2963 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4465 |        nan |     0.3217 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5446 |        nan |     0.3853 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |        nan |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |        nan |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |        nan |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.0537 |  -0.5799 |    0.4224 |                       8 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.2921 |  -0.5968 |   -0.0088 |                       4 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.4808 |  -0.7649 |   -0.2253 |                       1 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1658 |  -0.3279 |    0.0105 |                       4 |             15 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0253 |  -0.0612 |    0.0137 |                       3 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0998 |  -0.1508 |   -0.056  |                       1 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1553 |  -0.2419 |   -0.0835 |                       2 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.2122 |  -0.3356 |   -0.1064 |                       2 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0253 |  -0.0598 |    0.0135 |                       3 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0655 |  -0.1059 |   -0.0286 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.1221 |  -0.1784 |   -0.0755 |                       1 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1931 |  -0.285  |   -0.1135 |                       1 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0343 |  -0.0694 |    0.0015 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.1072 |  -0.1593 |   -0.0656 |                       1 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1814 |  -0.27   |   -0.1052 |                       1 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.0512 |  -0.5086 |    0.4998 |                       9 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.723  |  -0.0064 |    1.3901 |                       9 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.0924 |  -0.3776 |    0.1838 |                       7 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0747 |  -0.2621 |    0.1029 |                       9 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0343 |  -0.0004 |    0.0626 |                      12 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0142 |  -0.0844 |    0.0455 |                      11 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0562 |  -0.1707 |    0.0355 |                       9 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.0462 |  -0.2123 |    0.0961 |                       9 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0343 |   0.0005 |    0.0627 |                      12 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.0046 |  -0.0603 |    0.0412 |                      11 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.052  |  -0.1359 |    0.0171 |                      10 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0991 |  -0.2365 |    0.0117 |                      10 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0075 |  -0.0355 |    0.0422 |                      11 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0372 |  -0.1095 |    0.0232 |                       9 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0918 |  -0.2196 |    0.0144 |                       9 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |           0.0864 |  -0.466  |    0.5715 |                       9 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.2458 |  -0.2862 |    0.7191 |                       8 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.5833 |   0.0882 |    1.073  |                       9 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           0.9884 |   0.5053 |    1.4834 |                      12 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0133 |   0.6554 |    1.4032 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.9086 |   0.5533 |    1.292  |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.7942 |   0.4348 |    1.173  |                      14 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.6855 |   0.2938 |    1.0829 |                      10 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0133 |   0.6477 |    1.4064 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           0.9672 |   0.6113 |    1.3554 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.8974 |   0.5537 |    1.2542 |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.7814 |   0.445  |    1.1381 |                      14 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           0.9981 |   0.6425 |    1.3871 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9268 |   0.582  |    1.2948 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.8042 |   0.4616 |    1.1723 |                      15 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.646  |   2.7832 |    4.4777 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.5782 |   0.9691 |    2.1734 |                      14 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.0431 |  -0.2946 |    0.3295 |                       9 |             15 |
| early_life        |       0.6 | lstm         | mssa        |           0.0111 |  -0.1496 |    0.162  |                       8 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.0249 |  -0.0122 |    0.0708 |                       9 |             15 |
| horizon           |       3   | lstm         | mssa        |          -0.0265 |  -0.0773 |    0.0426 |                       3 |             15 |
| horizon           |       6   | lstm         | mssa        |          -0.0695 |  -0.1694 |    0.043  |                       3 |             15 |
| horizon           |      12   | lstm         | mssa        |          -0.0611 |  -0.2234 |    0.1377 |                       4 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.0249 |  -0.0127 |    0.0717 |                       9 |             15 |
| sparse_all        |       2   | lstm         | mssa        |          -0.0004 |  -0.0469 |    0.0535 |                       6 |             15 |
| sparse_all        |       4   | lstm         | mssa        |          -0.0503 |  -0.1284 |    0.0212 |                       6 |             15 |
| sparse_all        |       8   | lstm         | mssa        |          -0.081  |  -0.2051 |    0.0231 |                       7 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0235 |  -0.0212 |    0.0726 |                       9 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.0297 |  -0.1063 |    0.0399 |                       7 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.0734 |  -0.1948 |    0.0264 |                       7 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.6174 |   2.6937 |    4.4461 |                      14 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.5746 |   0.9257 |    2.2147 |                      14 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.0121 |  -0.3065 |    0.2967 |                       8 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |          -0.0192 |  -0.1882 |    0.1274 |                       8 |             15 |
| horizon           |       1   | patchtst     | mssa        |           0.0043 |  -0.0278 |    0.0386 |                       8 |             15 |
| horizon           |       3   | patchtst     | mssa        |          -0.01   |  -0.0683 |    0.0565 |                       5 |             15 |
| horizon           |       6   | patchtst     | mssa        |          -0.0297 |  -0.129  |    0.091  |                       5 |             15 |
| horizon           |      12   | patchtst     | mssa        |          -0.0415 |  -0.1712 |    0.1076 |                       5 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |           0.0043 |  -0.0283 |    0.0393 |                       8 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.0172 |  -0.0544 |    0.0243 |                       5 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.0474 |  -0.114  |    0.0142 |                       5 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.0656 |  -0.1913 |    0.0373 |                       9 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |           0.0008 |  -0.033  |    0.0374 |                       7 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.0318 |  -0.0967 |    0.0263 |                       6 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.0609 |  -0.1801 |    0.0394 |                      10 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.834  |   2.9539 |    4.6579 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.7516 |   1.1121 |    2.3748 |                      14 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.0968 |  -0.2321 |    0.3925 |                       9 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.0304 |  -0.1461 |    0.183  |                       9 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0221 |  -0.0231 |    0.0599 |                      12 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.0466 |  -0.0321 |    0.1134 |                      12 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.152  |   0.013  |    0.2707 |                      12 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.3817 |   0.1809 |    0.5608 |                      12 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0221 |  -0.0229 |    0.0591 |                      12 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0178 |  -0.042  |    0.0687 |                      12 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.0308 |  -0.06   |    0.1066 |                      11 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.1256 |  -0.0418 |    0.2696 |                      12 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0204 |  -0.036  |    0.0678 |                      12 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.025  |  -0.0548 |    0.0924 |                      11 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1142 |  -0.047  |    0.2517 |                      12 |             15 |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8574 |          0.1426 |       0.1731 |
| gbm_residual | temp_plus5 |          0.6713 |          0.3287 |       0.0173 |
| jtg_enkf     | load_x2    |          0.5798 |          0.4137 |       0.0487 |
| jtg_enkf     | temp_plus5 |          0.7649 |          0.2351 |       0.1892 |
| jtg_global   | load_x2    |          1      |          0      |       1.4494 |
| jtg_global   | temp_plus5 |          1      |          0      |       6.1406 |
| lstm         | load_x2    |          0.7709 |          0.2291 |       0.5611 |
| lstm         | temp_plus5 |          0.703  |          0.297  |       0.1187 |
| mssa         | load_x2    |          1      |          0      |       0.4577 |
| mssa         | temp_plus5 |          1      |          0      |       0.93   |
| patchtst     | load_x2    |          0.7416 |          0.2584 |       0.5069 |
| patchtst     | temp_plus5 |          0.7976 |          0.2024 |       0.1357 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf | native    | 0.723  | 0.8359 | 3.7425 |
| mssa     | aci       | 0.9653 | 1.8872 | 2.2706 |
| mssa     | native    | 0.9201 | 1.3713 | 2.278  |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7641 |                 9.0167 |
|    0.2 |          10 |           0.5623 |                 4.26   |
|    0.4 |           8 |           0.672  |                 7.6    |
|    0.4 |          10 |           0.4729 |                 3.62   |
|    0.6 |           8 |           0.6115 |                 6.53   |
|    0.6 |          10 |           0.3591 |                 5.5033 |
