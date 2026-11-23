# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E6_ablation_s3`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.9539 |        nan |     1.5369 |      0.5062 |      2.8873 |      1.2458 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      2.5193 |        nan |     1.9767 |      0.7402 |      4.9417 |      1.4417 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.7173 |        nan |     1.2661 |      0.6512 |      2.7055 |      1.0148 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.9345 |        nan |     1.5229 |      0.5223 |      2.9157 |      1.2416 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.5485 |        nan |     1.281  |      0.5365 |      2.7059 |      1.0063 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.8266 |        nan |     1.4888 |      0.48   |      2.4601 |      1.2079 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      2.0181 |        nan |     1.5751 |      0.5255 |      2.7612 |      1.2787 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.5716 |        nan |     1.2399 |      0.416  |      1.8206 |      1.03   |             1.5721 |                0.1043 |                          0 |           14.0883 |              1.55  |
| mssa:fixed_mat  |       0.4 |      1.1813 |        nan |     0.9445 |      0.5069 |      1.7727 |      0.7634 |             1.1619 |                0.1015 |                          0 |            5.265  |              2.72  |
| mssa:fixed_mat  |       0.6 |      0.7088 |        nan |     0.5593 |      0.7626 |      1.6944 |      0.4113 |             0.7384 |                0.077  |                          0 |          nan      |              1.94  |
| mssa:neural_ssm |       0.2 |      1.3521 |        nan |     1.0437 |      0.7725 |      3.1352 |      0.7765 |             1.3722 |                0.1615 |                          0 |           16.1043 |            nan     |
| mssa:neural_ssm |       0.4 |      0.9602 |        nan |     0.7619 |      0.9214 |      2.9761 |      0.5355 |             0.9998 |                0.178  |                          0 |            9.76   |             13.27  |
| mssa:neural_ssm |       0.6 |      0.7746 |        nan |     0.5804 |      0.9121 |      2.8063 |      0.4205 |             0.7697 |                0.1839 |                          0 |            3.19   |              1.17  |
| mssa:no_defl    |       0.2 |      1.5039 |        nan |     1.1398 |      0.5249 |      1.8408 |      0.9411 |             1.4535 |                0.124  |                          0 |           12.1    |              1.55  |
| mssa:no_defl    |       0.4 |      1.1504 |        nan |     0.9005 |      0.5595 |      1.797  |      0.7265 |             1.1025 |                0.1239 |                          0 |            8.3767 |              3.5   |
| mssa:no_defl    |       0.6 |      0.7237 |        nan |     0.5625 |      0.7865 |      1.7163 |      0.4179 |             0.7343 |                0.1224 |                          0 |            0.38   |              1.94  |
| mssa:no_disc    |       0.2 |      1.5245 |        nan |     1.1787 |      0.5272 |      2.0106 |      0.9583 |             1.4937 |                0.0708 |                          0 |           14.2767 |            nan     |
| mssa:no_disc    |       0.4 |      1.1663 |        nan |     0.9107 |      0.6244 |      1.9599 |      0.7186 |             1.1039 |                0.0822 |                          0 |            5.265  |            nan     |
| mssa:no_disc    |       0.6 |      0.7371 |        nan |     0.5833 |      0.8219 |      1.872  |      0.4207 |             0.7537 |                0.077  |                          0 |            2.34   |            nan     |
| mssa:no_ms      |       0.2 |      1.1176 |        nan |     0.9026 |      0.5203 |      1.6088 |      0.7236 |             1.0932 |                0.0697 |                          0 |           14.77   |              3.08  |
| mssa:no_ms      |       0.4 |      0.8076 |        nan |     0.6319 |      0.6435 |      1.57   |      0.487  |             0.7267 |                0.0846 |                          0 |            5.7    |             11.855 |
| mssa:no_ms      |       0.6 |      0.5765 |        nan |     0.4403 |      0.847  |      1.5034 |      0.3193 |             0.523  |                0.0608 |                          0 |            1.56   |              2.34  |
| mssa:no_proj    |       0.2 |      1.4494 |        nan |     1.1613 |      0.3805 |      1.4869 |      0.9736 |             1.3715 |                0.0418 |                          0 |           15.0029 |             15.93  |
| mssa:no_proj    |       0.4 |      1.1072 |        nan |     0.8863 |      0.4443 |      1.447  |      0.722  |             1.0328 |                0.0395 |                          0 |            0.78   |             12.255 |
| mssa:no_proj    |       0.6 |      0.7556 |        nan |     0.5925 |      0.6553 |      1.3816 |      0.4524 |             0.6967 |                0.028  |                          0 |            2.34   |              1.17  |
| mssa:no_rev     |       0.2 |      1.6463 |        nan |     1.242  |      0.392  |      1.4787 |      1.0645 |             1.5368 |                0      |                          0 |           12.0067 |            nan     |
| mssa:no_rev     |       0.4 |      1.2202 |        nan |     0.9322 |      0.4916 |      1.4543 |      0.7741 |             1.1509 |                0      |                          0 |            6.285  |            nan     |
| mssa:no_rev     |       0.6 |      0.7123 |        nan |     0.5588 |      0.6758 |      1.3655 |      0.4259 |             0.7115 |                0      |                          0 |            1.94   |            nan     |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.4106 |        nan |     0.305  |      0.8946 |      1.3151 |      0.2242 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.5446 |        nan |     0.4156 |      0.8374 |      1.4657 |      0.3056 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.6898 |        nan |     0.527  |      0.7827 |      1.569  |      0.3953 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.8569 |        nan |     0.6521 |      0.7064 |      1.6507 |      0.5018 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3699 |        nan |     0.2648 |      0.9348 |      1.3962 |      0.197  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4643 |        nan |     0.3495 |      0.9414 |      1.8481 |      0.255  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.5872 |        nan |     0.4521 |      0.9368 |      2.2285 |      0.3259 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.7431 |        nan |     0.58   |      0.922  |      2.601  |      0.4145 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3951 |        nan |     0.2922 |      0.9071 |      1.2982 |      0.2138 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.5148 |        nan |     0.3933 |      0.8613 |      1.4644 |      0.2873 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.6469 |        nan |     0.4981 |      0.8013 |      1.5803 |      0.3696 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.7967 |        nan |     0.6098 |      0.7314 |      1.6706 |      0.463  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3915 |        nan |     0.2849 |      0.8979 |      1.2888 |      0.2117 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.5194 |        nan |     0.3923 |      0.8627 |      1.5104 |      0.2877 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6676 |        nan |     0.5072 |      0.8186 |      1.6724 |      0.3766 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.8424 |        nan |     0.6353 |      0.7574 |      1.803  |      0.4829 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.388  |        nan |     0.2825 |      0.8794 |      1.161  |      0.2103 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.495  |        nan |     0.3723 |      0.8397 |      1.2969 |      0.2761 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.6077 |        nan |     0.4613 |      0.786  |      1.3868 |      0.3461 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.7371 |        nan |     0.5578 |      0.7284 |      1.4557 |      0.4267 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.4023 |        nan |     0.2953 |      0.8517 |      1.0918 |      0.2203 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.523  |        nan |     0.3957 |      0.7915 |      1.1982 |      0.2965 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.6524 |        nan |     0.4995 |      0.7276 |      1.2701 |      0.3808 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.8049 |        nan |     0.6181 |      0.6383 |      1.3292 |      0.484  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5735 |        nan |     0.4439 |      0.7426 |      1.2492 |      0.3353 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.6377 |        nan |     0.4923 |      0.701  |      1.2631 |      0.3763 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.7241 |        nan |     0.5524 |      0.6592 |      1.2829 |      0.4287 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.8579 |        nan |     0.6419 |      0.6063 |      1.3172 |      0.5092 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.4106 |        nan |     0.305  |      0.8946 |      1.3151 |      0.2242 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4672 |        nan |     0.3525 |      0.8711 |      1.3622 |      0.2586 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5705 |        nan |     0.436  |      0.8193 |      1.4441 |      0.3238 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.7184 |        nan |     0.5531 |      0.7375 |      1.5417 |      0.419  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3699 |        nan |     0.2648 |      0.9348 |      1.3962 |      0.197  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4157 |        nan |     0.3041 |      0.9353 |      1.5407 |      0.2242 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4865 |        nan |     0.367  |      0.9284 |      1.7475 |      0.2652 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.599  |        nan |     0.4539 |      0.9168 |      2.0206 |      0.327  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3951 |        nan |     0.2922 |      0.9071 |      1.2982 |      0.2138 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4548 |        nan |     0.3445 |      0.8822 |      1.367  |      0.2515 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.551  |        nan |     0.4253 |      0.8346 |      1.4529 |      0.3122 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6873 |        nan |     0.5336 |      0.7708 |      1.5558 |      0.3994 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3915 |        nan |     0.2849 |      0.8979 |      1.2888 |      0.2117 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4476 |        nan |     0.3332 |      0.8775 |      1.3728 |      0.2458 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.543  |        nan |     0.4105 |      0.8429 |      1.4812 |      0.3037 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6898 |        nan |     0.5244 |      0.7842 |      1.6125 |      0.3941 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.388  |        nan |     0.2825 |      0.8794 |      1.161  |      0.2103 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4362 |        nan |     0.3247 |      0.8554 |      1.2192 |      0.2408 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5194 |        nan |     0.3909 |      0.8244 |      1.2912 |      0.2925 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.626  |        nan |     0.4714 |      0.7685 |      1.3775 |      0.3581 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.4023 |        nan |     0.2953 |      0.8517 |      1.0918 |      0.2203 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4573 |        nan |     0.3418 |      0.8193 |      1.1364 |      0.2554 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5418 |        nan |     0.4095 |      0.7685 |      1.1851 |      0.31   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6609 |        nan |     0.5033 |      0.7043 |      1.2607 |      0.3871 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5735 |        nan |     0.4439 |      0.7426 |      1.2492 |      0.3353 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.6459 |        nan |     0.4967 |      0.6885 |      1.2735 |      0.3808 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.7207 |        nan |     0.555  |      0.6506 |      1.3117 |      0.4307 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.8481 |        nan |     0.6476 |      0.6067 |      1.3664 |      0.5128 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.427  |        nan |     0.3228 |      0.882  |      1.3184 |      0.2367 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5427 |        nan |     0.4143 |      0.8258 |      1.4162 |      0.3073 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.6954 |        nan |     0.5359 |      0.7462 |      1.5268 |      0.405  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3882 |        nan |     0.2851 |      0.9355 |      1.4143 |      0.2099 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4621 |        nan |     0.3463 |      0.9243 |      1.6575 |      0.2516 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.5728 |        nan |     0.4347 |      0.9198 |      1.9652 |      0.3127 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4181 |        nan |     0.3175 |      0.8949 |      1.3202 |      0.2311 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5229 |        nan |     0.4032 |      0.8449 |      1.4228 |      0.2952 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.664  |        nan |     0.5155 |      0.7826 |      1.5395 |      0.3847 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4103 |        nan |     0.3046 |      0.8829 |      1.3104 |      0.2261 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5136 |        nan |     0.3867 |      0.8474 |      1.44   |      0.2869 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6646 |        nan |     0.506  |      0.791  |      1.5896 |      0.3794 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4018 |        nan |     0.3008 |      0.8608 |      1.1808 |      0.2229 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5014 |        nan |     0.3748 |      0.8295 |      1.2672 |      0.2812 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6084 |        nan |     0.4584 |      0.7741 |      1.3648 |      0.3477 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4215 |        nan |     0.3165 |      0.835  |      1.1062 |      0.2354 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5212 |        nan |     0.3919 |      0.7797 |      1.1652 |      0.297  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.642  |        nan |     0.4887 |      0.7119 |      1.2502 |      0.3751 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.6223 |        nan |     0.4778 |      0.6986 |      1.2692 |      0.3652 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.7056 |        nan |     0.543  |      0.6548 |      1.3076 |      0.4206 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.8348 |        nan |     0.638  |      0.6116 |      1.363  |      0.5043 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.4793 |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.8255 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.4967 |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       1.3508 |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.5042 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.9255 |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.4475 |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.8766 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.4861 |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.7645 |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.5053 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.7835 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3917 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       0.7828 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.963  | 2.0142 | 2.352  |
| mssa:fixed_mat  | native    | 0.8931 | 1.3059 | 2.5108 |
| mssa:neural_ssm | aci       | 0.9732 | 1.8294 | 2.1416 |
| mssa:neural_ssm | native    | 0.936  | 1.3952 | 2.1661 |
| mssa:no_defl    | aci       | 0.9658 | 1.92   | 2.3115 |
| mssa:no_defl    | native    | 0.9036 | 1.2925 | 2.3646 |
| mssa:no_disc    | aci       | 0.9633 | 1.9601 | 2.262  |
| mssa:no_disc    | native    | 0.8954 | 1.2834 | 2.4421 |
| mssa:no_ms      | aci       | 0.9645 | 1.9799 | 2.2989 |
| mssa:no_ms      | native    | 0.8785 | 1.1566 | 2.5887 |
| mssa:no_proj    | aci       | 0.9645 | 2.0018 | 2.3098 |
| mssa:no_proj    | native    | 0.8496 | 1.088  | 2.7868 |
| mssa:no_rev     | aci       | 0.9497 | 2.4279 | 2.826  |
| mssa:no_rev     | native    | 0.7349 | 1.2374 | 4.5219 |
