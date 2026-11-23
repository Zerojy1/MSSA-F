# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E6_ablation_s1`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.6562 |        nan |     1.244  |      0.7618 |      3.4891 |      0.9602 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      1.7221 |        nan |     1.3583 |      0.6989 |      3.5729 |      1.0398 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.7068 |        nan |     1.2612 |      0.6769 |      2.9226 |      1.003  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.6716 |        nan |     1.215  |      0.7269 |      3.5011 |      0.9718 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.3902 |        nan |     1.0322 |      0.743  |      2.708  |      0.7988 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.6358 |        nan |     1.2506 |      0.5994 |      2.8266 |      0.9915 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.6888 |        nan |     1.2057 |      0.6751 |      2.4768 |      0.9719 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.4861 |        nan |     1.1495 |      0.5908 |      2.0873 |      0.92   |             1.4855 |                0.0835 |                          0 |           13.7943 |           nan      |
| mssa:fixed_mat  |       0.4 |      1.1427 |        nan |     0.9003 |      0.6626 |      2.0231 |      0.7032 |             1.1383 |                0.0984 |                          0 |           12.1767 |           nan      |
| mssa:fixed_mat  |       0.6 |      0.6972 |        nan |     0.5515 |      0.8402 |      1.9326 |      0.4041 |             0.7297 |                0.0864 |                          0 |            0.38   |           nan      |
| mssa:neural_ssm |       0.2 |      1.5486 |        nan |     1.1605 |      0.733  |      3.1039 |      0.8883 |             1.4555 |                0.1615 |                          0 |           14.002  |           nan      |
| mssa:neural_ssm |       0.4 |      1.0348 |        nan |     0.7775 |      0.871  |      2.9527 |      0.5734 |             1.0507 |                0.1825 |                          0 |            4.0167 |            10.18   |
| mssa:neural_ssm |       0.6 |      0.7707 |        nan |     0.5744 |      0.9167 |      2.7722 |      0.415  |             0.7492 |                0.2035 |                          0 |            0.75   |             1.17   |
| mssa:no_defl    |       0.2 |      1.4702 |        nan |     1.0975 |      0.6029 |      2.0743 |      0.8876 |             1.41   |                0.0853 |                          0 |           11.1529 |           nan      |
| mssa:no_defl    |       0.4 |      1.1282 |        nan |     0.8648 |      0.6695 |      2.0197 |      0.6813 |             1.0697 |                0.0992 |                          0 |            7.2967 |           nan      |
| mssa:no_defl    |       0.6 |      0.695  |        nan |     0.5472 |      0.8174 |      1.9336 |      0.4017 |             0.7126 |                0.0886 |                          0 |            0.38   |             3.88   |
| mssa:no_disc    |       0.2 |      1.4604 |        nan |     1.0894 |      0.6309 |      2.157  |      0.8771 |             1.4487 |                0.0997 |                          0 |           11.1233 |           nan      |
| mssa:no_disc    |       0.4 |      1.1201 |        nan |     0.8458 |      0.6977 |      2.099  |      0.6702 |             1.0994 |                0.1131 |                          0 |            6.48   |           nan      |
| mssa:no_disc    |       0.6 |      0.7173 |        nan |     0.5698 |      0.8322 |      2.0005 |      0.4147 |             0.7848 |                0.105  |                          0 |            0.79   |           nan      |
| mssa:no_ms      |       0.2 |      1.3392 |        nan |     1.0264 |      0.6074 |      2.0268 |      0.8162 |             1.282  |                0.1037 |                          0 |           11.2214 |             0.77   |
| mssa:no_ms      |       0.4 |      1.0084 |        nan |     0.7832 |      0.6748 |      1.9616 |      0.6046 |             0.9778 |                0.1161 |                          0 |            1.5133 |             1.94   |
| mssa:no_ms      |       0.6 |      0.662  |        nan |     0.5116 |      0.855  |      1.8767 |      0.3733 |             0.6785 |                0.1165 |                          0 |            1.17   |             1.94   |
| mssa:no_proj    |       0.2 |      1.388  |        nan |     1.0843 |      0.5192 |      1.9281 |      0.8753 |             1.3757 |                0.0609 |                          0 |            8.3033 |             6.2333 |
| mssa:no_proj    |       0.4 |      1.1672 |        nan |     0.9145 |      0.5252 |      1.8633 |      0.7411 |             1.1757 |                0.0581 |                          0 |            8.5825 |             5.2175 |
| mssa:no_proj    |       0.6 |      0.7957 |        nan |     0.6175 |      0.6895 |      1.7469 |      0.4777 |             0.8128 |                0.0397 |                          0 |            1.73   |             6.41   |
| mssa:no_rev     |       0.2 |      1.4971 |        nan |     1.1238 |      0.4189 |      1.4354 |      0.9565 |             1.4523 |                0      |                          0 |           15.85   |           nan      |
| mssa:no_rev     |       0.4 |      1.0813 |        nan |     0.846  |      0.5206 |      1.4147 |      0.6951 |             1.0404 |                0      |                          0 |           14.73   |           nan      |
| mssa:no_rev     |       0.6 |      0.634  |        nan |     0.4997 |      0.7192 |      1.3335 |      0.3786 |             0.5875 |                0      |                          0 |          nan      |           nan      |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3888 |        nan |     0.2813 |      0.9159 |      1.3461 |      0.2083 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.5043 |        nan |     0.3783 |      0.8843 |      1.5688 |      0.2772 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.6375 |        nan |     0.4844 |      0.8416 |      1.7335 |      0.3579 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.7878 |        nan |     0.5961 |      0.7899 |      1.8675 |      0.449  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3653 |        nan |     0.2614 |      0.9265 |      1.3133 |      0.194  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4671 |        nan |     0.3516 |      0.9325 |      1.7565 |      0.2557 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.601  |        nan |     0.4625 |      0.9253 |      2.1375 |      0.3328 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.7722 |        nan |     0.5965 |      0.907  |      2.522  |      0.4294 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3919 |        nan |     0.2864 |      0.921  |      1.3725 |      0.2107 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.5132 |        nan |     0.3875 |      0.888  |      1.5903 |      0.283  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.6508 |        nan |     0.4965 |      0.843  |      1.7476 |      0.3658 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.7978 |        nan |     0.6009 |      0.7899 |      1.8716 |      0.4525 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3867 |        nan |     0.282  |      0.9191 |      1.3602 |      0.2076 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.5036 |        nan |     0.3803 |      0.8922 |      1.5925 |      0.2771 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6383 |        nan |     0.488  |      0.8502 |      1.7673 |      0.3581 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.7884 |        nan |     0.596  |      0.8019 |      1.9141 |      0.4469 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3679 |        nan |     0.2636 |      0.9191 |      1.3145 |      0.196  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.4698 |        nan |     0.3544 |      0.903  |      1.5407 |      0.2572 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.5931 |        nan |     0.4549 |      0.8693 |      1.7067 |      0.3309 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.7413 |        nan |     0.5681 |      0.8109 |      1.8377 |      0.4199 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3757 |        nan |     0.2714 |      0.8983 |      1.2559 |      0.2022 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.4789 |        nan |     0.3631 |      0.8547 |      1.4392 |      0.2673 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.5992 |        nan |     0.4641 |      0.8023 |      1.5724 |      0.3436 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.7347 |        nan |     0.5688 |      0.7409 |      1.6831 |      0.4295 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5207 |        nan |     0.403  |      0.775  |      1.2109 |      0.3015 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.5732 |        nan |     0.4441 |      0.7395 |      1.2248 |      0.3359 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.6411 |        nan |     0.4939 |      0.7013 |      1.2441 |      0.3784 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.7435 |        nan |     0.5619 |      0.6523 |      1.2768 |      0.44   |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3888 |        nan |     0.2813 |      0.9159 |      1.3461 |      0.2083 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4421 |        nan |     0.3272 |      0.8956 |      1.4321 |      0.241  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.524  |        nan |     0.3962 |      0.8655 |      1.5432 |      0.2913 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.6499 |        nan |     0.4964 |      0.8202 |      1.6793 |      0.3677 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3653 |        nan |     0.2614 |      0.9265 |      1.3133 |      0.194  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.4111 |        nan |     0.3027 |      0.9233 |      1.4536 |      0.2217 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4837 |        nan |     0.3673 |      0.9187 |      1.6561 |      0.2641 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6062 |        nan |     0.4624 |      0.9039 |      1.9265 |      0.3315 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3919 |        nan |     0.2864 |      0.921  |      1.3725 |      0.2107 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4469 |        nan |     0.3338 |      0.8951 |      1.4569 |      0.244  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5322 |        nan |     0.4049 |      0.872  |      1.565  |      0.296  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6657 |        nan |     0.5071 |      0.8189 |      1.6944 |      0.3753 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3867 |        nan |     0.282  |      0.9191 |      1.3602 |      0.2076 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4397 |        nan |     0.3277 |      0.9006 |      1.4487 |      0.2397 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5255 |        nan |     0.399  |      0.8701 |      1.5634 |      0.2919 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6573 |        nan |     0.4995 |      0.8272 |      1.704  |      0.37   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3679 |        nan |     0.2636 |      0.9191 |      1.3145 |      0.196  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4083 |        nan |     0.3006 |      0.9136 |      1.3887 |      0.2208 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.4837 |        nan |     0.3673 |      0.8937 |      1.4999 |      0.2664 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.5986 |        nan |     0.4583 |      0.8503 |      1.6332 |      0.3348 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3757 |        nan |     0.2714 |      0.8983 |      1.2559 |      0.2022 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4202 |        nan |     0.3108 |      0.878  |      1.329  |      0.2307 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4787 |        nan |     0.362  |      0.853  |      1.4229 |      0.2676 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.5743 |        nan |     0.4393 |      0.8119 |      1.5373 |      0.326  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5207 |        nan |     0.403  |      0.775  |      1.2109 |      0.3015 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.571  |        nan |     0.4419 |      0.7375 |      1.2375 |      0.3346 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6301 |        nan |     0.4886 |      0.7079 |      1.2751 |      0.3741 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.73   |        nan |     0.5651 |      0.6557 |      1.3277 |      0.44   |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.4079 |        nan |     0.3025 |      0.8986 |      1.3696 |      0.2233 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.4961 |        nan |     0.3745 |      0.8702 |      1.5016 |      0.2755 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.626  |        nan |     0.4786 |      0.8248 |      1.656  |      0.3539 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3804 |        nan |     0.2828 |      0.9198 |      1.3299 |      0.2065 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4565 |        nan |     0.3455 |      0.9175 |      1.5673 |      0.2493 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.578  |        nan |     0.4418 |      0.9092 |      1.8709 |      0.3161 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4106 |        nan |     0.3071 |      0.8995 |      1.3953 |      0.2249 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5008 |        nan |     0.3805 |      0.8782 |      1.5244 |      0.2784 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6399 |        nan |     0.4882 |      0.828  |      1.6721 |      0.3603 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.4052 |        nan |     0.3023 |      0.9041 |      1.3836 |      0.2218 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.4971 |        nan |     0.3774 |      0.8751 |      1.5198 |      0.2761 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6331 |        nan |     0.4812 |      0.8332 |      1.6791 |      0.3559 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.3791 |        nan |     0.2793 |      0.9152 |      1.3244 |      0.2061 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.46   |        nan |     0.3483 |      0.8997 |      1.4575 |      0.2534 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.5761 |        nan |     0.442  |      0.8575 |      1.6099 |      0.3225 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.391  |        nan |     0.2886 |      0.8866 |      1.2775 |      0.2152 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.4521 |        nan |     0.3403 |      0.8609 |      1.3893 |      0.2523 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.5506 |        nan |     0.4221 |      0.8179 |      1.5187 |      0.3125 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5463 |        nan |     0.4251 |      0.7438 |      1.2332 |      0.3202 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6148 |        nan |     0.4771 |      0.7108 |      1.271  |      0.3645 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.7159 |        nan |     0.5547 |      0.6639 |      1.3243 |      0.4312 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.4353 |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.8896 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.3613 |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       0.607  |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.4597 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.9897 |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.4247 |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.9152 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.474  |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.8945 |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.5431 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.9602 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3522 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       0.7908 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.9663 | 1.8737 | 2.2499 |
| mssa:fixed_mat  | native    | 0.9115 | 1.3387 | 2.3144 |
| mssa:neural_ssm | aci       | 0.9687 | 1.8409 | 2.1847 |
| mssa:neural_ssm | native    | 0.9245 | 1.3129 | 2.204  |
| mssa:no_defl    | aci       | 0.9663 | 1.8908 | 2.2483 |
| mssa:no_defl    | native    | 0.9169 | 1.3663 | 2.2893 |
| mssa:no_disc    | aci       | 0.9663 | 1.8722 | 2.2433 |
| mssa:no_disc    | native    | 0.9149 | 1.3538 | 2.2672 |
| mssa:no_ms      | aci       | 0.9673 | 1.8499 | 2.2356 |
| mssa:no_ms      | native    | 0.9136 | 1.3055 | 2.2301 |
| mssa:no_proj    | aci       | 0.9619 | 1.9081 | 2.2751 |
| mssa:no_proj    | native    | 0.8942 | 1.2493 | 2.3639 |
| mssa:no_rev     | aci       | 0.9524 | 2.2382 | 2.7071 |
| mssa:no_rev     | native    | 0.766  | 1.2003 | 3.9364 |
