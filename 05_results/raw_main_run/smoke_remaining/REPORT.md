# MSSA-Rut experiment report

Run directory: `results/smoke_remaining`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      2.3277 |        nan |     1.9766 |      0.4023 |      2.5436 |      1.6584 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |     11.3189 |        nan |     7.296  |      0.2529 |      2.7574 |      6.954  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      2.1624 |        nan |     1.7326 |      0.4644 |      2.376  |      1.4721 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      2.1973 |        nan |     1.7493 |      0.4552 |      2.3742 |      1.4931 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      2.0154 |        nan |     1.5408 |      0.4897 |      2.3872 |      1.2969 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      2.3965 |        nan |     1.9899 |      0.3839 |      2.3823 |      1.698  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      2.1717 |        nan |     1.6685 |      0.4598 |      2.2266 |      1.4428 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      2.0845 |        nan |     1.7694 |      0.1605 |      1.2859 |      1.5899 |             2.4547 |                0.0582 |                          0 |             30.62 |             nan    |
| mssa:fixed_mat  |       0.4 |      1.7156 |        nan |     1.4437 |      0.2634 |      1.2689 |      1.2785 |             1.9452 |                0.0465 |                          0 |            nan    |             nan    |
| mssa:fixed_mat  |       0.6 |      1.2299 |        nan |     1.0545 |      0.3068 |      1.1984 |      0.9054 |             1.3618 |                0.0234 |                          0 |            nan    |             nan    |
| mssa:neural_ssm |       0.2 |     12.7641 |        nan |     9.2666 |      0.0716 |      1.6995 |      9.0252 |            18.9776 |                0      |                          0 |              3.3  |              16.77 |
| mssa:neural_ssm |       0.4 |     11.2992 |        nan |     9.0253 |      0.0229 |      1.6446 |      8.7894 |            16.2376 |                0      |                          0 |            nan    |              13.68 |
| mssa:neural_ssm |       0.6 |      7.6123 |        nan |     6.1652 |      0.0057 |      1.4165 |      5.9614 |            11.0806 |                0      |                          0 |            nan    |               2.75 |
| mssa:no_defl    |       0.2 |      1.9145 |        nan |     1.5883 |      0.2436 |      1.1769 |      1.436  |             2.2737 |                0      |                          0 |             31.76 |             nan    |
| mssa:no_defl    |       0.4 |      1.5963 |        nan |     1.322  |      0.2863 |      1.1609 |      1.1797 |             1.829  |                0      |                          0 |            nan    |             nan    |
| mssa:no_defl    |       0.6 |      1.175  |        nan |     1.0032 |      0.3125 |      1.1011 |      0.868  |             1.3162 |                0      |                          0 |            nan    |             nan    |
| mssa:no_disc    |       0.2 |      1.9403 |        nan |     1.6006 |      0.255  |      1.1754 |      1.4507 |             2.2845 |                0      |                          0 |             32.16 |             nan    |
| mssa:no_disc    |       0.4 |      1.6159 |        nan |     1.333  |      0.3053 |      1.1596 |      1.192  |             1.8346 |                0.0077 |                          0 |            nan    |             nan    |
| mssa:no_disc    |       0.6 |      1.1858 |        nan |     1.008  |      0.3182 |      1.1001 |      0.8738 |             1.3163 |                0      |                          0 |            nan    |             nan    |
| mssa:no_ms      |       0.2 |      1.7172 |        nan |     1.4113 |      0.2837 |      1.1801 |      1.2638 |             1.999  |                0      |                          0 |             32.54 |             nan    |
| mssa:no_ms      |       0.4 |      1.429  |        nan |     1.1726 |      0.3168 |      1.1624 |      1.0337 |             1.6067 |                0.0153 |                          0 |            nan    |             nan    |
| mssa:no_ms      |       0.6 |      1.0882 |        nan |     0.9097 |      0.3352 |      1.1089 |      0.7763 |             1.1681 |                0      |                          0 |            nan    |             nan    |
| mssa:no_proj    |       0.2 |      2.1837 |        nan |     1.8272 |      0.1261 |      1.1868 |      1.6607 |             2.6648 |                0      |                          0 |             28.67 |             nan    |
| mssa:no_proj    |       0.4 |      1.7305 |        nan |     1.4514 |      0.229  |      1.1603 |      1.2964 |             2.0855 |                0.0038 |                          0 |            nan    |             nan    |
| mssa:no_proj    |       0.6 |      1.193  |        nan |     1.0306 |      0.2443 |      1.0931 |      0.8909 |             1.4515 |                0      |                          0 |            nan    |             nan    |
| mssa:no_rev     |       0.2 |      1.8706 |        nan |     1.5402 |      0.2006 |      0.9508 |      1.4164 |             2.2803 |                0      |                          0 |             33.31 |             nan    |
| mssa:no_rev     |       0.4 |      1.5203 |        nan |     1.2558 |      0.2595 |      0.938  |      1.138  |             1.8176 |                0      |                          0 |            nan    |             nan    |
| mssa:no_rev     |       0.6 |      1.0227 |        nan |     0.8727 |      0.233  |      0.8656 |      0.7629 |             1.241  |                0      |                          0 |            nan    |             nan    |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.5115 |        nan |     0.4097 |      0.6528 |      0.9882 |      0.3134 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.6819 |        nan |     0.559  |      0.5423 |      1.0689 |      0.4412 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.8392 |        nan |     0.6939 |      0.4436 |      1.1179 |      0.5642 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      1.024  |        nan |     0.8601 |      0.3509 |      1.1586 |      0.7163 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      1.0031 |        nan |     0.8534 |      0.2662 |      1.0256 |      0.7259 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      1.609  |        nan |     1.3592 |      0.1831 |      1.1243 |      1.212  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      2.2954 |        nan |     1.9171 |      0.1463 |      1.1953 |      1.7563 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      3.3941 |        nan |     2.7978 |      0.1028 |      1.2741 |      2.6211 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.5035 |        nan |     0.4038 |      0.625  |      0.917  |      0.3124 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.6591 |        nan |     0.5376 |      0.5117 |      0.9863 |      0.431  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.798  |        nan |     0.6572 |      0.4317 |      1.0271 |      0.5409 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.9682 |        nan |     0.8084 |      0.3584 |      1.0616 |      0.6808 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.5046 |        nan |     0.4045 |      0.6204 |      0.9162 |      0.3132 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.6617 |        nan |     0.5393 |      0.5164 |      0.9853 |      0.4327 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.8024 |        nan |     0.6602 |      0.4269 |      1.026  |      0.5439 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.9749 |        nan |     0.8129 |      0.3584 |      1.0604 |      0.6857 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.4732 |        nan |     0.3751 |      0.6829 |      0.9247 |      0.2857 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.6124 |        nan |     0.497  |      0.5775 |      0.9941 |      0.3911 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.7377 |        nan |     0.6047 |      0.4676 |      1.0346 |      0.4899 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.8939 |        nan |     0.7431 |      0.3634 |      1.0683 |      0.6181 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.4574 |        nan |     0.3587 |      0.7037 |      0.9198 |      0.2721 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.605  |        nan |     0.4886 |      0.5845 |      0.9891 |      0.3826 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.7496 |        nan |     0.6135 |      0.4892 |      1.0296 |      0.4968 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.9457 |        nan |     0.7868 |      0.3534 |      1.0635 |      0.6573 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5925 |        nan |     0.466  |      0.4838 |      0.7434 |      0.3847 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.6525 |        nan |     0.5148 |      0.4413 |      0.7559 |      0.4302 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.7316 |        nan |     0.5815 |      0.3909 |      0.7733 |      0.4928 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.881  |        nan |     0.71   |      0.3158 |      0.8047 |      0.6135 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.5115 |        nan |     0.4097 |      0.6528 |      0.9882 |      0.3134 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.6407 |        nan |     0.5154 |      0.5625 |      1.0274 |      0.4093 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.8117 |        nan |     0.6544 |      0.5023 |      1.0748 |      0.5385 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      1.0157 |        nan |     0.8144 |      0.4144 |      1.1341 |      0.6885 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      1.0031 |        nan |     0.8534 |      0.2662 |      1.0256 |      0.7259 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      4.0646 |        nan |     2.6484 |      0.2106 |      1.0728 |      2.5124 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      6.8439 |        nan |     4.4195 |      0.1921 |      1.1333 |      4.2738 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      8.771  |        nan |     5.667  |      0.1968 |      1.2131 |      5.5094 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.5035 |        nan |     0.4038 |      0.625  |      0.917  |      0.3124 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.6105 |        nan |     0.4911 |      0.5532 |      0.9518 |      0.3928 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.7578 |        nan |     0.6114 |      0.4676 |      0.9938 |      0.5052 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.9407 |        nan |     0.7608 |      0.4005 |      1.0466 |      0.6449 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.5046 |        nan |     0.4045 |      0.6204 |      0.9162 |      0.3132 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.6132 |        nan |     0.4934 |      0.5486 |      0.9508 |      0.3949 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.7639 |        nan |     0.617  |      0.4676 |      0.9928 |      0.5103 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.9498 |        nan |     0.7684 |      0.4028 |      1.0454 |      0.6524 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.4732 |        nan |     0.3751 |      0.6829 |      0.9247 |      0.2857 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.5518 |        nan |     0.4443 |      0.5856 |      0.9596 |      0.3464 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.6739 |        nan |     0.5428 |      0.5    |      1.0018 |      0.4365 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.8242 |        nan |     0.6726 |      0.419  |      1.0545 |      0.5572 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.4574 |        nan |     0.3587 |      0.7037 |      0.9198 |      0.2721 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.5299 |        nan |     0.4213 |      0.6574 |      0.9544 |      0.3261 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.659  |        nan |     0.5318 |      0.5486 |      0.9962 |      0.425  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.8153 |        nan |     0.6693 |      0.412  |      1.049  |      0.5519 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5925 |        nan |     0.466  |      0.4838 |      0.7434 |      0.3847 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.6986 |        nan |     0.5536 |      0.4421 |      0.7625 |      0.47   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.8057 |        nan |     0.6479 |      0.3727 |      0.7887 |      0.5572 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.9544 |        nan |     0.7721 |      0.3426 |      0.8251 |      0.675  |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.5846 |        nan |     0.4654 |      0.5945 |      1.0042 |      0.3675 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.7871 |        nan |     0.6317 |      0.5169 |      1.0611 |      0.5194 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.9973 |        nan |     0.7972 |      0.4248 |      1.1269 |      0.6733 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      3.7586 |        nan |     2.4148 |      0.2396 |      1.0448 |      2.2873 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      6.6437 |        nan |     4.2693 |      0.1908 |      1.1153 |      4.1278 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      8.7082 |        nan |     5.597  |      0.2005 |      1.2027 |      5.4419 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.5584 |        nan |     0.4456 |      0.5945 |      0.9318 |      0.354  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.7398 |        nan |     0.5942 |      0.48   |      0.9821 |      0.4912 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.926  |        nan |     0.7474 |      0.4063 |      1.0405 |      0.6335 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.5606 |        nan |     0.4479 |      0.5853 |      0.9308 |      0.356  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.7457 |        nan |     0.5996 |      0.4769 |      0.9811 |      0.496  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.9348 |        nan |     0.7547 |      0.409  |      1.0394 |      0.6406 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.5019 |        nan |     0.404  |      0.6267 |      0.9396 |      0.3124 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.662  |        nan |     0.5296 |      0.5108 |      0.9901 |      0.4264 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.81   |        nan |     0.6609 |      0.4222 |      1.0485 |      0.5471 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4764 |        nan |     0.3794 |      0.6728 |      0.9344 |      0.2909 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.6381 |        nan |     0.5118 |      0.5538 |      0.9845 |      0.409  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.7949 |        nan |     0.6523 |      0.4222 |      1.043  |      0.5367 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.6734 |        nan |     0.5287 |      0.4885 |      0.7594 |      0.4464 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.8043 |        nan |     0.6464 |      0.3662 |      0.786  |      0.5565 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.9487 |        nan |     0.7674 |      0.343  |      0.8227 |      0.6708 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |          1      |          0      |       0.5178 |
| mssa:fixed_mat  | temp_plus5 |          1      |          0      |       0.7161 |
| mssa:neural_ssm | load_x2    |          1      |          0      |       2.2325 |
| mssa:neural_ssm | temp_plus5 |          0.1918 |          0.8082 |      -0.0089 |
| mssa:no_defl    | load_x2    |          1      |          0      |       0.5043 |
| mssa:no_defl    | temp_plus5 |          1      |          0      |       0.6494 |
| mssa:no_disc    | load_x2    |          1      |          0      |       0.4992 |
| mssa:no_disc    | temp_plus5 |          1      |          0      |       0.6452 |
| mssa:no_ms      | load_x2    |          1      |          0      |       0.4855 |
| mssa:no_ms      | temp_plus5 |          1      |          0      |       0.6145 |
| mssa:no_proj    | load_x2    |          1      |          0      |       0.5285 |
| mssa:no_proj    | temp_plus5 |          1      |          0      |       0.6808 |
| mssa:no_rev     | load_x2    |          1      |          0      |       0.4028 |
| mssa:no_rev     | temp_plus5 |          1      |          0      |       0.5018 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |      IS |
|:----------------|:----------|-------:|-------:|--------:|
| mssa:fixed_mat  | aci       | 0.9602 | 2.0126 |  2.3203 |
| mssa:fixed_mat  | native    | 0.6345 | 0.984  |  4.7274 |
| mssa:neural_ssm | aci       | 0.9325 | 2.786  |  3.3794 |
| mssa:neural_ssm | native    | 0.2311 | 1.022  | 17.9414 |
| mssa:no_defl    | aci       | 0.9627 | 1.9629 |  2.2789 |
| mssa:no_defl    | native    | 0.5998 | 0.9133 |  5.0157 |
| mssa:no_disc    | aci       | 0.9627 | 1.9615 |  2.2716 |
| mssa:no_disc    | native    | 0.5948 | 0.9124 |  5.048  |
| mssa:no_ms      | aci       | 0.9652 | 1.9515 |  2.2509 |
| mssa:no_ms      | native    | 0.663  | 0.9211 |  4.2781 |
| mssa:no_proj    | aci       | 0.9652 | 1.9131 |  2.2072 |
| mssa:no_proj    | native    | 0.6854 | 0.9159 |  4.0204 |
| mssa:no_rev     | aci       | 0.9479 | 2.3875 |  2.7836 |
| mssa:no_rev     | native    | 0.4504 | 0.7394 |  8.9523 |

## E5 learned parameters

| exp   |   seed |   beta_hat |   gamma_hat |   wu_load_exp_min |   wu_load_exp_max |   wu_temp_exp_min |   wu_temp_exp_max |   R0eff_Surf_AC13_I_SBS |   R0eff_Surf_AC13_II_SBS |   R0eff_Surf_SMA13 |   R0eff_Surf_PAC13 |   R0eff_Mid_AC20_AH30 |   R0eff_Mid_AC20_SBS |   R0eff_Mid_AC20_AH50 |   R0eff_Bot_AC25_AH30 |   R0eff_Bot_AC25_AH50 |   R0eff_Bot_AC25_AH70 |   R0eff_Bot_AC25_Re_AH70 |   R0eff_Bot_AC10_SBS |   scale_I_SemiRigid_12cmAC |   scale_II_RigidComposite_12cmAC |   scale_III_SemiRigid_16_18cmAC |   scale_IV_Inverted_24_28cmAC |   scale_V_ThickAC_I_24_28cm |   scale_VI_ThickAC_II_36cm |   scale_VII_FullDepth_48_52cm |
|:------|-------:|-----------:|------------:|------------------:|------------------:|------------------:|------------------:|------------------------:|-------------------------:|-------------------:|-------------------:|----------------------:|---------------------:|----------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|---------------------:|---------------------------:|---------------------------------:|--------------------------------:|------------------------------:|----------------------------:|---------------------------:|------------------------------:|
| E5    |      0 |     0.4551 |       2.988 |             0.176 |             0.292 |             3.499 |             3.735 |                   1.716 |                   1.7063 |             1.5985 |             1.9615 |                 1.483 |               1.4823 |                2.3811 |                1.7171 |                2.2876 |                3.2264 |                   2.2064 |               2.1054 |                     0.3696 |                           0.3351 |                          0.4351 |                        0.4341 |                      0.4363 |                      0.345 |                        0.3385 |

## E5 hidden-material recovery

|   seed |   spearman |   n |
|-------:|-----------:|----:|
|      0 |    -0.3455 |  10 |

## E5 H1 discrepancy test

|   seed |   mean_abs_g_II_VII |   mean_abs_g_others |   U |   p_one_sided |
|-------:|--------------------:|--------------------:|----:|--------------:|
|      0 |              0.0666 |              0.0819 |  13 |          0.96 |
