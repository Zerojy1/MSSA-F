# MSSA-Rut experiment report

Run directory: `../merged_v3b`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         0 |      1.3175 |   nan      |     1.0244 |      0.8591 |      4.2763 |      0.7359 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         0 |      1.3528 |   nan      |     1.08   |      0.3905 |      1.4076 |      0.9151 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         0 |      1.3629 |     0.0372 |     1.086  |      0.3565 |      1.2501 |      0.9376 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.6174 |     0      |     1.2238 |      0.9793 |     10.0538 |      0.9367 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      1.5988 |     0      |     1.2602 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      5.0852 |     0.0606 |     4.5183 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.576  |     0.0755 |     1.1812 |      0.8503 |      4.7025 |      0.8681 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         0 |      1.4565 |   nan      |     1.0835 |      0.8669 |      5.3282 |      0.8148 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      5.1003 |     0.0332 |     4.5235 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.3018 |     0      |     4.7906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |       0.2 |      0.9667 |   nan      |     0.7479 |      0.8562 |      3.4324 |      0.5563 |             0.8499 |                0.0741 |                        nan |            9.35   |             9.035  |
| fusion       |       0.4 |      0.5053 |   nan      |     0.3871 |      0.9771 |      2.434  |      0.2867 |             0.4847 |                0.1113 |                        nan |            1.1067 |            12.14   |
| fusion       |       0.6 |      0.4524 |   nan      |     0.3449 |      0.9269 |      2.0168 |      0.253  |             0.3814 |                0.086  |                        nan |            2.72   |             8.255  |
| gbm_ens      |       0.2 |      0.965  |   nan      |     0.7885 |      0.4923 |      1.3096 |      0.6387 |             0.8366 |                0.1116 |                        nan |           12.6225 |           nan      |
| gbm_ens      |       0.4 |      0.5137 |   nan      |     0.4145 |      0.8099 |      1.2763 |      0.3026 |             0.4721 |                0.1406 |                        nan |            5.7733 |            11.855  |
| gbm_ens      |       0.6 |      0.4715 |   nan      |     0.362  |      0.8105 |      1.2668 |      0.2703 |             0.3901 |                0.1406 |                        nan |            2.34   |             5.1267 |
| gbm_residual |       0.2 |      0.9699 |     0.0303 |     0.791  |      0.4585 |      1.2501 |      0.6472 |             0.8367 |                0.1188 |                        nan |           11.4815 |             2.34   |
| gbm_residual |       0.4 |      0.5179 |     0.0066 |     0.4172 |      0.794  |      1.2501 |      0.3064 |             0.473  |                0.1568 |                        nan |            4.9347 |            12.224  |
| gbm_residual |       0.6 |      0.4743 |     0.0122 |     0.3645 |      0.8018 |      1.25   |      0.2726 |             0.3913 |                0.1419 |                        nan |            2.416  |             4.6807 |
| jtg_enkf     |       0.2 |      2.1483 |     0      |     1.766  |      0.451  |      3.1711 |      1.3816 |             2.5828 |                0      |                        nan |            8.8489 |            11.874  |
| jtg_enkf     |       0.4 |      0.9505 |     0      |     0.7692 |      0.529  |      1.4954 |      0.6037 |             1.1299 |                0      |                        nan |            7.2175 |             3.358  |
| jtg_enkf     |       0.6 |      0.5889 |     0      |     0.463  |      0.6119 |      0.9991 |      0.3643 |             0.4906 |                0      |                        nan |            0      |             8.645  |
| jtg_global   |       0.2 |      1.7184 |     0      |     1.3623 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |           13.155  |           nan      |
| jtg_global   |       0.4 |      1.8522 |     0      |     1.484  |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| jtg_global   |       0.6 |      1.934  |     0      |     1.5499 |    nan      |    nan      |    nan      |             1.6455 |                0      |                        nan |          nan      |           nan      |
| lstm         |       0.2 |      3.0204 |     0.0396 |     2.5058 |    nan      |    nan      |    nan      |             3.8922 |                0.2973 |                        nan |          nan      |           nan      |
| lstm         |       0.4 |      1.0651 |     0.0402 |     0.8377 |    nan      |    nan      |    nan      |             1.4414 |                0.2521 |                        nan |           10.6493 |             0.59   |
| lstm         |       0.6 |      0.651  |     0.014  |     0.5    |    nan      |    nan      |    nan      |             0.7024 |                0.2172 |                        nan |            1.56   |             9.55   |
| mssa         |       0.2 |      1.2368 |     0.1896 |     0.9622 |      0.8434 |      3.7307 |      0.6918 |             1.1624 |                0.0811 |                          0 |           10.7735 |             9.486  |
| mssa         |       0.4 |      0.6165 |     0.0388 |     0.4831 |      0.9722 |      2.8663 |      0.3473 |             0.6623 |                0.0801 |                          0 |            1.636  |             6.916  |
| mssa         |       0.6 |      0.5525 |     0.017  |     0.4331 |      0.942  |      2.1891 |      0.3063 |             0.6316 |                0.0691 |                          0 |            2.72   |            14.19   |
| mssa_ens     |       0.2 |      1.1305 |   nan      |     0.8957 |      0.8814 |      4.1296 |      0.6462 |             1.062  |                0.0603 |                        nan |            9.405  |             1.77   |
| mssa_ens     |       0.4 |      0.5996 |   nan      |     0.4718 |      0.9855 |      2.9236 |      0.3389 |             0.6592 |                0.0635 |                        nan |            0.5867 |             6.7433 |
| mssa_ens     |       0.6 |      0.5445 |   nan      |     0.4237 |      0.9509 |      2.2279 |      0.3011 |             0.6093 |                0.0444 |                        nan |          nan      |            14.19   |
| patchtst     |       0.2 |      3.0452 |     0.0167 |     2.5259 |    nan      |    nan      |    nan      |             3.9384 |                0.3198 |                        nan |           15.33   |           nan      |
| patchtst     |       0.4 |      1.0577 |     0.0193 |     0.837  |    nan      |    nan      |    nan      |             1.4876 |                0.2844 |                        nan |           11.6927 |           nan      |
| patchtst     |       0.6 |      0.6387 |     0.0111 |     0.4926 |    nan      |    nan      |    nan      |             0.7324 |                0.2538 |                        nan |          nan      |             8.4425 |
| persistence  |       0.2 |      3.2132 |     0      |     2.7371 |    nan      |    nan      |    nan      |             3.9014 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.1368 |     0      |     0.9179 |    nan      |    nan      |    nan      |             1.4506 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.6973 |     0      |     0.5372 |    nan      |    nan      |    nan      |             0.7199 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         1 |      0.329  |   nan      |     0.2326 |      0.9566 |      1.364  |      0.1738 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         3 |      0.3752 |   nan      |     0.2711 |      0.9508 |      1.5149 |      0.2003 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         6 |      0.4424 |   nan      |     0.3253 |      0.9435 |      1.6751 |      0.2366 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |        12 |      0.5106 |   nan      |     0.3759 |      0.9365 |      1.8985 |      0.2735 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         1 |      0.3606 |   nan      |     0.262  |      0.9251 |      1.2609 |      0.1928 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         3 |      0.3953 |   nan      |     0.2877 |      0.8983 |      1.2617 |      0.2127 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         6 |      0.4627 |   nan      |     0.3374 |      0.865  |      1.2639 |      0.2511 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |        12 |      0.5396 |   nan      |     0.3951 |      0.8054 |      1.268  |      0.2993 |                nan |                   nan |                        nan |               nan |                nan |
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
| mssa         |         1 |      0.3478 |     0.0015 |     0.2401 |      0.9291 |      1.2841 |      0.1816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4145 |     0.0021 |     0.2996 |      0.9318 |      1.5307 |      0.2209 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.4943 |     0.0053 |     0.3666 |      0.9249 |      1.7487 |      0.2665 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.5855 |     0.0099 |     0.4356 |      0.9218 |      2.0049 |      0.316  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         1 |      0.3455 |   nan      |     0.2381 |      0.9316 |      1.2957 |      0.1801 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         3 |      0.4094 |   nan      |     0.2949 |      0.9372 |      1.5549 |      0.2177 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         6 |      0.4853 |   nan      |     0.3598 |      0.9359 |      1.79   |      0.261  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |        12 |      0.5722 |   nan      |     0.4265 |      0.936  |      2.066  |      0.3079 |                nan |                   nan |                        nan |               nan |                nan |
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
| fusion       |         1 |      0.329  |   nan      |     0.2326 |      0.9566 |      1.364  |      0.1738 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         2 |      0.3493 |   nan      |     0.2501 |      0.9519 |      1.4172 |      0.1855 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         4 |      0.3747 |   nan      |     0.2735 |      0.9501 |      1.5072 |      0.2005 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         8 |      0.4273 |   nan      |     0.3124 |      0.9469 |      1.644  |      0.2286 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         1 |      0.3606 |   nan      |     0.262  |      0.9251 |      1.2609 |      0.1928 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         2 |      0.3699 |   nan      |     0.2683 |      0.9177 |      1.2612 |      0.1979 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         4 |      0.3849 |   nan      |     0.2814 |      0.9071 |      1.2625 |      0.2066 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         8 |      0.4343 |   nan      |     0.3193 |      0.8752 |      1.2643 |      0.2353 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         1 |      0.363  |     0.0043 |     0.2637 |      0.9211 |      1.2501 |      0.1943 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3723 |     0.0035 |     0.2701 |      0.9152 |      1.2501 |      0.1995 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.3876 |     0.0036 |     0.2833 |      0.9047 |      1.2501 |      0.2084 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.437  |     0.0037 |     0.3213 |      0.8731 |      1.2501 |      0.2374 |                nan |                   nan |                        nan |               nan |                nan |
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
| mssa         |         1 |      0.3478 |     0.0015 |     0.2401 |      0.9291 |      1.2841 |      0.1816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3801 |     0.0031 |     0.2692 |      0.9259 |      1.378  |      0.2011 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4249 |     0.0053 |     0.3091 |      0.9179 |      1.5061 |      0.2281 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.4953 |     0.0116 |     0.3651 |      0.9093 |      1.6837 |      0.2672 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         1 |      0.3455 |   nan      |     0.2381 |      0.9316 |      1.2957 |      0.1801 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         2 |      0.3761 |   nan      |     0.266  |      0.9321 |      1.3968 |      0.1985 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         4 |      0.4182 |   nan      |     0.3036 |      0.9265 |      1.5366 |      0.2239 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         8 |      0.4833 |   nan      |     0.3565 |      0.9261 |      1.7366 |      0.2597 |                nan |                   nan |                        nan |               nan |                nan |
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
| fusion       |         2 |      0.338  |   nan      |     0.2455 |      0.9521 |      1.376  |      0.1813 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         4 |      0.3576 |   nan      |     0.2634 |      0.9538 |      1.4749 |      0.1928 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         8 |      0.411  |   nan      |     0.3017 |      0.9488 |      1.621  |      0.2211 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         2 |      0.3678 |   nan      |     0.2698 |      0.9235 |      1.2607 |      0.1979 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         4 |      0.3705 |   nan      |     0.2736 |      0.9163 |      1.2616 |      0.1999 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         8 |      0.421  |   nan      |     0.3096 |      0.8828 |      1.2635 |      0.2279 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.3702 |     0.0033 |     0.2715 |      0.9185 |      1.2501 |      0.1995 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.373  |     0.0031 |     0.2754 |      0.9131 |      1.2501 |      0.2015 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.4236 |     0.0037 |     0.3117 |      0.8806 |      1.2501 |      0.2298 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4061 |     0      |     0.3071 |      0.7493 |      0.8797 |      0.2339 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4348 |     0      |     0.3255 |      0.7625 |      0.9394 |      0.2479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5042 |     0      |     0.3756 |      0.752  |      1.0549 |      0.2836 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      1.6007 |     0      |     1.259  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      1.6024 |     0      |     1.2631 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      1.6017 |     0      |     1.2618 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4198 |     0.0128 |     0.3028 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4456 |     0.0133 |     0.3217 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.517  |     0.0224 |     0.3707 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.357  |     0.0027 |     0.2545 |      0.9202 |      1.3104 |      0.191  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4042 |     0.0049 |     0.2954 |      0.9206 |      1.457  |      0.2179 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.476  |     0.0107 |     0.353  |      0.9115 |      1.6515 |      0.2581 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         2 |      0.3536 |   nan      |     0.2518 |      0.9272 |      1.3262 |      0.1888 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         4 |      0.3979 |   nan      |     0.2901 |      0.9286 |      1.4851 |      0.214  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         8 |      0.4642 |   nan      |     0.3449 |      0.9288 |      1.7027 |      0.2508 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4006 |     0.0112 |     0.2892 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4385 |     0.0211 |     0.3161 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5283 |     0.0281 |     0.377  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4212 |     0      |     0.2886 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5046 |     0      |     0.3428 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7264 |     0      |     0.4756 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - fusion), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_ens      | fusion      |           0.0755 |  -0.1218 |    0.2853 |                       9 |             15 |
| early_life        |       0.2 | gbm_ens      | fusion      |           0.0326 |  -0.1098 |    0.1772 |                       9 |             15 |
| early_life        |       0.4 | gbm_ens      | fusion      |           0.0223 |  -0.0378 |    0.0878 |                       9 |             15 |
| early_life        |       0.6 | gbm_ens      | fusion      |           0.026  |  -0.051  |    0.1102 |                       7 |             15 |
| horizon           |       1   | gbm_ens      | fusion      |           0.0245 |   0.0046 |    0.0531 |                      11 |             15 |
| horizon           |       3   | gbm_ens      | fusion      |           0.0123 |  -0.0064 |    0.0371 |                       7 |             15 |
| horizon           |       6   | gbm_ens      | fusion      |           0.011  |  -0.0101 |    0.0386 |                       7 |             15 |
| horizon           |      12   | gbm_ens      | fusion      |           0.0179 |  -0.0053 |    0.044  |                       8 |             15 |
| sparse_all        |       1   | gbm_ens      | fusion      |           0.0245 |   0.0049 |    0.0526 |                      11 |             15 |
| sparse_all        |       2   | gbm_ens      | fusion      |           0.013  |  -0.0072 |    0.0414 |                       7 |             15 |
| sparse_all        |       4   | gbm_ens      | fusion      |           0.0023 |  -0.0194 |    0.0314 |                       5 |             15 |
| sparse_all        |       8   | gbm_ens      | fusion      |          -0.0007 |  -0.0225 |    0.0265 |                       6 |             15 |
| sparse_unobserved |       2   | gbm_ens      | fusion      |           0.0223 |   0.0024 |    0.0518 |                      11 |             15 |
| sparse_unobserved |       4   | gbm_ens      | fusion      |           0.0051 |  -0.0162 |    0.0342 |                       7 |             15 |
| sparse_unobserved |       8   | gbm_ens      | fusion      |           0.0024 |  -0.0188 |    0.0282 |                       6 |             15 |
| cold_start        |       0   | gbm_residual | fusion      |           0.0837 |  -0.1107 |    0.2905 |                       9 |             15 |
| early_life        |       0.2 | gbm_residual | fusion      |           0.0367 |  -0.1038 |    0.1888 |                       9 |             15 |
| early_life        |       0.4 | gbm_residual | fusion      |           0.0258 |  -0.0352 |    0.0931 |                       9 |             15 |
| early_life        |       0.6 | gbm_residual | fusion      |           0.029  |  -0.0493 |    0.1124 |                       7 |             15 |
| horizon           |       1   | gbm_residual | fusion      |           0.0268 |   0.0072 |    0.0556 |                      12 |             15 |
| horizon           |       3   | gbm_residual | fusion      |           0.0147 |  -0.004  |    0.0394 |                       8 |             15 |
| horizon           |       6   | gbm_residual | fusion      |           0.0134 |  -0.0079 |    0.0413 |                       7 |             15 |
| horizon           |      12   | gbm_residual | fusion      |           0.0207 |  -0.0025 |    0.047  |                       9 |             15 |
| sparse_all        |       1   | gbm_residual | fusion      |           0.0268 |   0.0071 |    0.0554 |                      12 |             15 |
| sparse_all        |       2   | gbm_residual | fusion      |           0.0154 |  -0.0045 |    0.0434 |                       8 |             15 |
| sparse_all        |       4   | gbm_residual | fusion      |           0.0049 |  -0.0168 |    0.0337 |                       6 |             15 |
| sparse_all        |       8   | gbm_residual | fusion      |           0.0019 |  -0.0196 |    0.0287 |                       7 |             15 |
| sparse_unobserved |       2   | gbm_residual | fusion      |           0.0246 |   0.0045 |    0.0536 |                      11 |             15 |
| sparse_unobserved |       4   | gbm_residual | fusion      |           0.0077 |  -0.0136 |    0.0365 |                       7 |             15 |
| sparse_unobserved |       8   | gbm_residual | fusion      |           0.0049 |  -0.0166 |    0.0314 |                       7 |             15 |
| cold_start        |       0   | jtg_enkf     | fusion      |           0.2094 |  -0.1884 |    0.584  |                      10 |             15 |
| early_life        |       0.2 | jtg_enkf     | fusion      |           1.0982 |   0.5588 |    1.6568 |                      12 |             15 |
| early_life        |       0.4 | jtg_enkf     | fusion      |           0.4094 |   0.217  |    0.6059 |                      13 |             15 |
| early_life        |       0.6 | jtg_enkf     | fusion      |           0.1397 |   0.0845 |    0.2147 |                      14 |             15 |
| horizon           |       1   | jtg_enkf     | fusion      |           0.0902 |   0.0649 |    0.1107 |                      14 |             15 |
| horizon           |       3   | jtg_enkf     | fusion      |           0.1032 |   0.0753 |    0.1272 |                      14 |             15 |
| horizon           |       6   | jtg_enkf     | fusion      |           0.1158 |   0.0806 |    0.1483 |                      14 |             15 |
| horizon           |      12   | jtg_enkf     | fusion      |           0.1868 |   0.1287 |    0.2465 |                      14 |             15 |
| sparse_all        |       1   | jtg_enkf     | fusion      |           0.0902 |   0.0647 |    0.1104 |                      14 |             15 |
| sparse_all        |       2   | jtg_enkf     | fusion      |           0.0782 |   0.0499 |    0.0994 |                      14 |             15 |
| sparse_all        |       4   | jtg_enkf     | fusion      |           0.077  |   0.048  |    0.1043 |                      14 |             15 |
| sparse_all        |       8   | jtg_enkf     | fusion      |           0.0979 |   0.0485 |    0.1444 |                      14 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | fusion      |           0.0688 |   0.0418 |    0.0907 |                      14 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | fusion      |           0.0805 |   0.0564 |    0.1064 |                      14 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | fusion      |           0.0974 |   0.0525 |    0.1412 |                      14 |             15 |
| cold_start        |       0   | jtg_global   | fusion      |           0.2445 |  -0.0808 |    0.5505 |                      10 |             15 |
| early_life        |       0.2 | jtg_global   | fusion      |           0.6211 |   0.1662 |    1.0783 |                       9 |             15 |
| early_life        |       0.4 | jtg_global   | fusion      |           1.0851 |   0.6122 |    1.6221 |                      13 |             15 |
| early_life        |       0.6 | jtg_global   | fusion      |           1.2028 |   0.7088 |    1.7739 |                      14 |             15 |
| horizon           |       1   | jtg_global   | fusion      |           1.0692 |   0.7137 |    1.4614 |                      15 |             15 |
| horizon           |       3   | jtg_global   | fusion      |           1.026  |   0.6575 |    1.4058 |                      15 |             15 |
| horizon           |       6   | jtg_global   | fusion      |           0.9663 |   0.5972 |    1.3594 |                      15 |             15 |
| horizon           |      12   | jtg_global   | fusion      |           0.9185 |   0.5403 |    1.3255 |                      14 |             15 |
| sparse_all        |       1   | jtg_global   | fusion      |           1.0692 |   0.7127 |    1.4637 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | fusion      |           1.0499 |   0.691  |    1.4408 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | fusion      |           1.0264 |   0.6704 |    1.414  |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | fusion      |           0.9784 |   0.6319 |    1.3658 |                      15 |             15 |
| sparse_unobserved |       2   | jtg_global   | fusion      |           1.0594 |   0.6912 |    1.4511 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | fusion      |           1.0444 |   0.6913 |    1.4503 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | fusion      |           0.9934 |   0.6367 |    1.3765 |                      15 |             15 |
| cold_start        |       0   | lstm         | fusion      |           3.7778 |   3.0638 |    4.4074 |                      15 |             15 |
| early_life        |       0.2 | lstm         | fusion      |           1.9426 |   1.3231 |    2.5702 |                      13 |             15 |
| early_life        |       0.4 | lstm         | fusion      |           0.5262 |   0.3292 |    0.7268 |                      14 |             15 |
| early_life        |       0.6 | lstm         | fusion      |           0.2207 |   0.0883 |    0.3241 |                      14 |             15 |
| horizon           |       1   | lstm         | fusion      |           0.0716 |   0.03   |    0.1191 |                      11 |             15 |
| horizon           |       3   | lstm         | fusion      |           0.0991 |   0.0426 |    0.1674 |                      13 |             15 |
| horizon           |       6   | lstm         | fusion      |           0.1156 |   0.0388 |    0.215  |                      12 |             15 |
| horizon           |      12   | lstm         | fusion      |           0.1756 |   0.0631 |    0.3384 |                      12 |             15 |
| sparse_all        |       1   | lstm         | fusion      |           0.0716 |   0.0301 |    0.1207 |                      11 |             15 |
| sparse_all        |       2   | lstm         | fusion      |           0.0699 |   0.0266 |    0.1223 |                      12 |             15 |
| sparse_all        |       4   | lstm         | fusion      |           0.0738 |   0.0335 |    0.1205 |                      13 |             15 |
| sparse_all        |       8   | lstm         | fusion      |           0.1064 |   0.0614 |    0.1493 |                      14 |             15 |
| sparse_unobserved |       2   | lstm         | fusion      |           0.0731 |   0.0337 |    0.1189 |                      13 |             15 |
| sparse_unobserved |       4   | lstm         | fusion      |           0.0826 |   0.0416 |    0.1289 |                      14 |             15 |
| sparse_unobserved |       8   | lstm         | fusion      |           0.1055 |   0.0619 |    0.1493 |                      14 |             15 |
| cold_start        |       0   | mssa         | fusion      |           0.1841 |   0.0633 |    0.3077 |                      11 |             15 |
| early_life        |       0.2 | mssa         | fusion      |           0.2285 |   0.1092 |    0.3508 |                      14 |             15 |
| early_life        |       0.4 | mssa         | fusion      |           0.1031 |   0.0692 |    0.1371 |                      14 |             15 |
| early_life        |       0.6 | mssa         | fusion      |           0.0953 |   0.0324 |    0.1551 |                      13 |             15 |
| horizon           |       1   | mssa         | fusion      |           0.0199 |  -0.0006 |    0.0335 |                      13 |             15 |
| horizon           |       3   | mssa         | fusion      |           0.0419 |   0.0243 |    0.0555 |                      13 |             15 |
| horizon           |       6   | mssa         | fusion      |           0.0554 |   0.0323 |    0.075  |                      13 |             15 |
| horizon           |      12   | mssa         | fusion      |           0.0808 |   0.0522 |    0.1072 |                      13 |             15 |
| sparse_all        |       1   | mssa         | fusion      |           0.0199 |   0.0005 |    0.0335 |                      13 |             15 |
| sparse_all        |       2   | mssa         | fusion      |           0.0322 |   0.0109 |    0.047  |                      13 |             15 |
| sparse_all        |       4   | mssa         | fusion      |           0.0511 |   0.0281 |    0.0693 |                      14 |             15 |
| sparse_all        |       8   | mssa         | fusion      |           0.0678 |   0.0402 |    0.0913 |                      14 |             15 |
| sparse_unobserved |       2   | mssa         | fusion      |           0.0198 |  -0.0035 |    0.0358 |                      13 |             15 |
| sparse_unobserved |       4   | mssa         | fusion      |           0.0476 |   0.0265 |    0.066  |                      14 |             15 |
| sparse_unobserved |       8   | mssa         | fusion      |           0.0646 |   0.0363 |    0.0888 |                      14 |             15 |
| cold_start        |       0   | mssa_ens     | fusion      |           0.0795 |  -0.0742 |    0.2282 |                       8 |             15 |
| early_life        |       0.2 | mssa_ens     | fusion      |           0.1564 |   0.0407 |    0.2709 |                      12 |             15 |
| early_life        |       0.4 | mssa_ens     | fusion      |           0.0905 |   0.0534 |    0.126  |                      12 |             15 |
| early_life        |       0.6 | mssa_ens     | fusion      |           0.0838 |   0.0221 |    0.1467 |                      12 |             15 |
| horizon           |       1   | mssa_ens     | fusion      |           0.0177 |  -0.0023 |    0.0311 |                      13 |             15 |
| horizon           |       3   | mssa_ens     | fusion      |           0.037  |   0.0193 |    0.0506 |                      13 |             15 |
| horizon           |       6   | mssa_ens     | fusion      |           0.0471 |   0.0236 |    0.0667 |                      13 |             15 |
| horizon           |      12   | mssa_ens     | fusion      |           0.0687 |   0.0397 |    0.0938 |                      13 |             15 |
| sparse_all        |       1   | mssa_ens     | fusion      |           0.0177 |  -0.0023 |    0.0312 |                      13 |             15 |
| sparse_all        |       2   | mssa_ens     | fusion      |           0.0284 |   0.0065 |    0.0431 |                      13 |             15 |
| sparse_all        |       4   | mssa_ens     | fusion      |           0.0447 |   0.0223 |    0.0631 |                      14 |             15 |
| sparse_all        |       8   | mssa_ens     | fusion      |           0.057  |   0.0283 |    0.0812 |                      14 |             15 |
| sparse_unobserved |       2   | mssa_ens     | fusion      |           0.0166 |  -0.0067 |    0.0328 |                      13 |             15 |
| sparse_unobserved |       4   | mssa_ens     | fusion      |           0.0416 |   0.0197 |    0.0601 |                      14 |             15 |
| sparse_unobserved |       8   | mssa_ens     | fusion      |           0.054  |   0.0259 |    0.0789 |                      14 |             15 |
| cold_start        |       0   | patchtst     | fusion      |           3.7835 |   3.0663 |    4.4252 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | fusion      |           1.9549 |   1.2997 |    2.6115 |                      13 |             15 |
| early_life        |       0.4 | patchtst     | fusion      |           0.5229 |   0.3258 |    0.7121 |                      14 |             15 |
| early_life        |       0.6 | patchtst     | fusion      |           0.2074 |   0.0783 |    0.3084 |                      14 |             15 |
| horizon           |       1   | patchtst     | fusion      |           0.0545 |   0.0153 |    0.0981 |                      12 |             15 |
| horizon           |       3   | patchtst     | fusion      |           0.0911 |   0.0313 |    0.1604 |                      11 |             15 |
| horizon           |       6   | patchtst     | fusion      |           0.1178 |   0.0369 |    0.2186 |                       9 |             15 |
| horizon           |      12   | patchtst     | fusion      |           0.1707 |   0.0602 |    0.3151 |                      14 |             15 |
| sparse_all        |       1   | patchtst     | fusion      |           0.0545 |   0.0155 |    0.098  |                      12 |             15 |
| sparse_all        |       2   | patchtst     | fusion      |           0.0575 |   0.0174 |    0.1038 |                      11 |             15 |
| sparse_all        |       4   | patchtst     | fusion      |           0.0729 |   0.0306 |    0.117  |                      13 |             15 |
| sparse_all        |       8   | patchtst     | fusion      |           0.1192 |   0.0652 |    0.1653 |                      14 |             15 |
| sparse_unobserved |       2   | patchtst     | fusion      |           0.0562 |   0.0186 |    0.0981 |                      12 |             15 |
| sparse_unobserved |       4   | patchtst     | fusion      |           0.0776 |   0.0353 |    0.1222 |                      13 |             15 |
| sparse_unobserved |       8   | patchtst     | fusion      |           0.1157 |   0.066  |    0.1585 |                      14 |             15 |
| cold_start        |       0   | persistence  | fusion      |           3.9921 |   3.2715 |    4.6382 |                      15 |             15 |
| early_life        |       0.2 | persistence  | fusion      |           2.1269 |   1.4653 |    2.7851 |                      13 |             15 |
| early_life        |       0.4 | persistence  | fusion      |           0.5986 |   0.3943 |    0.7924 |                      14 |             15 |
| early_life        |       0.6 | persistence  | fusion      |           0.2449 |   0.094  |    0.3705 |                      13 |             15 |
| horizon           |       1   | persistence  | fusion      |           0.078  |   0.0458 |    0.1031 |                      14 |             15 |
| horizon           |       3   | persistence  | fusion      |           0.164  |   0.1239 |    0.1993 |                      14 |             15 |
| horizon           |       6   | persistence  | fusion      |           0.3241 |   0.2456 |    0.3901 |                      14 |             15 |
| horizon           |      12   | persistence  | fusion      |           0.6147 |   0.4983 |    0.7222 |                      15 |             15 |
| sparse_all        |       1   | persistence  | fusion      |           0.078  |   0.0462 |    0.1032 |                      14 |             15 |
| sparse_all        |       2   | persistence  | fusion      |           0.1006 |   0.0665 |    0.1311 |                      14 |             15 |
| sparse_all        |       4   | persistence  | fusion      |           0.1599 |   0.1104 |    0.2052 |                      13 |             15 |
| sparse_all        |       8   | persistence  | fusion      |           0.3226 |   0.2294 |    0.411  |                      14 |             15 |
| sparse_unobserved |       2   | persistence  | fusion      |           0.0817 |   0.0454 |    0.115  |                      14 |             15 |
| sparse_unobserved |       4   | persistence  | fusion      |           0.1426 |   0.0983 |    0.1874 |                      13 |             15 |
| sparse_unobserved |       8   | persistence  | fusion      |           0.3035 |   0.2153 |    0.3868 |                      14 |             15 |

### Paired structure-level RMSE difference (model - mssa_ens), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | fusion       | mssa_ens    |          -0.0795 |  -0.2311 |    0.0722 |                       7 |             15 |
| early_life        |       0.2 | fusion       | mssa_ens    |          -0.1564 |  -0.2705 |   -0.0414 |                       3 |             15 |
| early_life        |       0.4 | fusion       | mssa_ens    |          -0.0905 |  -0.126  |   -0.0538 |                       3 |             15 |
| early_life        |       0.6 | fusion       | mssa_ens    |          -0.0838 |  -0.1443 |   -0.0219 |                       3 |             15 |
| horizon           |       1   | fusion       | mssa_ens    |          -0.0177 |  -0.0313 |    0.0019 |                       2 |             15 |
| horizon           |       3   | fusion       | mssa_ens    |          -0.037  |  -0.0505 |   -0.0197 |                       2 |             15 |
| horizon           |       6   | fusion       | mssa_ens    |          -0.0471 |  -0.0665 |   -0.0239 |                       2 |             15 |
| horizon           |      12   | fusion       | mssa_ens    |          -0.0687 |  -0.0937 |   -0.0407 |                       2 |             15 |
| sparse_all        |       1   | fusion       | mssa_ens    |          -0.0177 |  -0.031  |    0.0022 |                       2 |             15 |
| sparse_all        |       2   | fusion       | mssa_ens    |          -0.0284 |  -0.043  |   -0.0071 |                       2 |             15 |
| sparse_all        |       4   | fusion       | mssa_ens    |          -0.0447 |  -0.0635 |   -0.0224 |                       1 |             15 |
| sparse_all        |       8   | fusion       | mssa_ens    |          -0.057  |  -0.0812 |   -0.0288 |                       1 |             15 |
| sparse_unobserved |       2   | fusion       | mssa_ens    |          -0.0166 |  -0.0329 |    0.0072 |                       2 |             15 |
| sparse_unobserved |       4   | fusion       | mssa_ens    |          -0.0416 |  -0.0603 |   -0.0203 |                       1 |             15 |
| sparse_unobserved |       8   | fusion       | mssa_ens    |          -0.054  |  -0.0793 |   -0.026  |                       1 |             15 |
| cold_start        |       0   | gbm_ens      | mssa_ens    |          -0.004  |  -0.3411 |    0.3391 |                       7 |             15 |
| early_life        |       0.2 | gbm_ens      | mssa_ens    |          -0.1237 |  -0.3352 |    0.1006 |                       7 |             15 |
| early_life        |       0.4 | gbm_ens      | mssa_ens    |          -0.0682 |  -0.1496 |    0.0152 |                       6 |             15 |
| early_life        |       0.6 | gbm_ens      | mssa_ens    |          -0.0578 |  -0.1899 |    0.0787 |                       5 |             15 |
| horizon           |       1   | gbm_ens      | mssa_ens    |           0.0068 |  -0.0253 |    0.0549 |                       4 |             15 |
| horizon           |       3   | gbm_ens      | mssa_ens    |          -0.0246 |  -0.0561 |    0.0166 |                       3 |             15 |
| horizon           |       6   | gbm_ens      | mssa_ens    |          -0.0361 |  -0.0762 |    0.014  |                       3 |             15 |
| horizon           |      12   | gbm_ens      | mssa_ens    |          -0.0508 |  -0.0984 |    0.0031 |                       4 |             15 |
| sparse_all        |       1   | gbm_ens      | mssa_ens    |           0.0068 |  -0.0253 |    0.0546 |                       4 |             15 |
| sparse_all        |       2   | gbm_ens      | mssa_ens    |          -0.0154 |  -0.0484 |    0.0332 |                       2 |             15 |
| sparse_all        |       4   | gbm_ens      | mssa_ens    |          -0.0424 |  -0.0789 |    0.0068 |                       2 |             15 |
| sparse_all        |       8   | gbm_ens      | mssa_ens    |          -0.0578 |  -0.0975 |   -0.0045 |                       2 |             15 |
| sparse_unobserved |       2   | gbm_ens      | mssa_ens    |           0.0058 |  -0.0285 |    0.057  |                       4 |             15 |
| sparse_unobserved |       4   | gbm_ens      | mssa_ens    |          -0.0365 |  -0.0729 |    0.0117 |                       2 |             15 |
| sparse_unobserved |       8   | gbm_ens      | mssa_ens    |          -0.0516 |  -0.0921 |    0.0004 |                       2 |             15 |
| cold_start        |       0   | gbm_residual | mssa_ens    |           0.0042 |  -0.3293 |    0.3329 |                       7 |             15 |
| early_life        |       0.2 | gbm_residual | mssa_ens    |          -0.1197 |  -0.3354 |    0.1065 |                       7 |             15 |
| early_life        |       0.4 | gbm_residual | mssa_ens    |          -0.0647 |  -0.1446 |    0.0175 |                       7 |             15 |
| early_life        |       0.6 | gbm_residual | mssa_ens    |          -0.0547 |  -0.1858 |    0.0783 |                       5 |             15 |
| horizon           |       1   | gbm_residual | mssa_ens    |           0.0091 |  -0.023  |    0.0582 |                       5 |             15 |
| horizon           |       3   | gbm_residual | mssa_ens    |          -0.0223 |  -0.0535 |    0.0204 |                       3 |             15 |
| horizon           |       6   | gbm_residual | mssa_ens    |          -0.0337 |  -0.0734 |    0.0152 |                       3 |             15 |
| horizon           |      12   | gbm_residual | mssa_ens    |          -0.0479 |  -0.0961 |    0.0052 |                       4 |             15 |
| sparse_all        |       1   | gbm_residual | mssa_ens    |           0.0091 |  -0.0229 |    0.0568 |                       5 |             15 |
| sparse_all        |       2   | gbm_residual | mssa_ens    |          -0.013  |  -0.0459 |    0.0371 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa_ens    |          -0.0397 |  -0.0764 |    0.0114 |                       2 |             15 |
| sparse_all        |       8   | gbm_residual | mssa_ens    |          -0.0551 |  -0.0958 |   -0.0016 |                       2 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa_ens    |           0.008  |  -0.0262 |    0.0604 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa_ens    |          -0.034  |  -0.0707 |    0.0143 |                       2 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa_ens    |          -0.049  |  -0.0896 |    0.0039 |                       2 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa_ens    |           0.1299 |  -0.3314 |    0.5262 |                      12 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa_ens    |           0.9419 |   0.4395 |    1.4416 |                      12 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa_ens    |           0.3189 |   0.1213 |    0.5066 |                      11 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa_ens    |           0.056  |  -0.0076 |    0.123  |                      11 |             15 |
| horizon           |       1   | jtg_enkf     | mssa_ens    |           0.0725 |   0.0608 |    0.0839 |                      15 |             15 |
| horizon           |       3   | jtg_enkf     | mssa_ens    |           0.0662 |   0.0511 |    0.0815 |                      15 |             15 |
| horizon           |       6   | jtg_enkf     | mssa_ens    |           0.0687 |   0.0451 |    0.0919 |                      14 |             15 |
| horizon           |      12   | jtg_enkf     | mssa_ens    |           0.1181 |   0.073  |    0.1664 |                      14 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa_ens    |           0.0725 |   0.0612 |    0.0838 |                      15 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa_ens    |           0.0498 |   0.0403 |    0.0603 |                      15 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa_ens    |           0.0324 |   0.0094 |    0.0539 |                      12 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa_ens    |           0.0409 |  -0.0013 |    0.0839 |                      11 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa_ens    |           0.0522 |   0.0417 |    0.0633 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa_ens    |           0.0388 |   0.0169 |    0.0606 |                      12 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa_ens    |           0.0434 |   0.0033 |    0.0853 |                      11 |             15 |
| cold_start        |       0   | jtg_global   | mssa_ens    |           0.1651 |  -0.2348 |    0.535  |                      10 |             15 |
| early_life        |       0.2 | jtg_global   | mssa_ens    |           0.4647 |   0.0236 |    0.9074 |                      10 |             15 |
| early_life        |       0.4 | jtg_global   | mssa_ens    |           0.9947 |   0.5187 |    1.5262 |                      12 |             15 |
| early_life        |       0.6 | jtg_global   | mssa_ens    |           1.1191 |   0.6338 |    1.6709 |                      14 |             15 |
| horizon           |       1   | jtg_global   | mssa_ens    |           1.0515 |   0.6837 |    1.4676 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa_ens    |           0.9891 |   0.615  |    1.3859 |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa_ens    |           0.9192 |   0.5465 |    1.3125 |                      14 |             15 |
| horizon           |      12   | jtg_global   | mssa_ens    |           0.8498 |   0.4617 |    1.2644 |                      12 |             15 |
| sparse_all        |       1   | jtg_global   | mssa_ens    |           1.0515 |   0.6815 |    1.4556 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa_ens    |           1.0215 |   0.6524 |    1.4208 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa_ens    |           0.9817 |   0.6147 |    1.3763 |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | mssa_ens    |           0.9214 |   0.5529 |    1.3159 |                      15 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa_ens    |           1.0428 |   0.6738 |    1.4545 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa_ens    |           1.0028 |   0.6317 |    1.4102 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa_ens    |           0.9395 |   0.5732 |    1.3443 |                      15 |             15 |
| cold_start        |       0   | lstm         | mssa_ens    |           3.6983 |   2.9522 |    4.3883 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa_ens    |           1.7862 |   1.1366 |    2.4268 |                      13 |             15 |
| early_life        |       0.4 | lstm         | mssa_ens    |           0.4358 |   0.2364 |    0.6491 |                      14 |             15 |
| early_life        |       0.6 | lstm         | mssa_ens    |           0.1369 |   0.009  |    0.2461 |                      13 |             15 |
| horizon           |       1   | lstm         | mssa_ens    |           0.0539 |   0.012  |    0.0998 |                      10 |             15 |
| horizon           |       3   | lstm         | mssa_ens    |           0.0621 |   0.005  |    0.1279 |                       8 |             15 |
| horizon           |       6   | lstm         | mssa_ens    |           0.0685 |  -0.0077 |    0.1641 |                       9 |             15 |
| horizon           |      12   | lstm         | mssa_ens    |           0.1069 |  -0.0049 |    0.2564 |                       9 |             15 |
| sparse_all        |       1   | lstm         | mssa_ens    |           0.0539 |   0.0126 |    0.0996 |                      10 |             15 |
| sparse_all        |       2   | lstm         | mssa_ens    |           0.0415 |  -0.0015 |    0.0879 |                       9 |             15 |
| sparse_all        |       4   | lstm         | mssa_ens    |           0.0291 |  -0.0093 |    0.0731 |                       8 |             15 |
| sparse_all        |       8   | lstm         | mssa_ens    |           0.0493 |   0.011  |    0.089  |                      11 |             15 |
| sparse_unobserved |       2   | lstm         | mssa_ens    |           0.0566 |   0.0159 |    0.1034 |                      11 |             15 |
| sparse_unobserved |       4   | lstm         | mssa_ens    |           0.041  |   0.0003 |    0.0857 |                      10 |             15 |
| sparse_unobserved |       8   | lstm         | mssa_ens    |           0.0516 |   0.0105 |    0.0937 |                      11 |             15 |
| cold_start        |       0   | mssa         | mssa_ens    |           0.1046 |   0.0502 |    0.1657 |                      15 |             15 |
| early_life        |       0.2 | mssa         | mssa_ens    |           0.0721 |   0.017  |    0.1446 |                      15 |             15 |
| early_life        |       0.4 | mssa         | mssa_ens    |           0.0126 |   0.0069 |    0.0197 |                      15 |             15 |
| early_life        |       0.6 | mssa         | mssa_ens    |           0.0116 |   0.0044 |    0.0203 |                      15 |             15 |
| horizon           |       1   | mssa         | mssa_ens    |           0.0022 |   0.0014 |    0.0031 |                      15 |             15 |
| horizon           |       3   | mssa         | mssa_ens    |           0.0049 |   0.0031 |    0.0069 |                      15 |             15 |
| horizon           |       6   | mssa         | mssa_ens    |           0.0083 |   0.0053 |    0.0118 |                      15 |             15 |
| horizon           |      12   | mssa         | mssa_ens    |           0.0121 |   0.0082 |    0.0164 |                      15 |             15 |
| sparse_all        |       1   | mssa         | mssa_ens    |           0.0022 |   0.0014 |    0.0031 |                      15 |             15 |
| sparse_all        |       2   | mssa         | mssa_ens    |           0.0038 |   0.0024 |    0.0054 |                      15 |             15 |
| sparse_all        |       4   | mssa         | mssa_ens    |           0.0064 |   0.0041 |    0.009  |                      15 |             15 |
| sparse_all        |       8   | mssa         | mssa_ens    |           0.0108 |   0.0072 |    0.015  |                      15 |             15 |
| sparse_unobserved |       2   | mssa         | mssa_ens    |           0.0033 |   0.0019 |    0.0049 |                      15 |             15 |
| sparse_unobserved |       4   | mssa         | mssa_ens    |           0.006  |   0.0038 |    0.0084 |                      15 |             15 |
| sparse_unobserved |       8   | mssa         | mssa_ens    |           0.0106 |   0.0071 |    0.0147 |                      15 |             15 |
| cold_start        |       0   | patchtst     | mssa_ens    |           3.7041 |   2.9271 |    4.4027 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa_ens    |           1.7985 |   1.1148 |    2.4864 |                      13 |             15 |
| early_life        |       0.4 | patchtst     | mssa_ens    |           0.4324 |   0.2315 |    0.6312 |                      14 |             15 |
| early_life        |       0.6 | patchtst     | mssa_ens    |           0.1236 |  -0.0104 |    0.2328 |                      13 |             15 |
| horizon           |       1   | patchtst     | mssa_ens    |           0.0369 |  -0.0016 |    0.0772 |                      10 |             15 |
| horizon           |       3   | patchtst     | mssa_ens    |           0.0541 |  -0.0027 |    0.1196 |                       9 |             15 |
| horizon           |       6   | patchtst     | mssa_ens    |           0.0708 |  -0.0076 |    0.1671 |                       9 |             15 |
| horizon           |      12   | patchtst     | mssa_ens    |           0.102  |  -0.0073 |    0.239  |                       9 |             15 |
| sparse_all        |       1   | patchtst     | mssa_ens    |           0.0369 |  -0.0011 |    0.078  |                      10 |             15 |
| sparse_all        |       2   | patchtst     | mssa_ens    |           0.0291 |  -0.008  |    0.0707 |                       9 |             15 |
| sparse_all        |       4   | patchtst     | mssa_ens    |           0.0282 |  -0.0088 |    0.0673 |                       9 |             15 |
| sparse_all        |       8   | patchtst     | mssa_ens    |           0.0621 |   0.0201 |    0.1038 |                      11 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa_ens    |           0.0396 |   0.0016 |    0.0789 |                      10 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa_ens    |           0.036  |  -0.0028 |    0.0759 |                      10 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa_ens    |           0.0617 |   0.021  |    0.101  |                      11 |             15 |
| cold_start        |       0   | persistence  | mssa_ens    |           3.9127 |   3.1494 |    4.6261 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa_ens    |           1.9705 |   1.2878 |    2.6489 |                      13 |             15 |
| early_life        |       0.4 | persistence  | mssa_ens    |           0.5081 |   0.2999 |    0.71   |                      14 |             15 |
| early_life        |       0.6 | persistence  | mssa_ens    |           0.1611 |   0.0072 |    0.2867 |                      13 |             15 |
| horizon           |       1   | persistence  | mssa_ens    |           0.0603 |   0.0445 |    0.0752 |                      15 |             15 |
| horizon           |       3   | persistence  | mssa_ens    |           0.127  |   0.0987 |    0.1546 |                      15 |             15 |
| horizon           |       6   | persistence  | mssa_ens    |           0.277  |   0.2124 |    0.335  |                      15 |             15 |
| horizon           |      12   | persistence  | mssa_ens    |           0.5461 |   0.4434 |    0.6424 |                      15 |             15 |
| sparse_all        |       1   | persistence  | mssa_ens    |           0.0603 |   0.0446 |    0.0755 |                      15 |             15 |
| sparse_all        |       2   | persistence  | mssa_ens    |           0.0722 |   0.0498 |    0.0943 |                      14 |             15 |
| sparse_all        |       4   | persistence  | mssa_ens    |           0.1152 |   0.0697 |    0.158  |                      14 |             15 |
| sparse_all        |       8   | persistence  | mssa_ens    |           0.2656 |   0.1813 |    0.3509 |                      14 |             15 |
| sparse_unobserved |       2   | persistence  | mssa_ens    |           0.0651 |   0.0405 |    0.0902 |                      13 |             15 |
| sparse_unobserved |       4   | persistence  | mssa_ens    |           0.1009 |   0.0552 |    0.1457 |                      14 |             15 |
| sparse_unobserved |       8   | persistence  | mssa_ens    |           0.2495 |   0.1663 |    0.3311 |                      14 |             15 |

### Paired structure-level RMSE difference (model - mssa), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | fusion       | mssa        |          -0.1841 |  -0.3083 |   -0.0608 |                       4 |             15 |
| early_life        |       0.2 | fusion       | mssa        |          -0.2285 |  -0.3498 |   -0.111  |                       1 |             15 |
| early_life        |       0.4 | fusion       | mssa        |          -0.1031 |  -0.1361 |   -0.0692 |                       1 |             15 |
| early_life        |       0.6 | fusion       | mssa        |          -0.0953 |  -0.1537 |   -0.0344 |                       2 |             15 |
| horizon           |       1   | fusion       | mssa        |          -0.0199 |  -0.0336 |   -0.0002 |                       2 |             15 |
| horizon           |       3   | fusion       | mssa        |          -0.0419 |  -0.0556 |   -0.0248 |                       2 |             15 |
| horizon           |       6   | fusion       | mssa        |          -0.0554 |  -0.0751 |   -0.0325 |                       2 |             15 |
| horizon           |      12   | fusion       | mssa        |          -0.0808 |  -0.1071 |   -0.0522 |                       2 |             15 |
| sparse_all        |       1   | fusion       | mssa        |          -0.0199 |  -0.0334 |    0      |                       2 |             15 |
| sparse_all        |       2   | fusion       | mssa        |          -0.0322 |  -0.0472 |   -0.0108 |                       2 |             15 |
| sparse_all        |       4   | fusion       | mssa        |          -0.0511 |  -0.0697 |   -0.0287 |                       1 |             15 |
| sparse_all        |       8   | fusion       | mssa        |          -0.0678 |  -0.0915 |   -0.0397 |                       1 |             15 |
| sparse_unobserved |       2   | fusion       | mssa        |          -0.0198 |  -0.036  |    0.0039 |                       2 |             15 |
| sparse_unobserved |       4   | fusion       | mssa        |          -0.0476 |  -0.0658 |   -0.0266 |                       1 |             15 |
| sparse_unobserved |       8   | fusion       | mssa        |          -0.0646 |  -0.089  |   -0.0369 |                       1 |             15 |
| cold_start        |       0   | gbm_ens      | mssa        |          -0.1086 |  -0.4101 |    0.2003 |                       7 |             15 |
| early_life        |       0.2 | gbm_ens      | mssa        |          -0.1959 |  -0.3821 |    0.0083 |                       5 |             15 |
| early_life        |       0.4 | gbm_ens      | mssa        |          -0.0808 |  -0.1594 |   -0      |                       6 |             15 |
| early_life        |       0.6 | gbm_ens      | mssa        |          -0.0693 |  -0.1992 |    0.0658 |                       5 |             15 |
| horizon           |       1   | gbm_ens      | mssa        |           0.0045 |  -0.0276 |    0.0527 |                       4 |             15 |
| horizon           |       3   | gbm_ens      | mssa        |          -0.0296 |  -0.0615 |    0.0117 |                       3 |             15 |
| horizon           |       6   | gbm_ens      | mssa        |          -0.0444 |  -0.0844 |    0.0057 |                       2 |             15 |
| horizon           |      12   | gbm_ens      | mssa        |          -0.0628 |  -0.1113 |   -0.0088 |                       4 |             15 |
| sparse_all        |       1   | gbm_ens      | mssa        |           0.0045 |  -0.0277 |    0.0523 |                       4 |             15 |
| sparse_all        |       2   | gbm_ens      | mssa        |          -0.0193 |  -0.0524 |    0.0294 |                       2 |             15 |
| sparse_all        |       4   | gbm_ens      | mssa        |          -0.0488 |  -0.0855 |    0.0002 |                       2 |             15 |
| sparse_all        |       8   | gbm_ens      | mssa        |          -0.0686 |  -0.1082 |   -0.0156 |                       2 |             15 |
| sparse_unobserved |       2   | gbm_ens      | mssa        |           0.0025 |  -0.0315 |    0.0539 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_ens      | mssa        |          -0.0425 |  -0.0785 |    0.0056 |                       2 |             15 |
| sparse_unobserved |       8   | gbm_ens      | mssa        |          -0.0622 |  -0.1024 |   -0.0111 |                       2 |             15 |
| cold_start        |       0   | gbm_residual | mssa        |          -0.1004 |  -0.3992 |    0.1938 |                       7 |             15 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.1918 |  -0.3798 |    0.0098 |                       5 |             15 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.0773 |  -0.1544 |    0.0024 |                       6 |             15 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.0663 |  -0.1939 |    0.0655 |                       5 |             15 |
| horizon           |       1   | gbm_residual | mssa        |           0.0069 |  -0.0252 |    0.056  |                       4 |             15 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0272 |  -0.0587 |    0.0152 |                       3 |             15 |
| horizon           |       6   | gbm_residual | mssa        |          -0.042  |  -0.0817 |    0.0072 |                       3 |             15 |
| horizon           |      12   | gbm_residual | mssa        |          -0.06   |  -0.1097 |   -0.0063 |                       4 |             15 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0069 |  -0.0253 |    0.0545 |                       4 |             15 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0169 |  -0.05   |    0.0335 |                       2 |             15 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.0462 |  -0.083  |    0.0047 |                       2 |             15 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.0659 |  -0.1064 |   -0.0123 |                       2 |             15 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0048 |  -0.0293 |    0.0571 |                       4 |             15 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.04   |  -0.0765 |    0.0079 |                       2 |             15 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.0596 |  -0.0996 |   -0.0069 |                       2 |             15 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.0253 |  -0.4194 |    0.4184 |                       9 |             15 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           0.8697 |   0.3907 |    1.3456 |                      12 |             15 |
| early_life        |       0.4 | jtg_enkf     | mssa        |           0.3063 |   0.1122 |    0.4915 |                      11 |             15 |
| early_life        |       0.6 | jtg_enkf     | mssa        |           0.0444 |  -0.0189 |    0.1115 |                      10 |             15 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0703 |   0.0588 |    0.0815 |                      15 |             15 |
| horizon           |       3   | jtg_enkf     | mssa        |           0.0613 |   0.0469 |    0.0759 |                      15 |             15 |
| horizon           |       6   | jtg_enkf     | mssa        |           0.0604 |   0.0379 |    0.0819 |                      14 |             15 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.1061 |   0.0631 |    0.1519 |                      14 |             15 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0703 |   0.059  |    0.0815 |                      15 |             15 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.046  |   0.0366 |    0.0562 |                      15 |             15 |
| sparse_all        |       4   | jtg_enkf     | mssa        |           0.0259 |   0.0042 |    0.0468 |                      12 |             15 |
| sparse_all        |       8   | jtg_enkf     | mssa        |           0.0301 |  -0.0106 |    0.0716 |                      10 |             15 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0489 |   0.0383 |    0.0603 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |           0.0328 |   0.0116 |    0.0541 |                      12 |             15 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |           0.0329 |  -0.0064 |    0.0736 |                      10 |             15 |
| cold_start        |       0   | jtg_global   | mssa        |           0.0604 |  -0.3081 |    0.4015 |                       9 |             15 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.3926 |  -0.0207 |    0.8108 |                       9 |             15 |
| early_life        |       0.4 | jtg_global   | mssa        |           0.982  |   0.5083 |    1.5101 |                      12 |             15 |
| early_life        |       0.6 | jtg_global   | mssa        |           1.1075 |   0.6187 |    1.6593 |                      14 |             15 |
| horizon           |       1   | jtg_global   | mssa        |           1.0493 |   0.6818 |    1.4652 |                      15 |             15 |
| horizon           |       3   | jtg_global   | mssa        |           0.9841 |   0.6093 |    1.3814 |                      15 |             15 |
| horizon           |       6   | jtg_global   | mssa        |           0.9108 |   0.5382 |    1.3037 |                      14 |             15 |
| horizon           |      12   | jtg_global   | mssa        |           0.8377 |   0.4504 |    1.2542 |                      12 |             15 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.0493 |   0.6794 |    1.4533 |                      15 |             15 |
| sparse_all        |       2   | jtg_global   | mssa        |           1.0177 |   0.6489 |    1.4173 |                      15 |             15 |
| sparse_all        |       4   | jtg_global   | mssa        |           0.9753 |   0.6067 |    1.3699 |                      15 |             15 |
| sparse_all        |       8   | jtg_global   | mssa        |           0.9106 |   0.5419 |    1.306  |                      15 |             15 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           1.0395 |   0.6701 |    1.4509 |                      15 |             15 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           0.9968 |   0.6249 |    1.4039 |                      15 |             15 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           0.9289 |   0.5635 |    1.3351 |                      15 |             15 |
| cold_start        |       0   | lstm         | mssa        |           3.5937 |   2.873  |    4.2547 |                      15 |             15 |
| early_life        |       0.2 | lstm         | mssa        |           1.714  |   1.0965 |    2.308  |                      13 |             15 |
| early_life        |       0.4 | lstm         | mssa        |           0.4231 |   0.2265 |    0.6336 |                      14 |             15 |
| early_life        |       0.6 | lstm         | mssa        |           0.1253 |  -0.0013 |    0.2285 |                      13 |             15 |
| horizon           |       1   | lstm         | mssa        |           0.0517 |   0.01   |    0.0971 |                      10 |             15 |
| horizon           |       3   | lstm         | mssa        |           0.0572 |   0.0009 |    0.1221 |                       8 |             15 |
| horizon           |       6   | lstm         | mssa        |           0.0602 |  -0.0156 |    0.1544 |                       9 |             15 |
| horizon           |      12   | lstm         | mssa        |           0.0949 |  -0.0168 |    0.2427 |                       8 |             15 |
| sparse_all        |       1   | lstm         | mssa        |           0.0517 |   0.0106 |    0.0971 |                      10 |             15 |
| sparse_all        |       2   | lstm         | mssa        |           0.0376 |  -0.0049 |    0.0835 |                       8 |             15 |
| sparse_all        |       4   | lstm         | mssa        |           0.0227 |  -0.0149 |    0.0655 |                       8 |             15 |
| sparse_all        |       8   | lstm         | mssa        |           0.0386 |   0.0008 |    0.0781 |                      11 |             15 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0533 |   0.0132 |    0.0995 |                      10 |             15 |
| sparse_unobserved |       4   | lstm         | mssa        |           0.035  |  -0.0047 |    0.0787 |                       9 |             15 |
| sparse_unobserved |       8   | lstm         | mssa        |           0.041  |   0.0011 |    0.0825 |                      11 |             15 |
| cold_start        |       0   | mssa_ens     | mssa        |          -0.1046 |  -0.1657 |   -0.0502 |                       0 |             15 |
| early_life        |       0.2 | mssa_ens     | mssa        |          -0.0721 |  -0.1446 |   -0.017  |                       0 |             15 |
| early_life        |       0.4 | mssa_ens     | mssa        |          -0.0126 |  -0.0197 |   -0.0069 |                       0 |             15 |
| early_life        |       0.6 | mssa_ens     | mssa        |          -0.0116 |  -0.0203 |   -0.0044 |                       0 |             15 |
| horizon           |       1   | mssa_ens     | mssa        |          -0.0022 |  -0.0031 |   -0.0014 |                       0 |             15 |
| horizon           |       3   | mssa_ens     | mssa        |          -0.0049 |  -0.0069 |   -0.0031 |                       0 |             15 |
| horizon           |       6   | mssa_ens     | mssa        |          -0.0083 |  -0.0118 |   -0.0053 |                       0 |             15 |
| horizon           |      12   | mssa_ens     | mssa        |          -0.0121 |  -0.0164 |   -0.0082 |                       0 |             15 |
| sparse_all        |       1   | mssa_ens     | mssa        |          -0.0022 |  -0.0031 |   -0.0014 |                       0 |             15 |
| sparse_all        |       2   | mssa_ens     | mssa        |          -0.0038 |  -0.0054 |   -0.0024 |                       0 |             15 |
| sparse_all        |       4   | mssa_ens     | mssa        |          -0.0064 |  -0.009  |   -0.0041 |                       0 |             15 |
| sparse_all        |       8   | mssa_ens     | mssa        |          -0.0108 |  -0.015  |   -0.0072 |                       0 |             15 |
| sparse_unobserved |       2   | mssa_ens     | mssa        |          -0.0033 |  -0.0049 |   -0.0019 |                       0 |             15 |
| sparse_unobserved |       4   | mssa_ens     | mssa        |          -0.006  |  -0.0084 |   -0.0038 |                       0 |             15 |
| sparse_unobserved |       8   | mssa_ens     | mssa        |          -0.0106 |  -0.0147 |   -0.0071 |                       0 |             15 |
| cold_start        |       0   | patchtst     | mssa        |           3.5994 |   2.8564 |    4.2743 |                      15 |             15 |
| early_life        |       0.2 | patchtst     | mssa        |           1.7264 |   1.0816 |    2.3672 |                      13 |             15 |
| early_life        |       0.4 | patchtst     | mssa        |           0.4198 |   0.2206 |    0.6171 |                      14 |             15 |
| early_life        |       0.6 | patchtst     | mssa        |           0.1121 |  -0.0185 |    0.2171 |                      13 |             15 |
| horizon           |       1   | patchtst     | mssa        |           0.0346 |  -0.0035 |    0.0748 |                      10 |             15 |
| horizon           |       3   | patchtst     | mssa        |           0.0492 |  -0.0067 |    0.1139 |                       9 |             15 |
| horizon           |       6   | patchtst     | mssa        |           0.0624 |  -0.0155 |    0.157  |                       8 |             15 |
| horizon           |      12   | patchtst     | mssa        |           0.0899 |  -0.0187 |    0.2254 |                       9 |             15 |
| sparse_all        |       1   | patchtst     | mssa        |           0.0346 |  -0.003  |    0.0753 |                      10 |             15 |
| sparse_all        |       2   | patchtst     | mssa        |           0.0253 |  -0.0115 |    0.0666 |                       9 |             15 |
| sparse_all        |       4   | patchtst     | mssa        |           0.0218 |  -0.0146 |    0.0597 |                       8 |             15 |
| sparse_all        |       8   | patchtst     | mssa        |           0.0513 |   0.0099 |    0.0921 |                      11 |             15 |
| sparse_unobserved |       2   | patchtst     | mssa        |           0.0363 |  -0.0014 |    0.0752 |                       9 |             15 |
| sparse_unobserved |       4   | patchtst     | mssa        |           0.03   |  -0.0077 |    0.0689 |                      10 |             15 |
| sparse_unobserved |       8   | patchtst     | mssa        |           0.0511 |   0.0114 |    0.0895 |                      11 |             15 |
| cold_start        |       0   | persistence  | mssa        |           3.808  |   3.0711 |    4.4952 |                      15 |             15 |
| early_life        |       0.2 | persistence  | mssa        |           1.8984 |   1.2494 |    2.5421 |                      13 |             15 |
| early_life        |       0.4 | persistence  | mssa        |           0.4955 |   0.2893 |    0.6956 |                      14 |             15 |
| early_life        |       0.6 | persistence  | mssa        |           0.1495 |  -0.0011 |    0.2704 |                      13 |             15 |
| horizon           |       1   | persistence  | mssa        |           0.0581 |   0.0422 |    0.0731 |                      14 |             15 |
| horizon           |       3   | persistence  | mssa        |           0.1221 |   0.0937 |    0.1496 |                      14 |             15 |
| horizon           |       6   | persistence  | mssa        |           0.2687 |   0.2048 |    0.3258 |                      14 |             15 |
| horizon           |      12   | persistence  | mssa        |           0.534  |   0.433  |    0.6288 |                      15 |             15 |
| sparse_all        |       1   | persistence  | mssa        |           0.0581 |   0.0423 |    0.0732 |                      14 |             15 |
| sparse_all        |       2   | persistence  | mssa        |           0.0684 |   0.0458 |    0.0907 |                      14 |             15 |
| sparse_all        |       4   | persistence  | mssa        |           0.1088 |   0.0634 |    0.1517 |                      14 |             15 |
| sparse_all        |       8   | persistence  | mssa        |           0.2548 |   0.1713 |    0.3402 |                      14 |             15 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0619 |   0.0373 |    0.0868 |                      13 |             15 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.095  |   0.0493 |    0.1397 |                      14 |             15 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.2389 |   0.1564 |    0.32   |                      14 |             15 |

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         0 |      1.5519 |   nan      |     1.181  |      0.7741 |      3.9314 |      0.8661 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         0 |      1.8226 |   nan      |     1.41   |      0.3483 |      1.3926 |      1.241  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         0 |      1.8295 |     0.0398 |     1.4137 |      0.3168 |      1.2445 |      1.2623 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |     0      |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      4.9347 |     0.0387 |     4.3507 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.4591 |     0.1365 |     1.1239 |      0.8766 |      4.4503 |      0.7978 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         0 |      1.3971 |   nan      |     1.0784 |      0.9223 |      4.7692 |      0.7596 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      4.9462 |     0.0313 |     4.3609 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |     0      |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |       0.2 |      1.0572 |   nan      |     0.8408 |      0.8381 |      3.3266 |      0.603  |             0.9309 |                0.0568 |                        nan |           13.396  |            17.66   |
| fusion       |       0.4 |      0.5786 |   nan      |     0.4557 |      0.9595 |      2.5873 |      0.3284 |             0.5789 |                0.0715 |                        nan |            2.0975 |             7.9767 |
| fusion       |       0.6 |      0.5339 |   nan      |     0.4112 |      0.8969 |      2.0153 |      0.3016 |             0.4372 |                0.0487 |                        nan |            2.34   |             8.835  |
| gbm_ens      |       0.2 |      1.3067 |   nan      |     1.0199 |      0.4213 |      1.2929 |      0.8711 |             1.1496 |                0.1185 |                        nan |            9.3171 |           nan      |
| gbm_ens      |       0.4 |      0.6714 |   nan      |     0.5352 |      0.6677 |      1.2675 |      0.4109 |             0.7058 |                0.1428 |                        nan |            1.77   |            13.1633 |
| gbm_ens      |       0.6 |      0.5937 |   nan      |     0.4725 |      0.717  |      1.2619 |      0.3588 |             0.5577 |                0.1387 |                        nan |            1.56   |             8.065  |
| gbm_residual |       0.2 |      1.3097 |     0.0098 |     1.0231 |      0.4088 |      1.2445 |      0.8781 |             1.1539 |                0.125  |                        nan |           10.1256 |           nan      |
| gbm_residual |       0.4 |      0.6741 |     0.0143 |     0.5367 |      0.6523 |      1.2445 |      0.4142 |             0.708  |                0.1505 |                        nan |            3.8235 |            12.954  |
| gbm_residual |       0.6 |      0.596  |     0.013  |     0.4751 |      0.7051 |      1.2445 |      0.3613 |             0.5622 |                0.1444 |                        nan |            1.008  |             7.714  |
| jtg_enkf     |       0.2 |      2.7621 |     0      |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |     0      |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |     0      |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| lstm         |       0.2 |      2.8272 |     0.0183 |     2.3005 |    nan      |    nan      |    nan      |             3.6215 |                0.2973 |                        nan |            1.4    |           nan      |
| lstm         |       0.4 |      1.0046 |     0.0121 |     0.7854 |    nan      |    nan      |    nan      |             1.389  |                0.2496 |                        nan |            7.9413 |             0.3725 |
| lstm         |       0.6 |      0.7552 |     0.0202 |     0.5811 |    nan      |    nan      |    nan      |             0.8278 |                0.2203 |                        nan |            2.62   |             8.4783 |
| mssa         |       0.2 |      0.9796 |     0.0241 |     0.79   |      0.9117 |      3.8043 |      0.5614 |             0.9362 |                0      |                          0 |            8.147  |            12.5872 |
| mssa         |       0.4 |      0.6628 |     0.042  |     0.5257 |      0.9704 |      2.9449 |      0.3719 |             0.6639 |                0      |                          0 |            2.68   |             7.5381 |
| mssa         |       0.6 |      0.5758 |     0.0093 |     0.4547 |      0.9463 |      2.2173 |      0.3239 |             0.4398 |                0      |                          0 |            3.5    |            14.786  |
| mssa_ens     |       0.2 |      0.9508 |   nan      |     0.7674 |      0.9288 |      3.9041 |      0.5478 |             0.8878 |                0      |                        nan |            7.353  |            12.62   |
| mssa_ens     |       0.4 |      0.6544 |   nan      |     0.5226 |      0.9758 |      2.9759 |      0.3675 |             0.6633 |                0      |                        nan |            1.925  |             7.816  |
| mssa_ens     |       0.6 |      0.5751 |   nan      |     0.4541 |      0.9512 |      2.2221 |      0.3232 |             0.4398 |                0      |                        nan |          nan      |            14.57   |
| patchtst     |       0.2 |      2.847  |     0.0164 |     2.3228 |    nan      |    nan      |    nan      |             3.6168 |                0.3207 |                        nan |          nan      |           nan      |
| patchtst     |       0.4 |      1.0042 |     0.0222 |     0.7937 |    nan      |    nan      |    nan      |             1.3821 |                0.2814 |                        nan |            8.2017 |           nan      |
| patchtst     |       0.6 |      0.7422 |     0.014  |     0.5752 |    nan      |    nan      |    nan      |             0.7949 |                0.2474 |                        nan |            3.875  |            10.21   |
| persistence  |       0.2 |      2.9861 |     0      |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |     0      |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |     0      |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         1 |      0.3463 |   nan      |     0.2488 |      0.9506 |      1.4124 |      0.1841 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         3 |      0.4013 |   nan      |     0.2936 |      0.9395 |      1.5614 |      0.2157 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         6 |      0.4806 |   nan      |     0.3573 |      0.9284 |      1.7243 |      0.2597 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |        12 |      0.5593 |   nan      |     0.4209 |      0.9255 |      1.966  |      0.3044 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         1 |      0.4135 |   nan      |     0.3047 |      0.891  |      1.2587 |      0.224  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         3 |      0.4566 |   nan      |     0.3358 |      0.8542 |      1.2597 |      0.2494 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         6 |      0.541  |   nan      |     0.4011 |      0.8037 |      1.2619 |      0.3015 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |        12 |      0.6448 |   nan      |     0.4859 |      0.7311 |      1.2662 |      0.3738 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         1 |      0.4162 |     0.0082 |     0.3066 |      0.8845 |      1.2445 |      0.226  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4592 |     0.0105 |     0.338  |      0.8484 |      1.2445 |      0.2516 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5436 |     0.0103 |     0.403  |      0.7971 |      1.2445 |      0.304  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6475 |     0.0112 |     0.4878 |      0.7213 |      1.2445 |      0.3769 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |     0      |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |     0      |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |     0      |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |     0      |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4121 |     0.025  |     0.2983 |      0.7998 |      0.9247 |      0.2264 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4956 |     0.0335 |     0.3613 |      0.7257 |      0.9247 |      0.2813 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.6039 |     0.0735 |     0.4424 |      0.6503 |      0.9247 |      0.3542 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.7725 |     0.106  |     0.5834 |      0.521  |      0.9247 |      0.4836 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3479 |     0.0017 |     0.2442 |      0.9297 |      1.3006 |      0.1836 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4203 |     0.0022 |     0.3122 |      0.9307 |      1.5516 |      0.2277 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.5047 |     0.0029 |     0.3851 |      0.924  |      1.7731 |      0.277  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.5946 |     0.0045 |     0.4564 |      0.9227 |      2.032  |      0.3267 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         1 |      0.347  |   nan      |     0.2436 |      0.9316 |      1.3048 |      0.183  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         3 |      0.4186 |   nan      |     0.3111 |      0.9336 |      1.5591 |      0.2266 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         6 |      0.5019 |   nan      |     0.3833 |      0.9299 |      1.7856 |      0.2752 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |        12 |      0.59   |   nan      |     0.4536 |      0.9279 |      2.0529 |      0.3238 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3846 |     0.0109 |     0.2807 |      0.8067 |      0.895  |      0.2117 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4803 |     0.0275 |     0.3535 |      0.7173 |      0.895  |      0.2749 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.5739 |     0.0132 |     0.4238 |      0.644  |      0.895  |      0.3381 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.6938 |     0.023  |     0.5165 |      0.5601 |      0.895  |      0.4235 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |     0      |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |     0      |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |     0      |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |     0      |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         1 |      0.3463 |   nan      |     0.2488 |      0.9506 |      1.4124 |      0.1841 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         2 |      0.37   |   nan      |     0.2672 |      0.9444 |      1.4645 |      0.1971 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         4 |      0.3999 |   nan      |     0.2939 |      0.9411 |      1.5468 |      0.2145 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         8 |      0.4716 |   nan      |     0.3469 |      0.9283 |      1.6764 |      0.2529 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         1 |      0.4135 |   nan      |     0.3047 |      0.891  |      1.2587 |      0.224  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         2 |      0.425  |   nan      |     0.3108 |      0.8822 |      1.2588 |      0.2297 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         4 |      0.4471 |   nan      |     0.3275 |      0.8691 |      1.2596 |      0.2422 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         8 |      0.5145 |   nan      |     0.3767 |      0.8372 |      1.2618 |      0.2818 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         1 |      0.4162 |     0.0082 |     0.3066 |      0.8845 |      1.2445 |      0.226  |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4277 |     0.0086 |     0.3127 |      0.8782 |      1.2445 |      0.2317 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4497 |     0.0094 |     0.3292 |      0.8627 |      1.2445 |      0.2443 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5172 |     0.008  |     0.3788 |      0.8287 |      1.2445 |      0.2842 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |     0      |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |     0      |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |     0      |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |     0      |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.4121 |     0.025  |     0.2983 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4334 |     0.0216 |     0.3132 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4606 |     0.0235 |     0.3355 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.541  |     0.0206 |     0.3878 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3479 |     0.0017 |     0.2442 |      0.9297 |      1.3006 |      0.1836 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3839 |     0.0026 |     0.2767 |      0.9222 |      1.3962 |      0.205  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4268 |     0.0032 |     0.3166 |      0.9203 |      1.5268 |      0.231  |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.5099 |     0.0066 |     0.3844 |      0.9124 |      1.707  |      0.2779 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         1 |      0.347  |   nan      |     0.2436 |      0.9316 |      1.3048 |      0.183  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         2 |      0.3824 |   nan      |     0.2757 |      0.9276 |      1.4031 |      0.204  |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         4 |      0.4246 |   nan      |     0.3151 |      0.9261 |      1.5366 |      0.2296 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         8 |      0.5061 |   nan      |     0.3819 |      0.9206 |      1.7243 |      0.2754 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3846 |     0.0109 |     0.2807 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4116 |     0.015  |     0.2993 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4515 |     0.0093 |     0.328  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5612 |     0.0117 |     0.3943 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |     0      |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |     0      |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |     0      |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |     0      |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| fusion       |         2 |      0.3589 |   nan      |     0.2607 |      0.9453 |      1.4253 |      0.192  |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         4 |      0.383  |   nan      |     0.2825 |      0.9455 |      1.5147 |      0.2063 |                nan |                   nan |                        nan |               nan |                nan |
| fusion       |         8 |      0.4567 |   nan      |     0.3369 |      0.9319 |      1.6521 |      0.2452 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         2 |      0.4208 |   nan      |     0.3092 |      0.8891 |      1.2585 |      0.2279 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         4 |      0.4306 |   nan      |     0.3173 |      0.8788 |      1.2591 |      0.2337 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_ens      |         8 |      0.4987 |   nan      |     0.3651 |      0.848  |      1.2611 |      0.2719 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4235 |     0.0081 |     0.3112 |      0.8843 |      1.2445 |      0.2299 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4333 |     0.0094 |     0.3192 |      0.873  |      1.2445 |      0.2358 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5014 |     0.0082 |     0.367  |      0.8394 |      1.2445 |      0.2743 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |     0      |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |     0      |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |     0      |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4275 |     0.0195 |     0.3116 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4527 |     0.0246 |     0.331  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.5264 |     0.0203 |     0.3804 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3643 |     0.0024 |     0.262  |      0.9192 |      1.3276 |      0.1954 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.409  |     0.0039 |     0.3027 |      0.9228 |      1.4768 |      0.2213 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.4949 |     0.0066 |     0.3741 |      0.9133 |      1.6741 |      0.2703 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         2 |      0.3629 |   nan      |     0.2611 |      0.9241 |      1.3337 |      0.1945 |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         4 |      0.4069 |   nan      |     0.3015 |      0.9284 |      1.4859 |      0.22   |                nan |                   nan |                        nan |               nan |                nan |
| mssa_ens     |         8 |      0.4912 |   nan      |     0.3716 |      0.9207 |      1.6908 |      0.2679 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.3995 |     0.0125 |     0.2937 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4387 |     0.0097 |     0.3197 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.5424 |     0.011  |     0.3849 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |     0      |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |     0      |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |     0      |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - fusion), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_ens      | fusion      |           0.2493 |   0.1181 |    0.3908 |                      14 |             19 |
| early_life        |       0.2 | gbm_ens      | fusion      |           0.175  |   0.0378 |    0.313  |                      11 |             19 |
| early_life        |       0.4 | gbm_ens      | fusion      |           0.078  |  -0.0068 |    0.1741 |                      11 |             19 |
| early_life        |       0.6 | gbm_ens      | fusion      |           0.0629 |  -0.0042 |    0.1332 |                      13 |             19 |
| horizon           |       1   | gbm_ens      | fusion      |           0.0556 |   0.0281 |    0.0909 |                      17 |             19 |
| horizon           |       3   | gbm_ens      | fusion      |           0.0434 |   0.0161 |    0.0764 |                      13 |             19 |
| horizon           |       6   | gbm_ens      | fusion      |           0.0472 |   0.0144 |    0.0858 |                      12 |             19 |
| horizon           |      12   | gbm_ens      | fusion      |           0.0695 |   0.0286 |    0.114  |                      14 |             19 |
| sparse_all        |       1   | gbm_ens      | fusion      |           0.0556 |   0.0277 |    0.0903 |                      17 |             19 |
| sparse_all        |       2   | gbm_ens      | fusion      |           0.0433 |   0.0157 |    0.0781 |                      12 |             19 |
| sparse_all        |       4   | gbm_ens      | fusion      |           0.0351 |   0.0043 |    0.0727 |                      12 |             19 |
| sparse_all        |       8   | gbm_ens      | fusion      |           0.0308 |   0.0011 |    0.0668 |                      13 |             19 |
| sparse_unobserved |       2   | gbm_ens      | fusion      |           0.0503 |   0.021  |    0.0871 |                      14 |             19 |
| sparse_unobserved |       4   | gbm_ens      | fusion      |           0.0358 |   0.0062 |    0.0725 |                      12 |             19 |
| sparse_unobserved |       8   | gbm_ens      | fusion      |           0.0297 |   0.0003 |    0.0663 |                      12 |             19 |
| cold_start        |       0   | gbm_residual | fusion      |           0.256  |   0.1246 |    0.3969 |                      14 |             19 |
| early_life        |       0.2 | gbm_residual | fusion      |           0.1792 |   0.0424 |    0.3215 |                      11 |             19 |
| early_life        |       0.4 | gbm_residual | fusion      |           0.0806 |  -0.0053 |    0.1759 |                      12 |             19 |
| early_life        |       0.6 | gbm_residual | fusion      |           0.0657 |   0      |    0.1359 |                      13 |             19 |
| horizon           |       1   | gbm_residual | fusion      |           0.0581 |   0.0304 |    0.0938 |                      18 |             19 |
| horizon           |       3   | gbm_residual | fusion      |           0.0459 |   0.0188 |    0.0787 |                      14 |             19 |
| horizon           |       6   | gbm_residual | fusion      |           0.0497 |   0.017  |    0.0888 |                      12 |             19 |
| horizon           |      12   | gbm_residual | fusion      |           0.0721 |   0.0311 |    0.1157 |                      14 |             19 |
| sparse_all        |       1   | gbm_residual | fusion      |           0.0581 |   0.0305 |    0.0934 |                      18 |             19 |
| sparse_all        |       2   | gbm_residual | fusion      |           0.0457 |   0.0176 |    0.0811 |                      14 |             19 |
| sparse_all        |       4   | gbm_residual | fusion      |           0.0376 |   0.0072 |    0.0747 |                      12 |             19 |
| sparse_all        |       8   | gbm_residual | fusion      |           0.0334 |   0.0025 |    0.0714 |                      13 |             19 |
| sparse_unobserved |       2   | gbm_residual | fusion      |           0.0527 |   0.0232 |    0.0896 |                      14 |             19 |
| sparse_unobserved |       4   | gbm_residual | fusion      |           0.0383 |   0.0085 |    0.0761 |                      12 |             19 |
| sparse_unobserved |       8   | gbm_residual | fusion      |           0.0323 |   0.0028 |    0.068  |                      12 |             19 |
| cold_start        |       0   | jtg_enkf     | fusion      |           0.3273 |  -0.0211 |    0.6859 |                      10 |             19 |
| early_life        |       0.2 | jtg_enkf     | fusion      |           1.6077 |   1.0562 |    2.1538 |                      18 |             19 |
| early_life        |       0.4 | jtg_enkf     | fusion      |           0.2742 |   0.0901 |    0.4407 |                      16 |             19 |
| early_life        |       0.6 | jtg_enkf     | fusion      |           0.0327 |  -0.0767 |    0.1343 |                      12 |             19 |
| horizon           |       1   | jtg_enkf     | fusion      |           0.0779 |   0.0486 |    0.1019 |                      18 |             19 |
| horizon           |       3   | jtg_enkf     | fusion      |           0.087  |   0.0561 |    0.1136 |                      17 |             19 |
| horizon           |       6   | jtg_enkf     | fusion      |           0.0969 |   0.0607 |    0.1303 |                      17 |             19 |
| horizon           |      12   | jtg_enkf     | fusion      |           0.1798 |   0.1134 |    0.241  |                      17 |             19 |
| sparse_all        |       1   | jtg_enkf     | fusion      |           0.0779 |   0.0479 |    0.1023 |                      18 |             19 |
| sparse_all        |       2   | jtg_enkf     | fusion      |           0.066  |   0.0351 |    0.0908 |                      17 |             19 |
| sparse_all        |       4   | jtg_enkf     | fusion      |           0.0621 |   0.0312 |    0.0903 |                      16 |             19 |
| sparse_all        |       8   | jtg_enkf     | fusion      |           0.084  |   0.0364 |    0.1265 |                      16 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | fusion      |           0.0567 |   0.027  |    0.0817 |                      17 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | fusion      |           0.0628 |   0.0343 |    0.0901 |                      16 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | fusion      |           0.0778 |   0.0351 |    0.1156 |                      16 |             19 |
| cold_start        |       0   | lstm         | fusion      |           3.404  |   2.6836 |    4.0403 |                      18 |             19 |
| early_life        |       0.2 | lstm         | fusion      |           1.6218 |   1.06   |    2.1539 |                      17 |             19 |
| early_life        |       0.4 | lstm         | fusion      |           0.4082 |   0.2222 |    0.5815 |                      16 |             19 |
| early_life        |       0.6 | lstm         | fusion      |           0.2347 |   0.1131 |    0.339  |                      17 |             19 |
| horizon           |       1   | lstm         | fusion      |           0.0628 |   0.0383 |    0.0883 |                      18 |             19 |
| horizon           |       3   | lstm         | fusion      |           0.0874 |   0.0542 |    0.1272 |                      18 |             19 |
| horizon           |       6   | lstm         | fusion      |           0.11   |   0.0585 |    0.1717 |                      18 |             19 |
| horizon           |      12   | lstm         | fusion      |           0.1917 |   0.1054 |    0.2984 |                      17 |             19 |
| sparse_all        |       1   | lstm         | fusion      |           0.0628 |   0.0385 |    0.0886 |                      18 |             19 |
| sparse_all        |       2   | lstm         | fusion      |           0.0607 |   0.0334 |    0.0909 |                      15 |             19 |
| sparse_all        |       4   | lstm         | fusion      |           0.0608 |   0.0351 |    0.0889 |                      16 |             19 |
| sparse_all        |       8   | lstm         | fusion      |           0.0697 |   0.0401 |    0.0972 |                      17 |             19 |
| sparse_unobserved |       2   | lstm         | fusion      |           0.0648 |   0.0363 |    0.095  |                      15 |             19 |
| sparse_unobserved |       4   | lstm         | fusion      |           0.0697 |   0.0413 |    0.1004 |                      16 |             19 |
| sparse_unobserved |       8   | lstm         | fusion      |           0.0712 |   0.043  |    0.0978 |                      17 |             19 |
| cold_start        |       0   | mssa         | fusion      |          -0.0575 |  -0.2156 |    0.0896 |                      10 |             19 |
| early_life        |       0.2 | mssa         | fusion      |          -0.0411 |  -0.1836 |    0.0946 |                      10 |             19 |
| early_life        |       0.4 | mssa         | fusion      |           0.081  |   0.0051 |    0.1596 |                      15 |             19 |
| early_life        |       0.6 | mssa         | fusion      |           0.0556 |   0.0018 |    0.1187 |                      13 |             19 |
| horizon           |       1   | mssa         | fusion      |           0.003  |  -0.0233 |    0.0236 |                      15 |             19 |
| horizon           |       3   | mssa         | fusion      |           0.0221 |  -0.0031 |    0.0423 |                      14 |             19 |
| horizon           |       6   | mssa         | fusion      |           0.0282 |  -0.002  |    0.0542 |                      13 |             19 |
| horizon           |      12   | mssa         | fusion      |           0.0424 |   0.0032 |    0.0783 |                      14 |             19 |
| sparse_all        |       1   | mssa         | fusion      |           0.003  |  -0.0242 |    0.0239 |                      15 |             19 |
| sparse_all        |       2   | mssa         | fusion      |           0.0153 |  -0.0132 |    0.038  |                      15 |             19 |
| sparse_all        |       4   | mssa         | fusion      |           0.0285 |  -0.0009 |    0.0547 |                      14 |             19 |
| sparse_all        |       8   | mssa         | fusion      |           0.0411 |   0.003  |    0.0749 |                      14 |             19 |
| sparse_unobserved |       2   | mssa         | fusion      |           0.0054 |  -0.0247 |    0.0297 |                      13 |             19 |
| sparse_unobserved |       4   | mssa         | fusion      |           0.0277 |  -0.0006 |    0.0531 |                      14 |             19 |
| sparse_unobserved |       8   | mssa         | fusion      |           0.0412 |   0.0032 |    0.075  |                      14 |             19 |
| cold_start        |       0   | mssa_ens     | fusion      |          -0.1049 |  -0.2644 |    0.0506 |                       9 |             19 |
| early_life        |       0.2 | mssa_ens     | fusion      |          -0.0624 |  -0.2085 |    0.0793 |                       9 |             19 |
| early_life        |       0.4 | mssa_ens     | fusion      |           0.0773 |   0.0025 |    0.1514 |                      13 |             19 |
| early_life        |       0.6 | mssa_ens     | fusion      |           0.055  |   0.0022 |    0.1171 |                      13 |             19 |
| horizon           |       1   | mssa_ens     | fusion      |           0.0021 |  -0.0241 |    0.0227 |                      15 |             19 |
| horizon           |       3   | mssa_ens     | fusion      |           0.0205 |  -0.0045 |    0.0415 |                      14 |             19 |
| horizon           |       6   | mssa_ens     | fusion      |           0.0257 |  -0.0045 |    0.0518 |                      13 |             19 |
| horizon           |      12   | mssa_ens     | fusion      |           0.0381 |  -0.0009 |    0.0745 |                      14 |             19 |
| sparse_all        |       1   | mssa_ens     | fusion      |           0.0021 |  -0.0234 |    0.0228 |                      15 |             19 |
| sparse_all        |       2   | mssa_ens     | fusion      |           0.0139 |  -0.0142 |    0.0366 |                      15 |             19 |
| sparse_all        |       4   | mssa_ens     | fusion      |           0.0265 |  -0.0025 |    0.0521 |                      13 |             19 |
| sparse_all        |       8   | mssa_ens     | fusion      |           0.0378 |  -0.001  |    0.0712 |                      14 |             19 |
| sparse_unobserved |       2   | mssa_ens     | fusion      |           0.0042 |  -0.0262 |    0.0285 |                      13 |             19 |
| sparse_unobserved |       4   | mssa_ens     | fusion      |           0.0259 |  -0.002  |    0.0509 |                      14 |             19 |
| sparse_unobserved |       8   | mssa_ens     | fusion      |           0.038  |   0.0015 |    0.0711 |                      14 |             19 |
| cold_start        |       0   | patchtst     | fusion      |           3.4149 |   2.6819 |    4.064  |                      18 |             19 |
| early_life        |       0.2 | patchtst     | fusion      |           1.6371 |   1.0615 |    2.1777 |                      17 |             19 |
| early_life        |       0.4 | patchtst     | fusion      |           0.4095 |   0.2189 |    0.5826 |                      16 |             19 |
| early_life        |       0.6 | patchtst     | fusion      |           0.221  |   0.0897 |    0.3319 |                      16 |             19 |
| horizon           |       1   | patchtst     | fusion      |           0.0381 |   0.0226 |    0.0541 |                      16 |             19 |
| horizon           |       3   | patchtst     | fusion      |           0.0742 |   0.0457 |    0.1061 |                      17 |             19 |
| horizon           |       6   | patchtst     | fusion      |           0.0854 |   0.0433 |    0.1325 |                      16 |             19 |
| horizon           |      12   | patchtst     | fusion      |           0.124  |   0.0553 |    0.2093 |                      17 |             19 |
| sparse_all        |       1   | patchtst     | fusion      |           0.0381 |   0.0224 |    0.0545 |                      16 |             19 |
| sparse_all        |       2   | patchtst     | fusion      |           0.0415 |   0.0235 |    0.0615 |                      18 |             19 |
| sparse_all        |       4   | patchtst     | fusion      |           0.0524 |   0.0286 |    0.0772 |                      15 |             19 |
| sparse_all        |       8   | patchtst     | fusion      |           0.0852 |   0.0405 |    0.128  |                      15 |             19 |
| sparse_unobserved |       2   | patchtst     | fusion      |           0.0395 |   0.0197 |    0.0611 |                      15 |             19 |
| sparse_unobserved |       4   | patchtst     | fusion      |           0.0572 |   0.0309 |    0.0848 |                      16 |             19 |
| sparse_unobserved |       8   | patchtst     | fusion      |           0.0832 |   0.0412 |    0.1241 |                      15 |             19 |
| cold_start        |       0   | persistence  | fusion      |           3.6162 |   2.9248 |    4.2531 |                      19 |             19 |
| early_life        |       0.2 | persistence  | fusion      |           1.7862 |   1.2127 |    2.3227 |                      17 |             19 |
| early_life        |       0.4 | persistence  | fusion      |           0.4843 |   0.2913 |    0.6745 |                      16 |             19 |
| early_life        |       0.6 | persistence  | fusion      |           0.2443 |   0.0923 |    0.3803 |                      15 |             19 |
| horizon           |       1   | persistence  | fusion      |           0.0507 |   0.0138 |    0.0815 |                      16 |             19 |
| horizon           |       3   | persistence  | fusion      |           0.1273 |   0.0843 |    0.1642 |                      17 |             19 |
| horizon           |       6   | persistence  | fusion      |           0.2706 |   0.1967 |    0.3395 |                      17 |             19 |
| horizon           |      12   | persistence  | fusion      |           0.5373 |   0.4227 |    0.6442 |                      18 |             19 |
| sparse_all        |       1   | persistence  | fusion      |           0.0507 |   0.0143 |    0.0809 |                      16 |             19 |
| sparse_all        |       2   | persistence  | fusion      |           0.0701 |   0.0351 |    0.1008 |                      16 |             19 |
| sparse_all        |       4   | persistence  | fusion      |           0.1227 |   0.0785 |    0.1642 |                      16 |             19 |
| sparse_all        |       8   | persistence  | fusion      |           0.2598 |   0.1733 |    0.3389 |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | fusion      |           0.0508 |   0.0139 |    0.0828 |                      16 |             19 |
| sparse_unobserved |       4   | persistence  | fusion      |           0.1054 |   0.064  |    0.1423 |                      16 |             19 |
| sparse_unobserved |       8   | persistence  | fusion      |           0.2412 |   0.1613 |    0.3153 |                      16 |             19 |

### Paired structure-level RMSE difference (model - mssa_ens), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | fusion       | mssa_ens    |           0.1049 |  -0.0493 |    0.2627 |                      10 |             19 |
| early_life        |       0.2 | fusion       | mssa_ens    |           0.0624 |  -0.0809 |    0.2064 |                      10 |             19 |
| early_life        |       0.4 | fusion       | mssa_ens    |          -0.0773 |  -0.1528 |   -0.003  |                       6 |             19 |
| early_life        |       0.6 | fusion       | mssa_ens    |          -0.055  |  -0.1173 |   -0.0015 |                       6 |             19 |
| horizon           |       1   | fusion       | mssa_ens    |          -0.0021 |  -0.0228 |    0.0245 |                       4 |             19 |
| horizon           |       3   | fusion       | mssa_ens    |          -0.0205 |  -0.0412 |    0.0049 |                       5 |             19 |
| horizon           |       6   | fusion       | mssa_ens    |          -0.0257 |  -0.0515 |    0.0057 |                       6 |             19 |
| horizon           |      12   | fusion       | mssa_ens    |          -0.0381 |  -0.0741 |    0.001  |                       5 |             19 |
| sparse_all        |       1   | fusion       | mssa_ens    |          -0.0021 |  -0.0232 |    0.0241 |                       4 |             19 |
| sparse_all        |       2   | fusion       | mssa_ens    |          -0.0139 |  -0.0364 |    0.0142 |                       4 |             19 |
| sparse_all        |       4   | fusion       | mssa_ens    |          -0.0265 |  -0.052  |    0.0038 |                       6 |             19 |
| sparse_all        |       8   | fusion       | mssa_ens    |          -0.0378 |  -0.0712 |   -0.0003 |                       5 |             19 |
| sparse_unobserved |       2   | fusion       | mssa_ens    |          -0.0042 |  -0.0282 |    0.0266 |                       6 |             19 |
| sparse_unobserved |       4   | fusion       | mssa_ens    |          -0.0259 |  -0.0509 |    0.0024 |                       5 |             19 |
| sparse_unobserved |       8   | fusion       | mssa_ens    |          -0.038  |  -0.0708 |   -0.0003 |                       5 |             19 |
| cold_start        |       0   | gbm_ens      | mssa_ens    |           0.3542 |   0.089  |    0.6371 |                      12 |             19 |
| early_life        |       0.2 | gbm_ens      | mssa_ens    |           0.2374 |  -0.0238 |    0.512  |                      10 |             19 |
| early_life        |       0.4 | gbm_ens      | mssa_ens    |           0.0007 |  -0.1292 |    0.1409 |                       9 |             19 |
| early_life        |       0.6 | gbm_ens      | mssa_ens    |           0.0079 |  -0.0964 |    0.1094 |                       8 |             19 |
| horizon           |       1   | gbm_ens      | mssa_ens    |           0.0535 |   0.0056 |    0.1155 |                      11 |             19 |
| horizon           |       3   | gbm_ens      | mssa_ens    |           0.0229 |  -0.0247 |    0.0808 |                       8 |             19 |
| horizon           |       6   | gbm_ens      | mssa_ens    |           0.0216 |  -0.0363 |    0.0915 |                       8 |             19 |
| horizon           |      12   | gbm_ens      | mssa_ens    |           0.0313 |  -0.0447 |    0.113  |                      10 |             19 |
| sparse_all        |       1   | gbm_ens      | mssa_ens    |           0.0535 |   0.0056 |    0.1154 |                      11 |             19 |
| sparse_all        |       2   | gbm_ens      | mssa_ens    |           0.0294 |  -0.021  |    0.0939 |                       8 |             19 |
| sparse_all        |       4   | gbm_ens      | mssa_ens    |           0.0086 |  -0.0462 |    0.0736 |                       8 |             19 |
| sparse_all        |       8   | gbm_ens      | mssa_ens    |          -0.007  |  -0.0662 |    0.0664 |                       6 |             19 |
| sparse_unobserved |       2   | gbm_ens      | mssa_ens    |           0.0462 |  -0.0065 |    0.1129 |                       8 |             19 |
| sparse_unobserved |       4   | gbm_ens      | mssa_ens    |           0.0099 |  -0.0424 |    0.0748 |                       8 |             19 |
| sparse_unobserved |       8   | gbm_ens      | mssa_ens    |          -0.0083 |  -0.0661 |    0.0627 |                       6 |             19 |
| cold_start        |       0   | gbm_residual | mssa_ens    |           0.3609 |   0.0935 |    0.6387 |                      12 |             19 |
| early_life        |       0.2 | gbm_residual | mssa_ens    |           0.2416 |  -0.0142 |    0.5171 |                      10 |             19 |
| early_life        |       0.4 | gbm_residual | mssa_ens    |           0.0033 |  -0.1292 |    0.1421 |                       9 |             19 |
| early_life        |       0.6 | gbm_residual | mssa_ens    |           0.0108 |  -0.0912 |    0.1098 |                       9 |             19 |
| horizon           |       1   | gbm_residual | mssa_ens    |           0.0559 |   0.0083 |    0.1164 |                      11 |             19 |
| horizon           |       3   | gbm_residual | mssa_ens    |           0.0254 |  -0.0222 |    0.0839 |                       9 |             19 |
| horizon           |       6   | gbm_residual | mssa_ens    |           0.024  |  -0.0348 |    0.0938 |                       8 |             19 |
| horizon           |      12   | gbm_residual | mssa_ens    |           0.034  |  -0.0421 |    0.1141 |                      10 |             19 |
| sparse_all        |       1   | gbm_residual | mssa_ens    |           0.0559 |   0.0079 |    0.1177 |                      11 |             19 |
| sparse_all        |       2   | gbm_residual | mssa_ens    |           0.0318 |  -0.0181 |    0.095  |                       8 |             19 |
| sparse_all        |       4   | gbm_residual | mssa_ens    |           0.0111 |  -0.0427 |    0.0775 |                       8 |             19 |
| sparse_all        |       8   | gbm_residual | mssa_ens    |          -0.0044 |  -0.0644 |    0.067  |                       7 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa_ens    |           0.0486 |  -0.0045 |    0.1146 |                       8 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa_ens    |           0.0124 |  -0.0393 |    0.0746 |                       8 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa_ens    |          -0.0057 |  -0.064  |    0.0657 |                       6 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa_ens    |           0.4322 |   0.1476 |    0.7432 |                      12 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa_ens    |           1.6701 |   1.1882 |    2.1575 |                      18 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa_ens    |           0.1969 |   0.0691 |    0.3129 |                      15 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa_ens    |          -0.0223 |  -0.1005 |    0.0355 |                      11 |             19 |
| horizon           |       1   | jtg_enkf     | mssa_ens    |           0.0758 |   0.0659 |    0.086  |                      19 |             19 |
| horizon           |       3   | jtg_enkf     | mssa_ens    |           0.0666 |   0.0553 |    0.0777 |                      19 |             19 |
| horizon           |       6   | jtg_enkf     | mssa_ens    |           0.0712 |   0.0523 |    0.0909 |                      18 |             19 |
| horizon           |      12   | jtg_enkf     | mssa_ens    |           0.1417 |   0.0975 |    0.185  |                      17 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa_ens    |           0.0758 |   0.0659 |    0.0858 |                      19 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa_ens    |           0.0521 |   0.0434 |    0.0612 |                      19 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa_ens    |           0.0356 |   0.0193 |    0.0508 |                      17 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa_ens    |           0.0462 |   0.0104 |    0.0799 |                      14 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa_ens    |           0.0525 |   0.043  |    0.0628 |                      19 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa_ens    |           0.0369 |   0.0216 |    0.0517 |                      16 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa_ens    |           0.0398 |   0.0087 |    0.0688 |                      14 |             19 |
| cold_start        |       0   | lstm         | mssa_ens    |           3.5089 |   2.7841 |    4.1517 |                      19 |             19 |
| early_life        |       0.2 | lstm         | mssa_ens    |           1.6842 |   1.0702 |    2.291  |                      17 |             19 |
| early_life        |       0.4 | lstm         | mssa_ens    |           0.331  |   0.1286 |    0.5256 |                      14 |             19 |
| early_life        |       0.6 | lstm         | mssa_ens    |           0.1797 |   0.0584 |    0.28   |                      16 |             19 |
| horizon           |       1   | lstm         | mssa_ens    |           0.0607 |   0.0261 |    0.0974 |                      14 |             19 |
| horizon           |       3   | lstm         | mssa_ens    |           0.0669 |   0.0215 |    0.1151 |                      13 |             19 |
| horizon           |       6   | lstm         | mssa_ens    |           0.0844 |   0.0219 |    0.1545 |                      12 |             19 |
| horizon           |      12   | lstm         | mssa_ens    |           0.1535 |   0.0603 |    0.2563 |                      14 |             19 |
| sparse_all        |       1   | lstm         | mssa_ens    |           0.0607 |   0.0262 |    0.0982 |                      14 |             19 |
| sparse_all        |       2   | lstm         | mssa_ens    |           0.0468 |   0.0106 |    0.0862 |                      13 |             19 |
| sparse_all        |       4   | lstm         | mssa_ens    |           0.0344 |   0.0026 |    0.0693 |                      13 |             19 |
| sparse_all        |       8   | lstm         | mssa_ens    |           0.032  |  -0.0008 |    0.065  |                      12 |             19 |
| sparse_unobserved |       2   | lstm         | mssa_ens    |           0.0607 |   0.0197 |    0.1036 |                      12 |             19 |
| sparse_unobserved |       4   | lstm         | mssa_ens    |           0.0438 |   0.0098 |    0.0806 |                      11 |             19 |
| sparse_unobserved |       8   | lstm         | mssa_ens    |           0.0332 |   0.0007 |    0.066  |                      12 |             19 |
| cold_start        |       0   | mssa         | mssa_ens    |           0.0474 |   0.0127 |    0.0949 |                      19 |             19 |
| early_life        |       0.2 | mssa         | mssa_ens    |           0.0213 |   0.006  |    0.0426 |                      19 |             19 |
| early_life        |       0.4 | mssa         | mssa_ens    |           0.0037 |   0.0016 |    0.0063 |                      19 |             19 |
| early_life        |       0.6 | mssa         | mssa_ens    |           0.0006 |   0.0002 |    0.0012 |                      19 |             19 |
| horizon           |       1   | mssa         | mssa_ens    |           0.0008 |   0.0006 |    0.0012 |                      19 |             19 |
| horizon           |       3   | mssa         | mssa_ens    |           0.0016 |   0.0012 |    0.0021 |                      19 |             19 |
| horizon           |       6   | mssa         | mssa_ens    |           0.0026 |   0.002  |    0.0034 |                      19 |             19 |
| horizon           |      12   | mssa         | mssa_ens    |           0.0043 |   0.0031 |    0.0058 |                      19 |             19 |
| sparse_all        |       1   | mssa         | mssa_ens    |           0.0008 |   0.0006 |    0.0012 |                      19 |             19 |
| sparse_all        |       2   | mssa         | mssa_ens    |           0.0014 |   0.001  |    0.002  |                      19 |             19 |
| sparse_all        |       4   | mssa         | mssa_ens    |           0.002  |   0.0015 |    0.0028 |                      19 |             19 |
| sparse_all        |       8   | mssa         | mssa_ens    |           0.0034 |   0.0026 |    0.0043 |                      19 |             19 |
| sparse_unobserved |       2   | mssa         | mssa_ens    |           0.0012 |   0.0008 |    0.0018 |                      19 |             19 |
| sparse_unobserved |       4   | mssa         | mssa_ens    |           0.0018 |   0.0013 |    0.0027 |                      19 |             19 |
| sparse_unobserved |       8   | mssa         | mssa_ens    |           0.0032 |   0.0024 |    0.0041 |                      19 |             19 |
| cold_start        |       0   | patchtst     | mssa_ens    |           3.5198 |   2.7967 |    4.1853 |                      19 |             19 |
| early_life        |       0.2 | patchtst     | mssa_ens    |           1.6995 |   1.0861 |    2.3137 |                      17 |             19 |
| early_life        |       0.4 | patchtst     | mssa_ens    |           0.3322 |   0.1306 |    0.5236 |                      15 |             19 |
| early_life        |       0.6 | patchtst     | mssa_ens    |           0.166  |   0.0344 |    0.2715 |                      16 |             19 |
| horizon           |       1   | patchtst     | mssa_ens    |           0.036  |   0.0115 |    0.0641 |                      13 |             19 |
| horizon           |       3   | patchtst     | mssa_ens    |           0.0537 |   0.0153 |    0.0956 |                      14 |             19 |
| horizon           |       6   | patchtst     | mssa_ens    |           0.0597 |   0.0053 |    0.1185 |                      11 |             19 |
| horizon           |      12   | patchtst     | mssa_ens    |           0.0859 |   0.0128 |    0.1661 |                      11 |             19 |
| sparse_all        |       1   | patchtst     | mssa_ens    |           0.036  |   0.0114 |    0.0638 |                      13 |             19 |
| sparse_all        |       2   | patchtst     | mssa_ens    |           0.0276 |   0.0008 |    0.0571 |                      10 |             19 |
| sparse_all        |       4   | patchtst     | mssa_ens    |           0.0259 |  -0.0022 |    0.0539 |                      11 |             19 |
| sparse_all        |       8   | patchtst     | mssa_ens    |           0.0474 |   0.0091 |    0.0864 |                      16 |             19 |
| sparse_unobserved |       2   | patchtst     | mssa_ens    |           0.0353 |   0.0028 |    0.0705 |                      11 |             19 |
| sparse_unobserved |       4   | patchtst     | mssa_ens    |           0.0313 |   0.0011 |    0.0619 |                      11 |             19 |
| sparse_unobserved |       8   | patchtst     | mssa_ens    |           0.0451 |   0.0098 |    0.0821 |                      16 |             19 |
| cold_start        |       0   | persistence  | mssa_ens    |           3.7211 |   3.0357 |    4.3671 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa_ens    |           1.8486 |   1.2298 |    2.4549 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa_ens    |           0.407  |   0.2038 |    0.6083 |                      17 |             19 |
| early_life        |       0.6 | persistence  | mssa_ens    |           0.1893 |   0.0384 |    0.3154 |                      16 |             19 |
| horizon           |       1   | persistence  | mssa_ens    |           0.0486 |   0.034  |    0.0622 |                      17 |             19 |
| horizon           |       3   | persistence  | mssa_ens    |           0.1068 |   0.0825 |    0.1299 |                      18 |             19 |
| horizon           |       6   | persistence  | mssa_ens    |           0.245  |   0.1923 |    0.2963 |                      19 |             19 |
| horizon           |      12   | persistence  | mssa_ens    |           0.4992 |   0.4119 |    0.5866 |                      19 |             19 |
| sparse_all        |       1   | persistence  | mssa_ens    |           0.0486 |   0.0348 |    0.0624 |                      17 |             19 |
| sparse_all        |       2   | persistence  | mssa_ens    |           0.0562 |   0.038  |    0.0738 |                      17 |             19 |
| sparse_all        |       4   | persistence  | mssa_ens    |           0.0963 |   0.0614 |    0.1294 |                      18 |             19 |
| sparse_all        |       8   | persistence  | mssa_ens    |           0.222  |   0.1531 |    0.2912 |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | mssa_ens    |           0.0467 |   0.0271 |    0.0671 |                      16 |             19 |
| sparse_unobserved |       4   | persistence  | mssa_ens    |           0.0795 |   0.0438 |    0.1134 |                      17 |             19 |
| sparse_unobserved |       8   | persistence  | mssa_ens    |           0.2032 |   0.1359 |    0.2702 |                      17 |             19 |

### Paired structure-level RMSE difference (model - mssa), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | fusion       | mssa        |           0.0575 |  -0.0944 |    0.2157 |                       9 |             19 |
| early_life        |       0.2 | fusion       | mssa        |           0.0411 |  -0.0966 |    0.1804 |                       9 |             19 |
| early_life        |       0.4 | fusion       | mssa        |          -0.081  |  -0.1575 |   -0.006  |                       4 |             19 |
| early_life        |       0.6 | fusion       | mssa        |          -0.0556 |  -0.1178 |   -0.0024 |                       6 |             19 |
| horizon           |       1   | fusion       | mssa        |          -0.003  |  -0.0236 |    0.0236 |                       4 |             19 |
| horizon           |       3   | fusion       | mssa        |          -0.0221 |  -0.0427 |    0.0033 |                       5 |             19 |
| horizon           |       6   | fusion       | mssa        |          -0.0282 |  -0.0539 |    0.0028 |                       6 |             19 |
| horizon           |      12   | fusion       | mssa        |          -0.0424 |  -0.0781 |   -0.0034 |                       5 |             19 |
| sparse_all        |       1   | fusion       | mssa        |          -0.003  |  -0.0241 |    0.0231 |                       4 |             19 |
| sparse_all        |       2   | fusion       | mssa        |          -0.0153 |  -0.0377 |    0.0127 |                       4 |             19 |
| sparse_all        |       4   | fusion       | mssa        |          -0.0285 |  -0.0542 |    0.002  |                       5 |             19 |
| sparse_all        |       8   | fusion       | mssa        |          -0.0411 |  -0.0751 |   -0.0034 |                       5 |             19 |
| sparse_unobserved |       2   | fusion       | mssa        |          -0.0054 |  -0.0294 |    0.0252 |                       6 |             19 |
| sparse_unobserved |       4   | fusion       | mssa        |          -0.0277 |  -0.053  |    0.0008 |                       5 |             19 |
| sparse_unobserved |       8   | fusion       | mssa        |          -0.0412 |  -0.0746 |   -0.0035 |                       5 |             19 |
| cold_start        |       0   | gbm_ens      | mssa        |           0.3068 |   0.0492 |    0.5853 |                      11 |             19 |
| early_life        |       0.2 | gbm_ens      | mssa        |           0.216  |  -0.0408 |    0.4821 |                      10 |             19 |
| early_life        |       0.4 | gbm_ens      | mssa        |          -0.003  |  -0.133  |    0.1364 |                       9 |             19 |
| early_life        |       0.6 | gbm_ens      | mssa        |           0.0073 |  -0.0968 |    0.1086 |                       8 |             19 |
| horizon           |       1   | gbm_ens      | mssa        |           0.0527 |   0.0048 |    0.1144 |                      11 |             19 |
| horizon           |       3   | gbm_ens      | mssa        |           0.0214 |  -0.0264 |    0.0791 |                       8 |             19 |
| horizon           |       6   | gbm_ens      | mssa        |           0.019  |  -0.0387 |    0.0887 |                       8 |             19 |
| horizon           |      12   | gbm_ens      | mssa        |           0.0271 |  -0.0484 |    0.1083 |                      10 |             19 |
| sparse_all        |       1   | gbm_ens      | mssa        |           0.0527 |   0.0048 |    0.1144 |                      11 |             19 |
| sparse_all        |       2   | gbm_ens      | mssa        |           0.028  |  -0.0224 |    0.0923 |                       8 |             19 |
| sparse_all        |       4   | gbm_ens      | mssa        |           0.0066 |  -0.0482 |    0.0716 |                       8 |             19 |
| sparse_all        |       8   | gbm_ens      | mssa        |          -0.0104 |  -0.0695 |    0.063  |                       6 |             19 |
| sparse_unobserved |       2   | gbm_ens      | mssa        |           0.0449 |  -0.0077 |    0.1115 |                       8 |             19 |
| sparse_unobserved |       4   | gbm_ens      | mssa        |           0.0081 |  -0.0443 |    0.0728 |                       8 |             19 |
| sparse_unobserved |       8   | gbm_ens      | mssa        |          -0.0115 |  -0.0695 |    0.0598 |                       6 |             19 |
| cold_start        |       0   | gbm_residual | mssa        |           0.3135 |   0.0509 |    0.5867 |                      12 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |           0.2202 |  -0.0297 |    0.4882 |                      10 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.0004 |  -0.1325 |    0.1389 |                       9 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |           0.0102 |  -0.0916 |    0.1089 |                       9 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0551 |   0.0075 |    0.1155 |                      11 |             19 |
| horizon           |       3   | gbm_residual | mssa        |           0.0238 |  -0.0237 |    0.0822 |                       8 |             19 |
| horizon           |       6   | gbm_residual | mssa        |           0.0214 |  -0.0373 |    0.0909 |                       8 |             19 |
| horizon           |      12   | gbm_residual | mssa        |           0.0297 |  -0.0462 |    0.1098 |                      10 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0551 |   0.0071 |    0.1167 |                      11 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |           0.0305 |  -0.0196 |    0.0936 |                       8 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |           0.0091 |  -0.0448 |    0.0755 |                       8 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.0077 |  -0.0678 |    0.0637 |                       7 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0473 |  -0.0057 |    0.1132 |                       8 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |           0.0106 |  -0.0412 |    0.0728 |                       8 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.0089 |  -0.0675 |    0.0626 |                       6 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.3849 |   0.0906 |    0.7066 |                      12 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.6487 |   1.1628 |    2.1362 |                      18 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |           0.1931 |   0.0659 |    0.3087 |                      15 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.0229 |  -0.101  |    0.0348 |                      11 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0749 |   0.0649 |    0.0853 |                      19 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |           0.065  |   0.0535 |    0.0764 |                      19 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |           0.0686 |   0.0494 |    0.0884 |                      18 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.1374 |   0.0927 |    0.181  |                      17 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0749 |   0.065  |    0.0851 |                      19 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.0507 |   0.0418 |    0.06   |                      19 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |           0.0336 |   0.0171 |    0.0489 |                      17 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |           0.0428 |   0.0068 |    0.0767 |                      14 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0513 |   0.0415 |    0.0618 |                      19 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |           0.0351 |   0.0195 |    0.0501 |                      16 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |           0.0366 |   0.0053 |    0.0657 |                      14 |             19 |
| cold_start        |       0   | lstm         | mssa        |           3.4616 |   2.75   |    4.0867 |                      19 |             19 |
| early_life        |       0.2 | lstm         | mssa        |           1.6628 |   1.0579 |    2.2587 |                      17 |             19 |
| early_life        |       0.4 | lstm         | mssa        |           0.3272 |   0.1259 |    0.5206 |                      14 |             19 |
| early_life        |       0.6 | lstm         | mssa        |           0.1791 |   0.0579 |    0.2791 |                      16 |             19 |
| horizon           |       1   | lstm         | mssa        |           0.0598 |   0.0253 |    0.0965 |                      14 |             19 |
| horizon           |       3   | lstm         | mssa        |           0.0653 |   0.02   |    0.1134 |                      13 |             19 |
| horizon           |       6   | lstm         | mssa        |           0.0818 |   0.0194 |    0.1518 |                      12 |             19 |
| horizon           |      12   | lstm         | mssa        |           0.1492 |   0.0558 |    0.2523 |                      14 |             19 |
| sparse_all        |       1   | lstm         | mssa        |           0.0598 |   0.0255 |    0.0973 |                      14 |             19 |
| sparse_all        |       2   | lstm         | mssa        |           0.0454 |   0.0094 |    0.0848 |                      13 |             19 |
| sparse_all        |       4   | lstm         | mssa        |           0.0324 |   0.0007 |    0.0674 |                      10 |             19 |
| sparse_all        |       8   | lstm         | mssa        |           0.0286 |  -0.0045 |    0.0619 |                      12 |             19 |
| sparse_unobserved |       2   | lstm         | mssa        |           0.0594 |   0.0187 |    0.1021 |                      12 |             19 |
| sparse_unobserved |       4   | lstm         | mssa        |           0.042  |   0.0079 |    0.0786 |                      11 |             19 |
| sparse_unobserved |       8   | lstm         | mssa        |           0.03   |  -0.0028 |    0.0632 |                      12 |             19 |
| cold_start        |       0   | mssa_ens     | mssa        |          -0.0474 |  -0.0949 |   -0.0127 |                       0 |             19 |
| early_life        |       0.2 | mssa_ens     | mssa        |          -0.0213 |  -0.0426 |   -0.006  |                       0 |             19 |
| early_life        |       0.4 | mssa_ens     | mssa        |          -0.0037 |  -0.0063 |   -0.0016 |                       0 |             19 |
| early_life        |       0.6 | mssa_ens     | mssa        |          -0.0006 |  -0.0012 |   -0.0002 |                       0 |             19 |
| horizon           |       1   | mssa_ens     | mssa        |          -0.0008 |  -0.0012 |   -0.0006 |                       0 |             19 |
| horizon           |       3   | mssa_ens     | mssa        |          -0.0016 |  -0.0021 |   -0.0012 |                       0 |             19 |
| horizon           |       6   | mssa_ens     | mssa        |          -0.0026 |  -0.0034 |   -0.002  |                       0 |             19 |
| horizon           |      12   | mssa_ens     | mssa        |          -0.0043 |  -0.0058 |   -0.0031 |                       0 |             19 |
| sparse_all        |       1   | mssa_ens     | mssa        |          -0.0008 |  -0.0012 |   -0.0006 |                       0 |             19 |
| sparse_all        |       2   | mssa_ens     | mssa        |          -0.0014 |  -0.002  |   -0.001  |                       0 |             19 |
| sparse_all        |       4   | mssa_ens     | mssa        |          -0.002  |  -0.0028 |   -0.0015 |                       0 |             19 |
| sparse_all        |       8   | mssa_ens     | mssa        |          -0.0034 |  -0.0043 |   -0.0026 |                       0 |             19 |
| sparse_unobserved |       2   | mssa_ens     | mssa        |          -0.0012 |  -0.0018 |   -0.0008 |                       0 |             19 |
| sparse_unobserved |       4   | mssa_ens     | mssa        |          -0.0018 |  -0.0027 |   -0.0013 |                       0 |             19 |
| sparse_unobserved |       8   | mssa_ens     | mssa        |          -0.0032 |  -0.0041 |   -0.0024 |                       0 |             19 |
| cold_start        |       0   | patchtst     | mssa        |           3.4724 |   2.7671 |    4.1172 |                      19 |             19 |
| early_life        |       0.2 | patchtst     | mssa        |           1.6781 |   1.0723 |    2.2821 |                      17 |             19 |
| early_life        |       0.4 | patchtst     | mssa        |           0.3285 |   0.1275 |    0.5194 |                      15 |             19 |
| early_life        |       0.6 | patchtst     | mssa        |           0.1654 |   0.0341 |    0.2709 |                      16 |             19 |
| horizon           |       1   | patchtst     | mssa        |           0.0351 |   0.0108 |    0.0631 |                      12 |             19 |
| horizon           |       3   | patchtst     | mssa        |           0.0521 |   0.0139 |    0.0938 |                      14 |             19 |
| horizon           |       6   | patchtst     | mssa        |           0.0571 |   0.0029 |    0.1157 |                      10 |             19 |
| horizon           |      12   | patchtst     | mssa        |           0.0816 |   0.0086 |    0.1619 |                      11 |             19 |
| sparse_all        |       1   | patchtst     | mssa        |           0.0351 |   0.0107 |    0.0629 |                      12 |             19 |
| sparse_all        |       2   | patchtst     | mssa        |           0.0262 |  -0.0004 |    0.0557 |                      10 |             19 |
| sparse_all        |       4   | patchtst     | mssa        |           0.0239 |  -0.004  |    0.0519 |                      10 |             19 |
| sparse_all        |       8   | patchtst     | mssa        |           0.044  |   0.0055 |    0.0833 |                      16 |             19 |
| sparse_unobserved |       2   | patchtst     | mssa        |           0.0341 |   0.0017 |    0.0692 |                      11 |             19 |
| sparse_unobserved |       4   | patchtst     | mssa        |           0.0294 |  -0.0008 |    0.0601 |                      11 |             19 |
| sparse_unobserved |       8   | patchtst     | mssa        |           0.042  |   0.0063 |    0.0791 |                      16 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.6738 |   3.0044 |    4.293  |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.8273 |   1.2157 |    2.4201 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.4033 |   0.2015 |    0.6044 |                      17 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.1887 |   0.0378 |    0.315  |                      16 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0477 |   0.0331 |    0.0614 |                      17 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.1053 |   0.081  |    0.1283 |                      18 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.2424 |   0.1899 |    0.2935 |                      19 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.4949 |   0.4083 |    0.5814 |                      19 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0477 |   0.0339 |    0.0616 |                      17 |             19 |
| sparse_all        |       2   | persistence  | mssa        |           0.0549 |   0.0366 |    0.0725 |                      17 |             19 |
| sparse_all        |       4   | persistence  | mssa        |           0.0943 |   0.0594 |    0.1275 |                      18 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.2187 |   0.1496 |    0.288  |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0454 |   0.0257 |    0.066  |                      16 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0776 |   0.0419 |    0.1116 |                      17 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.2    |   0.1327 |    0.2671 |                      17 |             19 |

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.5685 |     0.0815 |     1.1851 |      0.8799 |      4.8334 |      0.8507 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      1.598  |     0.2781 |     1.2615 |      0.828  |      4.5801 |      0.9114 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.5495 |     0.0911 |     1.1729 |      0.8595 |      4.7733 |      0.8523 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.615  |     0.0592 |     1.2253 |      0.8855 |      5.0646 |      0.8821 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.5529 |     0.1448 |     1.1775 |      0.8829 |      4.9195 |      0.852  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.674  |     0.2599 |     1.2585 |      0.8779 |      5.3074 |      0.8987 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         0 |      1.5152 |     0.168  |     1.1422 |      0.7024 |      2.6953 |      0.884  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.5886 |     0.1616 |     1.196  |      0.878  |      4.6682 |      0.862  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         0 |      1.5368 |     0.1387 |     1.1501 |      0.8199 |      3.773  |      0.8573 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.1668 |     0.2375 |     0.9186 |      0.8818 |      3.8099 |      0.6505 |             1.1207 |                0.0836 |                          0 |            9.8975 |            11.215  |
| mssa:fixed_mat  |       0.4 |      0.6289 |     0.035  |     0.4975 |      0.9782 |      2.8965 |      0.3539 |             0.6971 |                0.0837 |                          0 |            1.792  |             7.4893 |
| mssa:fixed_mat  |       0.6 |      0.5566 |     0.0176 |     0.4369 |      0.942  |      2.1891 |      0.309  |             0.6411 |                0.0734 |                          0 |            2.72   |            14.19   |
| mssa:neural_ssm |       0.2 |      1.2436 |     0.2637 |     1.0045 |      0.8817 |      3.9365 |      0.7073 |             1.2642 |                0.1122 |                          0 |           13.6532 |             6.201  |
| mssa:neural_ssm |       0.4 |      0.7463 |     0.0717 |     0.5999 |      0.9742 |      3.1746 |      0.4204 |             0.8685 |                0.1423 |                          0 |            7.137  |             9.4267 |
| mssa:neural_ssm |       0.6 |      0.5744 |     0.0766 |     0.4441 |      0.9884 |      2.7026 |      0.3197 |             0.6558 |                0.1372 |                          0 |            1.455  |             7.023  |
| mssa:no_defl    |       0.2 |      1.1609 |     0.0853 |     0.9181 |      0.8776 |      3.9301 |      0.6573 |             1.0588 |                0.0846 |                          0 |           10.187  |             7.2047 |
| mssa:no_defl    |       0.4 |      0.6223 |     0.039  |     0.4883 |      0.9725 |      2.9648 |      0.3512 |             0.6976 |                0.0861 |                          0 |            0.462  |             6.9627 |
| mssa:no_defl    |       0.6 |      0.5727 |     0.0179 |     0.4517 |      0.9384 |      2.2369 |      0.3183 |             0.6888 |                0.0806 |                          0 |          nan      |           nan      |
| mssa:no_disc    |       0.2 |      1.1728 |     0.1218 |     0.9446 |      0.8955 |      4.1406 |      0.6683 |             1.065  |                0.0814 |                          0 |           10.8562 |             8.0597 |
| mssa:no_disc    |       0.4 |      0.61   |     0.0343 |     0.4908 |      0.9786 |      3.0358 |      0.3511 |             0.6777 |                0.0801 |                          0 |            5.1553 |             7.1936 |
| mssa:no_disc    |       0.6 |      0.554  |     0.0219 |     0.4382 |      0.9445 |      2.236  |      0.3087 |             0.6518 |                0.0734 |                          0 |            4.28   |            14.266  |
| mssa:no_ms      |       0.2 |      1.1033 |     0.1705 |     0.8652 |      0.8711 |      3.548  |      0.6176 |             1.074  |                0.0885 |                          0 |            9.4232 |            14.428  |
| mssa:no_ms      |       0.4 |      0.6737 |     0.0159 |     0.5258 |      0.944  |      2.728  |      0.372  |             0.812  |                0.0941 |                          0 |            1.0153 |             9.88   |
| mssa:no_ms      |       0.6 |      0.6147 |     0.0091 |     0.4881 |      0.9164 |      2.163  |      0.3408 |             0.7509 |                0.0878 |                          0 |          nan      |           nan      |
| mssa:no_proj    |       0.2 |      1.2649 |     0.3346 |     0.9899 |      0.8617 |      3.8824 |      0.7163 |             1.2167 |                0.0534 |                          0 |            9.8892 |             7.7398 |
| mssa:no_proj    |       0.4 |      0.6788 |     0.1178 |     0.5501 |      0.9621 |      2.8874 |      0.3842 |             0.7527 |                0.0498 |                          0 |            5.7493 |             4.9278 |
| mssa:no_proj    |       0.6 |      0.4983 |     0.0167 |     0.3865 |      0.9683 |      2.1734 |      0.2777 |             0.477  |                0.0383 |                          0 |            3.62   |            10.07   |
| mssa:no_rate    |       0.2 |      1.3482 |     0.1357 |     1.0205 |      0.6949 |      2.3788 |      0.7892 |             1.2394 |                0.063  |                          0 |           10.3819 |             9.489  |
| mssa:no_rate    |       0.4 |      0.8793 |     0.0674 |     0.6962 |      0.7872 |      2.242  |      0.5112 |             0.8709 |                0.0674 |                          0 |            5.414  |            14.0587 |
| mssa:no_rate    |       0.6 |      0.5273 |     0.0384 |     0.4004 |      0.9281 |      2.0499 |      0.2885 |             0.515  |                0.0439 |                          0 |            1.714  |             6.9688 |
| mssa:no_rev     |       0.2 |      1.1491 |     0.0819 |     0.9007 |      0.8862 |      3.7945 |      0.6434 |             1.103  |                0      |                          0 |           11.648  |            10.21   |
| mssa:no_rev     |       0.4 |      0.6388 |     0.034  |     0.4974 |      0.98   |      3.2223 |      0.3643 |             0.6305 |                0      |                          0 |            5.6327 |             4.9938 |
| mssa:no_rev     |       0.6 |      0.5183 |     0.0174 |     0.4091 |      0.9895 |      2.6523 |      0.2983 |             0.3703 |                0      |                          0 |          nan      |            14.765  |
| mssa:no_rw      |       0.2 |      1.1295 |     0.0977 |     0.863  |      0.8344 |      3.4437 |      0.6347 |             1.0118 |                0.0945 |                          0 |            9.8581 |            17.968  |
| mssa:no_rw      |       0.4 |      0.6277 |     0.0046 |     0.4891 |      0.9595 |      2.724  |      0.3501 |             0.7217 |                0.0987 |                          0 |            0.838  |            10.822  |
| mssa:no_rw      |       0.6 |      0.5689 |     0.0108 |     0.4521 |      0.9388 |      2.1147 |      0.3156 |             0.707  |                0.0941 |                          0 |            2.7267 |            14.855  |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3477 |     0.0015 |     0.2401 |      0.9292 |      1.2865 |      0.1815 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.4134 |     0.0016 |     0.2987 |      0.9337 |      1.5308 |      0.2203 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.4914 |     0.0031 |     0.364  |      0.9261 |      1.7483 |      0.2648 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.5802 |     0.0095 |     0.4315 |      0.9239 |      2.0071 |      0.313  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3579 |     0.0031 |     0.2502 |      0.9286 |      1.3201 |      0.1879 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4406 |     0.0111 |     0.3237 |      0.9397 |      1.7219 |      0.2383 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.5406 |     0.0235 |     0.4062 |      0.9354 |      2.0563 |      0.2952 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.6631 |     0.0452 |     0.4994 |      0.9282 |      2.4053 |      0.3619 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3475 |     0.0017 |     0.2402 |      0.9292 |      1.295  |      0.1816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.4132 |     0.0019 |     0.2991 |      0.9349 |      1.5509 |      0.2204 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.4919 |     0.005  |     0.366  |      0.9293 |      1.7792 |      0.2656 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.5786 |     0.0077 |     0.4321 |      0.9292 |      2.0496 |      0.3129 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3495 |     0.0015 |     0.2419 |      0.9289 |      1.3002 |      0.1826 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.4174 |     0.0014 |     0.3024 |      0.9343 |      1.5614 |      0.2224 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.4984 |     0.0029 |     0.3695 |      0.9274 |      1.7945 |      0.2683 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.5848 |     0.006  |     0.435  |      0.9263 |      2.0701 |      0.3149 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3472 |     0.0024 |     0.2396 |      0.9262 |      1.2695 |      0.1812 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.413  |     0.0019 |     0.299  |      0.9336 |      1.5179 |      0.2204 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.4939 |     0.0021 |     0.3671 |      0.9216 |      1.7421 |      0.2669 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.592  |     0.009  |     0.4428 |      0.9142 |      2.0069 |      0.3206 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.347  |     0.0003 |     0.2401 |      0.9279 |      1.3009 |      0.1818 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.4124 |     0.0012 |     0.2986 |      0.9305 |      1.5319 |      0.2201 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.4921 |     0.0022 |     0.3679 |      0.9244 |      1.7423 |      0.2667 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.5829 |     0.0077 |     0.4377 |      0.9175 |      2.0062 |      0.3162 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         1 |      0.3602 |     0.003  |     0.2536 |      0.9205 |      1.298  |      0.1904 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         3 |      0.4466 |     0.0091 |     0.3282 |      0.9071 |      1.5105 |      0.2411 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         6 |      0.549  |     0.0181 |     0.4108 |      0.8772 |      1.6777 |      0.3007 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |        12 |      0.6654 |     0.0316 |     0.4979 |      0.8531 |      1.8427 |      0.367  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.3581 |     0.004  |     0.2516 |      0.9375 |      1.4019 |      0.1898 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.4243 |     0.0013 |     0.3117 |      0.9306 |      1.5499 |      0.2283 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.5062 |     0.0056 |     0.386  |      0.9266 |      1.7514 |      0.2772 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.6019 |     0.0127 |     0.465  |      0.9231 |      2.0961 |      0.3306 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         1 |      0.3507 |     0.0012 |     0.2455 |      0.9339 |      1.3211 |      0.1843 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         3 |      0.4223 |     0.0043 |     0.311  |      0.9336 |      1.593  |      0.2272 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         6 |      0.5075 |     0.0092 |     0.3832 |      0.9286 |      1.8169 |      0.2766 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |        12 |      0.6042 |     0.0151 |     0.4574 |      0.9195 |      2.0409 |      0.3301 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3477 |     0.0015 |     0.2401 |      0.9292 |      1.2865 |      0.1815 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.38   |     0.0033 |     0.2692 |      0.9256 |      1.3802 |      0.201  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.4233 |     0.0065 |     0.3082 |      0.9201 |      1.5083 |      0.2273 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.4936 |     0.012  |     0.3647 |      0.9103 |      1.6871 |      0.2665 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3579 |     0.0031 |     0.2502 |      0.9286 |      1.3201 |      0.1879 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3967 |     0.0072 |     0.2856 |      0.93   |      1.4516 |      0.2115 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4586 |     0.018  |     0.3415 |      0.929  |      1.6375 |      0.2487 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.5622 |     0.0382 |     0.4244 |      0.9156 |      1.8872 |      0.3071 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3475 |     0.0017 |     0.2402 |      0.9292 |      1.295  |      0.1816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.3803 |     0.0038 |     0.2692 |      0.9257 |      1.3918 |      0.2012 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.4232 |     0.005  |     0.3074 |      0.9204 |      1.5246 |      0.2271 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.4907 |     0.0076 |     0.3614 |      0.9162 |      1.7105 |      0.2645 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3495 |     0.0015 |     0.2419 |      0.9289 |      1.3002 |      0.1826 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.3827 |     0.0035 |     0.2717 |      0.9263 |      1.3981 |      0.2024 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.4252 |     0.0051 |     0.3099 |      0.9237 |      1.5342 |      0.2282 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.4952 |     0.0064 |     0.3652 |      0.9177 |      1.7253 |      0.2667 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3472 |     0.0024 |     0.2396 |      0.9262 |      1.2695 |      0.1812 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.3783 |     0.0041 |     0.2674 |      0.9223 |      1.364  |      0.1999 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.4217 |     0.0035 |     0.3071 |      0.9195 |      1.4934 |      0.2264 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.4886 |     0.0051 |     0.3597 |      0.91   |      1.6746 |      0.2632 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.347  |     0.0003 |     0.2401 |      0.9279 |      1.3009 |      0.1818 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.3742 |     0.0005 |     0.265  |      0.931  |      1.3914 |      0.1982 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4152 |     0.0028 |     0.2998 |      0.9256 |      1.5154 |      0.2219 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.4766 |     0.0037 |     0.3429 |      0.9255 |      1.691  |      0.2526 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         1 |      0.3602 |     0.003  |     0.2536 |      0.9205 |      1.298  |      0.1904 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         2 |      0.3952 |     0.0049 |     0.2849 |      0.9138 |      1.3761 |      0.2116 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         4 |      0.4512 |     0.0087 |     0.3314 |      0.8993 |      1.485  |      0.2439 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         8 |      0.5358 |     0.0181 |     0.3955 |      0.8823 |      1.6221 |      0.2905 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.3581 |     0.004  |     0.2516 |      0.9375 |      1.4019 |      0.1898 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.3905 |     0.0036 |     0.2807 |      0.9348 |      1.484  |      0.2087 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.4249 |     0.0026 |     0.3114 |      0.9311 |      1.5987 |      0.2295 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.4817 |     0.0052 |     0.3588 |      0.9322 |      1.7693 |      0.2603 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         1 |      0.3507 |     0.0012 |     0.2455 |      0.9339 |      1.3211 |      0.1843 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         2 |      0.387  |     0.0027 |     0.2786 |      0.9288 |      1.4219 |      0.2066 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         4 |      0.4423 |     0.0054 |     0.326  |      0.9133 |      1.5581 |      0.2399 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         8 |      0.5255 |     0.0103 |     0.3904 |      0.8945 |      1.7403 |      0.286  |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.3573 |     0.0029 |     0.2547 |      0.9196 |      1.3133 |      0.1911 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.4031 |     0.0063 |     0.2947 |      0.9234 |      1.4594 |      0.2173 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.4749 |     0.0111 |     0.3528 |      0.9125 |      1.6547 |      0.2576 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3697 |     0.0047 |     0.268  |      0.9239 |      1.3385 |      0.1988 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4337 |     0.0164 |     0.3228 |      0.9292 |      1.5573 |      0.2355 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.5389 |     0.0376 |     0.4088 |      0.9176 |      1.8373 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.3574 |     0.0033 |     0.2541 |      0.9209 |      1.3215 |      0.191  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.4019 |     0.005  |     0.2933 |      0.9227 |      1.4732 |      0.2166 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.4713 |     0.0082 |     0.3493 |      0.9184 |      1.6764 |      0.2553 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.359  |     0.0027 |     0.2553 |      0.9217 |      1.3254 |      0.1917 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.4033 |     0.0052 |     0.2949 |      0.9253 |      1.4808 |      0.2173 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.4753 |     0.0069 |     0.3523 |      0.9202 |      1.6895 |      0.2572 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.3545 |     0.0039 |     0.2524 |      0.9176 |      1.2961 |      0.1896 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.4024 |     0.0032 |     0.2938 |      0.9212 |      1.4437 |      0.2168 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.4692 |     0.005  |     0.3471 |      0.9117 |      1.6415 |      0.2541 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.3555 |     0.0003 |     0.2521 |      0.9265 |      1.3283 |      0.1897 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.3992 |     0.0033 |     0.2872 |      0.9263 |      1.4691 |      0.2134 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.4577 |     0.0039 |     0.3307 |      0.9282 |      1.6598 |      0.2438 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         2 |      0.3687 |     0.0031 |     0.2669 |      0.9169 |      1.3165 |      0.1987 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         4 |      0.4298 |     0.0076 |     0.3154 |      0.9025 |      1.4445 |      0.2326 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rate    |         8 |      0.5149 |     0.0171 |     0.3807 |      0.8864 |      1.5981 |      0.2796 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.371  |     0.0033 |     0.2676 |      0.9351 |      1.4475 |      0.2001 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.4066 |     0.0032 |     0.2991 |      0.9339 |      1.565  |      0.2207 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.4641 |     0.0046 |     0.3489 |      0.9334 |      1.7394 |      0.2527 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         2 |      0.3626 |     0.0021 |     0.2616 |      0.9248 |      1.3465 |      0.1951 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         4 |      0.4199 |     0.0058 |     0.3102 |      0.9184 |      1.5047 |      0.2283 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rw      |         8 |      0.506  |     0.01   |     0.3771 |      0.8969 |      1.7073 |      0.2761 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |   frac_increase_at_end |
|:-------------|:-----------|----------------:|----------------:|-------------:|-----------------------:|
| gbm_residual | load_x2    |          0.9409 |          0.0557 |       0.1553 |                 0.7467 |
| gbm_residual | temp_plus5 |          0.7843 |          0.2157 |       0.056  |                 0.92   |
| jtg_enkf     | load_x2    |          1      |          0      |       1.046  |                 1      |
| jtg_enkf     | temp_plus5 |          1      |          0      |       5.2039 |                 1      |
| jtg_global   | load_x2    |          1      |          0      |       0.7801 |                 1      |
| jtg_global   | temp_plus5 |          1      |          0      |       4.001  |                 1      |
| lstm         | load_x2    |          0.8588 |          0.1412 |       0.4315 |                 0.7867 |
| lstm         | temp_plus5 |          0.4843 |          0.5157 |      -0.0143 |                 0.1733 |
| mssa         | load_x2    |          1      |          0      |       0.7797 |                 1      |
| mssa         | temp_plus5 |          1      |          0      |       1.8629 |                 1      |
| patchtst     | load_x2    |          0.7234 |          0.2766 |       0.197  |                 0.76   |
| patchtst     | temp_plus5 |          0.6139 |          0.3861 |       0.0204 |                 0.3333 |
| persistence  | load_x2    |          0      |          0      |       0      |                 0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |                 0      |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |   frac_increase_at_end |
|:-------------|:-----------|----------------:|----------------:|-------------:|-----------------------:|
| gbm_residual | load_x2    |          0.908  |          0.0896 |       0.1338 |                 0.7857 |
| gbm_residual | temp_plus5 |          0.7833 |          0.2165 |       0.0534 |                 0.8429 |
| jtg_enkf     | load_x2    |          1      |          0      |       0.9984 |                 1      |
| jtg_enkf     | temp_plus5 |          1      |          0      |       4.2686 |                 1      |
| lstm         | load_x2    |          0.8426 |          0.1574 |       0.3855 |                 0.7857 |
| lstm         | temp_plus5 |          0.467  |          0.533  |      -0.0156 |                 0.1714 |
| mssa         | load_x2    |          1      |          0      |       0.7553 |                 1      |
| mssa         | temp_plus5 |          1      |          0      |       1.7932 |                 1      |
| patchtst     | load_x2    |          0.6981 |          0.3019 |       0.1467 |                 0.8071 |
| patchtst     | temp_plus5 |          0.6214 |          0.3786 |       0.0245 |                 0.3548 |
| persistence  | load_x2    |          0      |          0      |       0      |                 0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |                 0      |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |   frac_increase_at_end |
|:----------------|:-----------|----------------:|----------------:|-------------:|-----------------------:|
| mssa:fixed_mat  | load_x2    |          1      |          0      |       0.794  |                 1      |
| mssa:fixed_mat  | temp_plus5 |          1      |          0      |       1.8368 |                 1      |
| mssa:neural_ssm | load_x2    |          0.7049 |          0.2951 |       0.2179 |                 0.7333 |
| mssa:neural_ssm | temp_plus5 |          1      |          0      |       0.466  |                 1      |
| mssa:no_defl    | load_x2    |          1      |          0      |       0.7425 |                 1      |
| mssa:no_defl    | temp_plus5 |          1      |          0      |       2.0501 |                 1      |
| mssa:no_disc    | load_x2    |          1      |          0      |       0.8265 |                 1      |
| mssa:no_disc    | temp_plus5 |          1      |          0      |       1.8978 |                 1      |
| mssa:no_ms      | load_x2    |          1      |          0      |       0.6933 |                 1      |
| mssa:no_ms      | temp_plus5 |          1      |          0      |       2.196  |                 1      |
| mssa:no_proj    | load_x2    |          1      |          0      |       0.8921 |                 1      |
| mssa:no_proj    | temp_plus5 |          1      |          0      |       1.9638 |                 1      |
| mssa:no_rate    | load_x2    |          1      |          0      |       0.8193 |                 1      |
| mssa:no_rate    | temp_plus5 |          1      |          0      |       1.6921 |                 1      |
| mssa:no_rev     | load_x2    |          1      |          0      |       0.7567 |                 1      |
| mssa:no_rev     | temp_plus5 |          1      |          0      |       2.3532 |                 1      |
| mssa:no_rw      | load_x2    |          1      |          0      |       0.6587 |                 1      |
| mssa:no_rw      | temp_plus5 |          1      |          0      |       1.7852 |                 1      |

## Native vs ACI intervals [E1E2]

| model        | setting   |   PICP |   MPIW |     IS |
|:-------------|:----------|-------:|-------:|-------:|
| fusion       | aci       | 0.9633 | 1.6415 | 1.9926 |
| fusion       | native    | 0.9533 | 1.365  | 1.8582 |
| gbm_ens      | aci       | 0.9595 | 1.7029 | 2.0854 |
| gbm_ens      | native    | 0.9223 | 1.2611 | 2.1596 |
| gbm_residual | aci       | 0.9591 | 1.7265 | 2.1066 |
| gbm_residual | native    | 0.9187 | 1.2501 | 2.1869 |
| jtg_enkf     | aci       | 0.9573 | 2.0693 | 2.508  |
| jtg_enkf     | native    | 0.723  | 0.8359 | 3.7425 |
| mssa         | aci       | 0.9645 | 1.8715 | 2.2521 |
| mssa         | native    | 0.9246 | 1.2809 | 2.1978 |
| mssa_ens     | aci       | 0.9643 | 1.8471 | 2.2542 |
| mssa_ens     | native    | 0.927  | 1.2922 | 2.1557 |

## Native vs ACI intervals [E3]

| model        | setting   |   PICP |   MPIW |     IS |
|:-------------|:----------|-------:|-------:|-------:|
| fusion       | aci       | 0.9646 | 1.7118 | 2.0609 |
| fusion       | native    | 0.947  | 1.4177 | 1.9522 |
| gbm_ens      | aci       | 0.9609 | 1.8393 | 2.186  |
| gbm_ens      | native    | 0.8871 | 1.2589 | 2.5768 |
| gbm_residual | aci       | 0.9607 | 1.8761 | 2.2207 |
| gbm_residual | native    | 0.8802 | 1.2446 | 2.6252 |
| jtg_enkf     | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf     | native    | 0.7276 | 0.8364 | 3.805  |
| mssa         | aci       | 0.9632 | 1.8278 | 2.1939 |
| mssa         | native    | 0.9249 | 1.2975 | 2.1574 |
| mssa_ens     | aci       | 0.9621 | 1.8268 | 2.1912 |
| mssa_ens     | native    | 0.9268 | 1.3015 | 2.1408 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.9641 | 1.8743 | 2.2575 |
| mssa:fixed_mat  | native    | 0.9248 | 1.283  | 2.1939 |
| mssa:neural_ssm | aci       | 0.9693 | 1.8632 | 2.2    |
| mssa:neural_ssm | native    | 0.9253 | 1.32   | 2.212  |
| mssa:no_defl    | aci       | 0.9638 | 1.866  | 2.258  |
| mssa:no_defl    | native    | 0.9244 | 1.2911 | 2.1866 |
| mssa:no_disc    | aci       | 0.9635 | 1.8724 | 2.2601 |
| mssa:no_disc    | native    | 0.9242 | 1.2925 | 2.1859 |
| mssa:no_ms      | aci       | 0.9639 | 1.8798 | 2.2592 |
| mssa:no_ms      | native    | 0.9214 | 1.264  | 2.1997 |
| mssa:no_proj    | aci       | 0.9661 | 1.8453 | 2.2208 |
| mssa:no_proj    | native    | 0.9233 | 1.2977 | 2.1735 |
| mssa:no_rate    | aci       | 0.9655 | 1.8693 | 2.2264 |
| mssa:no_rate    | native    | 0.9168 | 1.2929 | 2.234  |
| mssa:no_rev     | aci       | 0.9636 | 1.8944 | 2.2786 |
| mssa:no_rev     | native    | 0.9331 | 1.3985 | 2.1758 |
| mssa:no_rw      | aci       | 0.9646 | 1.8607 | 2.2403 |
| mssa:no_rw      | native    | 0.9294 | 1.3185 | 2.1651 |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.9155 |                 6.9377 |
|    0.2 |          10 |           0.6128 |                12.9172 |
|    0.4 |           8 |           0.6524 |                 7.4775 |
|    0.4 |          10 |           0.4763 |                 3.9412 |
|    0.6 |           8 |           0.4636 |                 2.453  |
|    0.6 |          10 |           0.2794 |                 4.9153 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.8862 |                 8.2607 |
|    0.2 |          10 |           0.5567 |                10.7073 |
|    0.4 |           8 |           0.6035 |                 8.9096 |
|    0.4 |          10 |           0.463  |                 8.9535 |
|    0.6 |           8 |           0.4483 |                 5.907  |
|    0.6 |          10 |           0.2452 |                 2.0075 |

## E0 synthetic identifiability

| exp   |   seed |   sig_m_true |   beta_true |   beta_hat |   gamma_true |   gamma_hat |   phi_true |   phi_hat |   sig_m_hat |   sig_r_true |   sig_r_hat |   u_spearman |   u_rmse |   Rperm_rmse |   rev_rmse |   rev_sd_true |
|:------|-------:|-------------:|------------:|-----------:|-------------:|------------:|-----------:|----------:|------------:|-------------:|------------:|-------------:|---------:|-------------:|-----------:|--------------:|
| E0    |      0 |          0.1 |         0.4 |     0.3976 |          3.2 |      3.2884 |        0.6 |    0.6354 |      0.1035 |         0.08 |      0.0662 |       0.3566 |   0.1436 |       0.0559 |     0.0805 |        0.2982 |
| E0    |      0 |          0.2 |         0.4 |     0.3972 |          3.2 |      3.2999 |        0.6 |    0.6436 |      0.1952 |         0.08 |      0.0725 |       0.3566 |   0.144  |       0.0722 |     0.0982 |        0.2982 |
| E0    |      1 |          0.1 |         0.4 |     0.3913 |          3.2 |      3.3225 |        0.6 |    0.6113 |      0.0968 |         0.08 |      0.0769 |       0.7972 |   0.1005 |       0.0505 |     0.0772 |        0.2941 |
| E0    |      1 |          0.2 |         0.4 |     0.3913 |          3.2 |      3.3256 |        0.6 |    0.6173 |      0.1901 |         0.08 |      0.084  |       0.7902 |   0.1068 |       0.0697 |     0.0977 |        0.2941 |
| E0    |      2 |          0.1 |         0.4 |     0.3957 |          3.2 |      3.3043 |        0.6 |    0.6242 |      0.1035 |         0.08 |      0.0742 |       0.4615 |   0.2143 |       0.0536 |     0.076  |        0.3005 |
| E0    |      2 |          0.2 |         0.4 |     0.3946 |          3.2 |      3.3287 |        0.6 |    0.6229 |      0.1966 |         0.08 |      0.0804 |       0.5524 |   0.2212 |       0.0658 |     0.0897 |        0.3005 |
| E0    |      3 |          0.1 |         0.4 |     0.4055 |          3.2 |      3.269  |        0.6 |    0.6045 |      0.1023 |         0.08 |      0.0769 |       0.5804 |   0.2983 |       0.0561 |     0.0811 |        0.2966 |
| E0    |      3 |          0.2 |         0.4 |     0.4072 |          3.2 |      3.2666 |        0.6 |    0.6176 |      0.1955 |         0.08 |      0.0855 |       0.4545 |   0.3148 |       0.0662 |     0.0951 |        0.2966 |
| E0    |      4 |          0.1 |         0.4 |     0.4004 |          3.2 |      3.3072 |        0.6 |    0.6325 |      0.0975 |         0.08 |      0.0732 |       0.7413 |   0.2035 |       0.0526 |     0.0738 |        0.2978 |
| E0    |      4 |          0.2 |         0.4 |     0.3931 |          3.2 |      3.3316 |        0.6 |    0.6297 |      0.192  |         0.08 |      0.0832 |       0.7413 |   0.1974 |       0.064  |     0.0881 |        0.2978 |

## E5 learned parameters

| exp   |   seed |   beta_hat |   gamma_hat |   wu_load_exp_min |   wu_load_exp_max |   wu_temp_exp_min |   wu_temp_exp_max |   R0eff_Surf_AC13_I_SBS |   R0eff_Surf_AC13_II_SBS |   R0eff_Surf_SMA13 |   R0eff_Surf_PAC13 |   R0eff_Mid_AC20_AH30 |   R0eff_Mid_AC20_SBS |   R0eff_Mid_AC20_AH50 |   R0eff_Bot_AC25_AH30 |   R0eff_Bot_AC25_AH50 |   R0eff_Bot_AC25_AH70 |   R0eff_Bot_AC25_Re_AH70 |   R0eff_Bot_AC10_SBS |   scale_I_SemiRigid_12cmAC |   scale_II_RigidComposite_12cmAC |   scale_III_SemiRigid_16_18cmAC |   scale_IV_Inverted_24_28cmAC |   scale_V_ThickAC_I_24_28cm |   scale_VI_ThickAC_II_36cm |   scale_VII_FullDepth_48_52cm |
|:------|-------:|-----------:|------------:|------------------:|------------------:|------------------:|------------------:|------------------------:|-------------------------:|-------------------:|-------------------:|----------------------:|---------------------:|----------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|---------------------:|---------------------------:|---------------------------------:|--------------------------------:|------------------------------:|----------------------------:|---------------------------:|------------------------------:|
| E5    |      0 |     0.3597 |      3.588  |             0.176 |             0.292 |             3.499 |             3.735 |                  1.6866 |                   1.6222 |             1.8076 |             1.8637 |                1.5375 |               1.5796 |                2.6547 |                1.6076 |                2.2182 |                3.0888 |                   1.9906 |               2.3121 |                     0.422  |                           0.299  |                          0.4412 |                        0.5071 |                      0.4575 |                     0.416  |                        0.4103 |
| E5    |      1 |     0.3746 |      3.549  |             0.176 |             0.292 |             3.499 |             3.735 |                  1.6327 |                   1.5959 |             1.8156 |             1.8938 |                1.6157 |               1.7058 |                2.4865 |                1.7838 |                2.1607 |                2.8805 |                   1.9995 |               2.3589 |                     0.4218 |                           0.316  |                          0.4046 |                        0.4523 |                      0.4323 |                     0.4127 |                        0.3754 |
| E5    |      2 |     0.3642 |      3.5579 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.6612 |                   1.6463 |             1.771  |             1.9078 |                1.4939 |               1.5185 |                2.5508 |                1.8878 |                2.1627 |                2.946  |                   2.0577 |               2.3361 |                     0.4015 |                           0.3186 |                          0.4606 |                        0.5233 |                      0.4661 |                     0.422  |                        0.3922 |
| E5    |      3 |     0.3706 |      3.5541 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.6395 |                   1.6651 |             1.8031 |             1.8784 |                1.5408 |               1.5898 |                2.5074 |                1.6719 |                2.2482 |                3.0373 |                   2.1003 |               2.3291 |                     0.4026 |                           0.3124 |                          0.4479 |                        0.5027 |                      0.4566 |                     0.4047 |                        0.4055 |
| E5    |      4 |     0.3595 |      3.5566 |             0.176 |             0.292 |             3.499 |             3.735 |                  1.6436 |                   1.6628 |             1.8016 |             1.8264 |                1.4383 |               1.5607 |                2.8345 |                1.7447 |                2.1318 |                3.0626 |                   2.0417 |               2.3205 |                     0.4246 |                           0.3229 |                          0.4582 |                        0.5263 |                      0.4669 |                     0.4305 |                        0.4708 |

## E5 hidden-material recovery

|   seed |   spearman |   n |
|-------:|-----------:|----:|
|      0 |    -0.2242 |  10 |
|      1 |    -0.1394 |  10 |
|      2 |    -0.2727 |  10 |
|      3 |    -0.3818 |  10 |
|      4 |    -0.1879 |  10 |

## E5 H1 discrepancy test

|   seed |   mean_abs_g_II_VII |   mean_abs_g_others |   U |   p_one_sided |
|-------:|--------------------:|--------------------:|----:|--------------:|
|      0 |              1.3559 |              1.3123 |  35 |        0.3323 |
|      1 |              1.1271 |              1.186  |  31 |        0.4807 |
|      2 |              1.3095 |              1.2466 |  40 |        0.1785 |
|      3 |              1.2742 |              1.1588 |  45 |        0.0761 |
|      4 |              1.3988 |              1.3334 |  44 |        0.0924 |
