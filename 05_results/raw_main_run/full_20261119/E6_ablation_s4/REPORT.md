# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E6_ablation_s4`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.3139 |        nan |     1.0434 |      0.6503 |      2.5202 |      0.808  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      1.8483 |        nan |     1.5142 |      0.7614 |      4.4064 |      1.1034 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.1425 |        nan |     0.9007 |      0.7031 |      2.4653 |      0.6881 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.384  |        nan |     1.1028 |      0.6196 |      2.5302 |      0.8685 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.2696 |        nan |     0.9731 |      0.6687 |      2.624  |      0.7568 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.2986 |        nan |     1.0444 |      0.6664 |      2.4735 |      0.8005 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.3104 |        nan |     1.0571 |      0.6774 |      2.5234 |      0.8063 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.2286 |        nan |     0.983  |      0.5891 |      2.0196 |      0.773  |             1.2531 |                0.0747 |                          0 |           10.6367 |            nan     |
| mssa:fixed_mat  |       0.4 |      1.0087 |        nan |     0.8087 |      0.6275 |      1.9651 |      0.6233 |             1.0197 |                0.0881 |                          0 |            7.9633 |             12.655 |
| mssa:fixed_mat  |       0.6 |      0.7306 |        nan |     0.5874 |      0.7991 |      1.8879 |      0.4275 |             0.7536 |                0.0851 |                          0 |            1.56   |            nan     |
| mssa:neural_ssm |       0.2 |      1.4571 |        nan |     1.0603 |      0.7513 |      3.137  |      0.8205 |             1.2913 |                0.1358 |                          0 |           14.592  |            nan     |
| mssa:neural_ssm |       0.4 |      0.9663 |        nan |     0.7329 |      0.9023 |      2.9719 |      0.5376 |             0.8785 |                0.1513 |                          0 |            9.7567 |             11.75  |
| mssa:neural_ssm |       0.6 |      0.7488 |        nan |     0.5598 |      0.9247 |      2.7992 |      0.4082 |             0.7415 |                0.1684 |                          0 |            2.7    |              1.94  |
| mssa:no_defl    |       0.2 |      1.1508 |        nan |     0.9123 |      0.5994 |      1.9263 |      0.7245 |             1.1468 |                0.0457 |                          0 |           12.1738 |              2.72  |
| mssa:no_defl    |       0.4 |      0.97   |        nan |     0.7624 |      0.6466 |      1.8804 |      0.5997 |             0.9022 |                0.0626 |                          0 |            3.9067 |             12.825 |
| mssa:no_defl    |       0.6 |      0.7022 |        nan |     0.5262 |      0.7477 |      1.8021 |      0.4048 |             0.6292 |                0.043  |                          0 |            1.17   |              2.32  |
| mssa:no_disc    |       0.2 |      1.2375 |        nan |     0.9832 |      0.5112 |      1.737  |      0.7996 |             1.2581 |                0.0353 |                          0 |           15.3838 |            nan     |
| mssa:no_disc    |       0.4 |      0.9974 |        nan |     0.8184 |      0.542  |      1.6972 |      0.6441 |             1.0257 |                0.0501 |                          0 |            4.4633 |            nan     |
| mssa:no_disc    |       0.6 |      0.7376 |        nan |     0.582  |      0.637  |      1.6156 |      0.4504 |             0.7281 |                0.0313 |                          0 |            1.17   |            nan     |
| mssa:no_ms      |       0.2 |      1.1058 |        nan |     0.8654 |      0.5782 |      1.6803 |      0.701  |             1.0648 |                0.0671 |                          0 |           10.1838 |            nan     |
| mssa:no_ms      |       0.4 |      0.8785 |        nan |     0.687  |      0.6069 |      1.6381 |      0.5497 |             0.8035 |                0.0664 |                          0 |            3.8467 |             12.245 |
| mssa:no_ms      |       0.6 |      0.6276 |        nan |     0.4983 |      0.7432 |      1.5623 |      0.3746 |             0.5863 |                0.0372 |                          0 |            0.79   |              6.79  |
| mssa:no_proj    |       0.2 |      1.1375 |        nan |     0.938  |      0.486  |      1.7045 |      0.745  |             1.2256 |                0.0475 |                          0 |           17.9162 |            nan     |
| mssa:no_proj    |       0.4 |      0.9293 |        nan |     0.7838 |      0.5374 |      1.6579 |      0.6047 |             0.9746 |                0.0541 |                          0 |            7.62   |             21.77  |
| mssa:no_proj    |       0.6 |      0.6612 |        nan |     0.5374 |      0.7295 |      1.585  |      0.4006 |             0.6565 |                0.0338 |                          0 |            1.94   |             14.19  |
| mssa:no_rev     |       0.2 |      1.2286 |        nan |     1.0044 |      0.5054 |      1.7639 |      0.8082 |             1.2917 |                0      |                          0 |           17.4557 |            nan     |
| mssa:no_rev     |       0.4 |      0.9985 |        nan |     0.8228 |      0.5763 |      1.7373 |      0.6403 |             0.9896 |                0      |                          0 |            6.675  |            nan     |
| mssa:no_rev     |       0.6 |      0.6491 |        nan |     0.5204 |      0.8025 |      1.6591 |      0.3801 |             0.6139 |                0      |                          0 |          nan      |            nan     |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3702 |        nan |     0.2723 |      0.9288 |      1.3669 |      0.1997 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.471  |        nan |     0.3677 |      0.9166 |      1.5845 |      0.2626 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.5886 |        nan |     0.4685 |      0.8731 |      1.738  |      0.3362 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.7202 |        nan |     0.5762 |      0.7989 |      1.8524 |      0.4207 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3674 |        nan |     0.262  |      0.9288 |      1.3735 |      0.1957 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4691 |        nan |     0.351  |      0.9386 |      1.8239 |      0.2564 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.6031 |        nan |     0.4583 |      0.9282 |      2.2085 |      0.3308 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.7754 |        nan |     0.5917 |      0.9135 |      2.5912 |      0.4264 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3755 |        nan |     0.276  |      0.9002 |      1.2695 |      0.2038 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.4722 |        nan |     0.3666 |      0.8758 |      1.486  |      0.2667 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.5811 |        nan |     0.4578 |      0.8224 |      1.6414 |      0.3363 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.7017 |        nan |     0.5476 |      0.7589 |      1.7602 |      0.4118 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.391  |        nan |     0.2903 |      0.8586 |      1.1695 |      0.216  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.499  |        nan |     0.388  |      0.8196 |      1.3467 |      0.2869 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6172 |        nan |     0.4869 |      0.7573 |      1.4732 |      0.3646 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.758  |        nan |     0.5989 |      0.6738 |      1.5727 |      0.4584 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.388  |        nan |     0.2875 |      0.8831 |      1.1885 |      0.212  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.4866 |        nan |     0.3745 |      0.8252 |      1.333  |      0.2764 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.5882 |        nan |     0.4595 |      0.7774 |      1.4323 |      0.3431 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.7004 |        nan |     0.5459 |      0.7199 |      1.5114 |      0.4158 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3722 |        nan |     0.2732 |      0.8951 |      1.2236 |      0.2018 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.4643 |        nan |     0.3546 |      0.8679 |      1.3655 |      0.2593 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.565  |        nan |     0.4387 |      0.8167 |      1.4611 |      0.3233 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.6765 |        nan |     0.5281 |      0.7494 |      1.5351 |      0.3963 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5027 |        nan |     0.3992 |      0.8872 |      1.5784 |      0.2861 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.5444 |        nan |     0.4355 |      0.8618 |      1.5903 |      0.313  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.5963 |        nan |     0.4789 |      0.8181 |      1.6069 |      0.3467 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.6698 |        nan |     0.535  |      0.7734 |      1.6323 |      0.3942 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3702 |        nan |     0.2723 |      0.9288 |      1.3669 |      0.1997 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4173 |        nan |     0.3164 |      0.9191 |      1.4457 |      0.2285 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.4927 |        nan |     0.3827 |      0.902  |      1.5522 |      0.2748 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.6071 |        nan |     0.4785 |      0.8466 |      1.677  |      0.3457 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3674 |        nan |     0.262  |      0.9288 |      1.3735 |      0.1957 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4143 |        nan |     0.3028 |      0.9302 |      1.5172 |      0.223  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4931 |        nan |     0.3703 |      0.9251 |      1.7238 |      0.2674 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6193 |        nan |     0.4642 |      0.9168 |      1.9985 |      0.335  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3755 |        nan |     0.276  |      0.9002 |      1.2695 |      0.2038 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4243 |        nan |     0.3195 |      0.8789 |      1.3509 |      0.2352 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.4954 |        nan |     0.3812 |      0.847  |      1.4556 |      0.28   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6085 |        nan |     0.4711 |      0.7888 |      1.5791 |      0.351  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.391  |        nan |     0.2903 |      0.8586 |      1.1695 |      0.216  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4456 |        nan |     0.3398 |      0.8272 |      1.2386 |      0.2524 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5318 |        nan |     0.4142 |      0.7805 |      1.3271 |      0.3096 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6562 |        nan |     0.5136 |      0.7093 |      1.4335 |      0.3906 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.388  |        nan |     0.2875 |      0.8831 |      1.1885 |      0.212  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4372 |        nan |     0.3325 |      0.8461 |      1.2496 |      0.245  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5114 |        nan |     0.3961 |      0.8059 |      1.3257 |      0.294  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6132 |        nan |     0.474  |      0.7408 |      1.4176 |      0.3592 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3722 |        nan |     0.2732 |      0.8951 |      1.2236 |      0.2018 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4163 |        nan |     0.3129 |      0.8854 |      1.2816 |      0.2291 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4896 |        nan |     0.3742 |      0.8503 |      1.3561 |      0.2741 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.5824 |        nan |     0.4496 |      0.8004 |      1.4447 |      0.3328 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5027 |        nan |     0.3992 |      0.8872 |      1.5784 |      0.2861 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5426 |        nan |     0.4319 |      0.8558 |      1.6067 |      0.3119 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6018 |        nan |     0.4803 |      0.8175 |      1.6471 |      0.3505 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.6863 |        nan |     0.5489 |      0.7583 |      1.7029 |      0.4063 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.3884 |        nan |     0.2933 |      0.9189 |      1.3836 |      0.2131 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.4681 |        nan |     0.3613 |      0.9028 |      1.5119 |      0.26   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.5848 |        nan |     0.4609 |      0.8544 |      1.6556 |      0.332  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3852 |        nan |     0.2826 |      0.9281 |      1.3916 |      0.2082 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4672 |        nan |     0.3488 |      0.9243 |      1.6337 |      0.2533 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.593  |        nan |     0.4453 |      0.9203 |      1.9425 |      0.3209 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.3967 |        nan |     0.2973 |      0.8839 |      1.2896 |      0.2196 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.4717 |        nan |     0.3604 |      0.8529 |      1.4153 |      0.2653 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.5876 |        nan |     0.4548 |      0.7958 |      1.5574 |      0.338  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4145 |        nan |     0.3157 |      0.8359 |      1.1885 |      0.2342 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5104 |        nan |     0.3951 |      0.7883 |      1.2945 |      0.2953 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.637  |        nan |     0.498  |      0.7172 |      1.4157 |      0.3778 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.407  |        nan |     0.3087 |      0.8507 |      1.2089 |      0.2278 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.4926 |        nan |     0.379  |      0.8154 |      1.2999 |      0.2816 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.5964 |        nan |     0.4608 |      0.7467 |      1.4036 |      0.3487 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.3905 |        nan |     0.2939 |      0.8894 |      1.2413 |      0.215  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4735 |        nan |     0.3596 |      0.8554 |      1.3307 |      0.2636 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.5655 |        nan |     0.4357 |      0.8079 |      1.4313 |      0.322  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5233 |        nan |     0.4164 |      0.8627 |      1.603  |      0.3009 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.5908 |        nan |     0.4705 |      0.8222 |      1.6434 |      0.3434 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.675  |        nan |     0.5394 |      0.7631 |      1.6997 |      0.399  |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.5025 |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.9416 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.46   |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       0.9479 |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.5294 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.989  |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.4923 |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.8653 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.5208 |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.81   |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.4649 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.7786 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3582 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       0.8696 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.9648 | 1.8564 | 2.2066 |
| mssa:fixed_mat  | native    | 0.9245 | 1.3553 | 2.1243 |
| mssa:neural_ssm | aci       | 0.9717 | 1.8286 | 2.1248 |
| mssa:neural_ssm | native    | 0.929  | 1.3726 | 2.1714 |
| mssa:no_defl    | aci       | 0.9633 | 1.8674 | 2.2502 |
| mssa:no_defl    | native    | 0.8938 | 1.2636 | 2.3076 |
| mssa:no_disc    | aci       | 0.9658 | 1.9022 | 2.2581 |
| mssa:no_disc    | native    | 0.8538 | 1.1632 | 2.5958 |
| mssa:no_ms      | aci       | 0.9648 | 1.9049 | 2.2821 |
| mssa:no_ms      | native    | 0.8768 | 1.1834 | 2.4841 |
| mssa:no_proj    | aci       | 0.9648 | 1.8605 | 2.1988 |
| mssa:no_proj    | native    | 0.8923 | 1.2168 | 2.2879 |
| mssa:no_rev     | aci       | 0.9534 | 2.1216 | 2.5513 |
| mssa:no_rev     | native    | 0.8812 | 1.5648 | 2.673  |
