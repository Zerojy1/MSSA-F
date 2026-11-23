# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E6_ablation_s0`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.8142 |        nan |     1.2827 |      0.7522 |      3.4804 |      1.0263 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      2.8123 |        nan |     2.3127 |      0.7664 |      6.2866 |      1.6558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.6591 |        nan |     1.2108 |      0.7063 |      3.1156 |      0.9627 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.6772 |        nan |     1.2471 |      0.7237 |      3.5069 |      0.993  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.7076 |        nan |     1.246  |      0.7435 |      3.0719 |      0.977  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.6958 |        nan |     1.2714 |      0.6095 |      2.5648 |      1.021  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.4606 |        nan |     1.1944 |      0.6416 |      2.8394 |      0.918  |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.6039 |        nan |     1.1828 |      0.6201 |      2.1256 |      0.9633 |             1.5139 |                0.0662 |                          0 |           13.8043 |            nan     |
| mssa:fixed_mat  |       0.4 |      1.2363 |        nan |     0.9449 |      0.6527 |      2.0621 |      0.7534 |             1.1537 |                0.0783 |                          0 |            7.8567 |             19.18  |
| mssa:fixed_mat  |       0.6 |      0.7461 |        nan |     0.597  |      0.8082 |      1.9648 |      0.4366 |             0.7543 |                0.0712 |                          0 |            0.38   |            nan     |
| mssa:neural_ssm |       0.2 |      1.4819 |        nan |     1.1286 |      0.7123 |      3.0461 |      0.8667 |             1.3471 |                0.1233 |                          0 |           19.6717 |            nan     |
| mssa:neural_ssm |       0.4 |      0.9759 |        nan |     0.7863 |      0.8947 |      2.8843 |      0.5587 |             0.916  |                0.1461 |                          0 |            8.0867 |             21.54  |
| mssa:neural_ssm |       0.6 |      0.735  |        nan |     0.5577 |      0.9258 |      2.7228 |      0.4019 |             0.714  |                0.1592 |                          0 |            9.14   |              2.32  |
| mssa:no_defl    |       0.2 |      1.528  |        nan |     1.1413 |      0.6126 |      2.189  |      0.9191 |             1.4335 |                0.0633 |                          0 |           10.382  |            nan     |
| mssa:no_defl    |       0.4 |      1.1569 |        nan |     0.9013 |      0.6809 |      2.1291 |      0.7018 |             1.0894 |                0.0753 |                          0 |            4.03   |            nan     |
| mssa:no_defl    |       0.6 |      0.7007 |        nan |     0.5557 |      0.8425 |      2.0313 |      0.4048 |             0.7067 |                0.0794 |                          0 |            1.56   |            nan     |
| mssa:no_disc    |       0.2 |      1.5245 |        nan |     1.1619 |      0.6235 |      2.2694 |      0.9306 |             1.4623 |                0.072  |                          0 |           19.87   |            nan     |
| mssa:no_disc    |       0.4 |      1.1781 |        nan |     0.9134 |      0.6748 |      2.2097 |      0.7184 |             1.0991 |                0.0876 |                          0 |            5.615  |            nan     |
| mssa:no_disc    |       0.6 |      0.753  |        nan |     0.6021 |      0.8299 |      2.1039 |      0.4397 |             0.7589 |                0.0794 |                          0 |            2.72   |            nan     |
| mssa:no_ms      |       0.2 |      1.5095 |        nan |     1.1355 |      0.5662 |      1.9435 |      0.928  |             1.3975 |                0.0784 |                          0 |           15.77   |            nan     |
| mssa:no_ms      |       0.4 |      1.1594 |        nan |     0.9013 |      0.6145 |      1.8891 |      0.721  |             1.0627 |                0.0993 |                          0 |            7.8067 |             18.44  |
| mssa:no_ms      |       0.6 |      0.6872 |        nan |     0.5507 |      0.8059 |      1.8058 |      0.4056 |             0.6739 |                0.0806 |                          0 |            0.79   |             14.19  |
| mssa:no_proj    |       0.2 |      1.4796 |        nan |     1.0952 |      0.486  |      1.6877 |      0.9113 |             1.3873 |                0.0476 |                          0 |            8.0971 |              1.94  |
| mssa:no_proj    |       0.4 |      1.1325 |        nan |     0.8999 |      0.4954 |      1.6421 |      0.7218 |             1.1191 |                0.0573 |                          0 |            0.4933 |              2.32  |
| mssa:no_proj    |       0.6 |      0.6992 |        nan |     0.5638 |      0.6998 |      1.5692 |      0.4206 |             0.7186 |                0.042  |                          0 |            2.34   |              8.835 |
| mssa:no_rev     |       0.2 |      1.1873 |        nan |     0.9632 |      0.4934 |      1.6175 |      0.7827 |             1.2097 |                0      |                          0 |           17.7929 |            nan     |
| mssa:no_rev     |       0.4 |      0.8898 |        nan |     0.7248 |      0.6153 |      1.5896 |      0.5591 |             0.8438 |                0      |                          0 |            8.84   |             21.37  |
| mssa:no_rev     |       0.6 |      0.6192 |        nan |     0.491  |      0.7523 |      1.5051 |      0.3672 |             0.5355 |                0      |                          0 |          nan      |            nan     |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.398  |        nan |     0.291  |      0.9187 |      1.3727 |      0.2142 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.5257 |        nan |     0.3976 |      0.8768 |      1.5942 |      0.2902 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.6714 |        nan |     0.5092 |      0.8262 |      1.7588 |      0.3773 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.8367 |        nan |     0.6283 |      0.7754 |      1.8948 |      0.4757 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3869 |        nan |     0.2793 |      0.9316 |      1.5006 |      0.208  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.5019 |        nan |     0.3777 |      0.9297 |      1.914  |      0.2751 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.6482 |        nan |     0.4934 |      0.9129 |      2.2464 |      0.3564 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.8296 |        nan |     0.6385 |      0.8999 |      2.5545 |      0.4593 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3886 |        nan |     0.283  |      0.9214 |      1.3727 |      0.2087 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.5101 |        nan |     0.3846 |      0.8885 |      1.6111 |      0.28   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.6508 |        nan |     0.4929 |      0.8588 |      1.7932 |      0.3629 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.8084 |        nan |     0.6063 |      0.8074 |      1.948  |      0.4558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3855 |        nan |     0.2821 |      0.9224 |      1.3753 |      0.2076 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.5064 |        nan |     0.3861 |      0.8955 |      1.6304 |      0.2798 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6487 |        nan |     0.4974 |      0.854  |      1.826  |      0.3647 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.8096 |        nan |     0.6158 |      0.8069 |      1.9942 |      0.4608 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3979 |        nan |     0.2913 |      0.908  |      1.3212 |      0.215  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.52   |        nan |     0.3927 |      0.8604 |      1.5119 |      0.2891 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.6554 |        nan |     0.4979 |      0.809  |      1.6471 |      0.3717 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.8073 |        nan |     0.6123 |      0.7614 |      1.7537 |      0.4652 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3886 |        nan |     0.2847 |      0.8872 |      1.2101 |      0.2105 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.5052 |        nan |     0.3813 |      0.8374 |      1.3511 |      0.2815 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.6353 |        nan |     0.4848 |      0.7846 |      1.4461 |      0.3621 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.7866 |        nan |     0.5974 |      0.7014 |      1.5197 |      0.4575 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5008 |        nan |     0.3914 |      0.8087 |      1.3771 |      0.2901 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.5486 |        nan |     0.4305 |      0.7765 |      1.3922 |      0.3212 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.6098 |        nan |     0.4783 |      0.7434 |      1.413  |      0.3602 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.699  |        nan |     0.5413 |      0.6998 |      1.4474 |      0.4152 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.398  |        nan |     0.291  |      0.9187 |      1.3727 |      0.2142 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4586 |        nan |     0.341  |      0.8919 |      1.4573 |      0.2501 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5518 |        nan |     0.4171 |      0.8632 |      1.5682 |      0.3063 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.7081 |        nan |     0.5319 |      0.7939 |      1.7035 |      0.3996 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3869 |        nan |     0.2793 |      0.9316 |      1.5006 |      0.208  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4441 |        nan |     0.3288 |      0.9293 |      1.6383 |      0.2407 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.5396 |        nan |     0.4085 |      0.9099 |      1.8296 |      0.2945 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6765 |        nan |     0.5178 |      0.896  |      2.076  |      0.3716 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3886 |        nan |     0.283  |      0.9214 |      1.3727 |      0.2087 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4445 |        nan |     0.3292 |      0.902  |      1.4587 |      0.2415 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5341 |        nan |     0.402  |      0.8743 |      1.5766 |      0.2943 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.677  |        nan |     0.5098 |      0.8249 |      1.7206 |      0.3785 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3855 |        nan |     0.2821 |      0.9224 |      1.3753 |      0.2076 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4393 |        nan |     0.328  |      0.9043 |      1.4703 |      0.2399 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5256 |        nan |     0.3996 |      0.8794 |      1.5945 |      0.2915 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6676 |        nan |     0.5076 |      0.8249 |      1.7471 |      0.3758 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3979 |        nan |     0.2913 |      0.908  |      1.3212 |      0.215  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4588 |        nan |     0.3431 |      0.8794 |      1.3978 |      0.2523 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5524 |        nan |     0.42   |      0.8383 |      1.4943 |      0.3103 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6986 |        nan |     0.5303 |      0.7685 |      1.6104 |      0.4005 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3886 |        nan |     0.2847 |      0.8872 |      1.2101 |      0.2105 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.438  |        nan |     0.3266 |      0.8641 |      1.2695 |      0.2409 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.524  |        nan |     0.3958 |      0.8276 |      1.3426 |      0.2934 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6412 |        nan |     0.488  |      0.7722 |      1.4319 |      0.3661 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5008 |        nan |     0.3914 |      0.8087 |      1.3771 |      0.2901 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5339 |        nan |     0.4205 |      0.78   |      1.4062 |      0.3128 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.5844 |        nan |     0.4624 |      0.756  |      1.4483 |      0.3466 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.6641 |        nan |     0.5256 |      0.7181 |      1.507  |      0.3971 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.42   |        nan |     0.312  |      0.9023 |      1.395  |      0.2295 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5193 |        nan |     0.392  |      0.8714 |      1.5268 |      0.288  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.6827 |        nan |     0.5133 |      0.8026 |      1.6802 |      0.3847 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4115 |        nan |     0.3055 |      0.9235 |      1.5224 |      0.2239 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.514  |        nan |     0.3877 |      0.9089 |      1.7491 |      0.2803 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6508 |        nan |     0.4986 |      0.8982 |      2.0279 |      0.3573 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4091 |        nan |     0.3024 |      0.9078 |      1.3913 |      0.2227 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5029 |        nan |     0.3774 |      0.8782 |      1.5312 |      0.277  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6514 |        nan |     0.4908 |      0.8311 |      1.6946 |      0.3637 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4049 |        nan |     0.3014 |      0.9069 |      1.399  |      0.2216 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.4953 |        nan |     0.3757 |      0.8862 |      1.5464 |      0.2745 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6424 |        nan |     0.4881 |      0.8322 |      1.7194 |      0.361  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4223 |        nan |     0.3154 |      0.8903 |      1.3443 |      0.2322 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.525  |        nan |     0.3981 |      0.8462 |      1.4597 |      0.2941 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6767 |        nan |     0.5139 |      0.7757 |      1.5914 |      0.3872 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4038 |        nan |     0.302  |      0.8774 |      1.2296 |      0.2222 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5009 |        nan |     0.3771 |      0.8363 |      1.3175 |      0.2796 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6202 |        nan |     0.4716 |      0.7794 |      1.4187 |      0.3533 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5098 |        nan |     0.4039 |      0.7926 |      1.402  |      0.2996 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.5724 |        nan |     0.4516 |      0.76   |      1.4443 |      0.3387 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.6516 |        nan |     0.5157 |      0.7219 |      1.5036 |      0.3892 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.466  |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.8984 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.5008 |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       1.8029 |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.4238 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.915  |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.4151 |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.8806 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.5186 |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.8394 |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.4854 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.7845 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3466 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       1.5672 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.9662 | 1.8866 | 2.2538 |
| mssa:fixed_mat  | native    | 0.9141 | 1.3635 | 2.3259 |
| mssa:neural_ssm | aci       | 0.9742 | 1.8763 | 2.1221 |
| mssa:neural_ssm | native    | 0.9365 | 1.4988 | 2.1537 |
| mssa:no_defl    | aci       | 0.9643 | 1.9125 | 2.2597 |
| mssa:no_defl    | native    | 0.9165 | 1.3617 | 2.2816 |
| mssa:no_disc    | aci       | 0.9648 | 1.8672 | 2.2114 |
| mssa:no_disc    | native    | 0.9185 | 1.3696 | 2.2347 |
| mssa:no_ms      | aci       | 0.966  | 1.8784 | 2.2246 |
| mssa:no_ms      | native    | 0.9025 | 1.3157 | 2.3545 |
| mssa:no_proj    | aci       | 0.965  | 1.9082 | 2.2523 |
| mssa:no_proj    | native    | 0.8832 | 1.2039 | 2.4432 |
| mssa:no_rev     | aci       | 0.9577 | 2.1636 | 2.5839 |
| mssa:no_rev     | native    | 0.7981 | 1.3648 | 3.5626 |
