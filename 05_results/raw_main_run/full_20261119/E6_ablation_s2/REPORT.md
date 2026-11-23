# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E6_ablation_s2`

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         0 |      1.9086 |        nan |     1.5228 |      0.5815 |      3.134  |      1.2014 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         0 |      1.6935 |        nan |     1.3396 |      0.7003 |      3.4693 |      1.0302 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         0 |      1.9041 |        nan |     1.4853 |      0.5581 |      2.8708 |      1.1929 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      1.7728 |        nan |     1.3772 |      0.7104 |      3.3917 |      1.0645 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         0 |      1.9053 |        nan |     1.5325 |      0.5209 |      2.8122 |      1.2349 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         0 |      1.903  |        nan |     1.4489 |      0.5815 |      2.756  |      1.1611 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         0 |      1.8652 |        nan |     1.4987 |      0.5163 |      2.5186 |      1.2142 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |       0.2 |      1.6776 |        nan |     1.3103 |      0.4768 |      1.9865 |      1.0724 |             1.6081 |                0.0789 |                          0 |           17.564  |           nan      |
| mssa:fixed_mat  |       0.4 |      1.2604 |        nan |     0.9898 |      0.5573 |      1.9373 |      0.7905 |             1.2174 |                0.0937 |                          0 |           11.41   |           nan      |
| mssa:fixed_mat  |       0.6 |      0.8095 |        nan |     0.6121 |      0.8242 |      1.8391 |      0.4507 |             0.8253 |                0.0817 |                          0 |            2.34   |           nan      |
| mssa:neural_ssm |       0.2 |      1.5325 |        nan |     1.1566 |      0.7347 |      3.05   |      0.8853 |             1.4664 |                0.1535 |                          0 |           16.0883 |           nan      |
| mssa:neural_ssm |       0.4 |      1.078  |        nan |     0.795  |      0.8641 |      2.9106 |      0.5876 |             1.0433 |                0.1873 |                          0 |            2.8933 |            14.3067 |
| mssa:neural_ssm |       0.6 |      0.8644 |        nan |     0.6261 |      0.9121 |      2.7407 |      0.4634 |             0.846  |                0.2222 |                          0 |            6.99   |             1.94   |
| mssa:no_defl    |       0.2 |      1.6867 |        nan |     1.2735 |      0.4986 |      1.956  |      1.0507 |             1.5841 |                0.0691 |                          0 |           13.24   |           nan      |
| mssa:no_defl    |       0.4 |      1.2681 |        nan |     0.9722 |      0.5878 |      1.9105 |      0.7784 |             1.2082 |                0.0906 |                          0 |            4.77   |            18.82   |
| mssa:no_defl    |       0.6 |      0.8241 |        nan |     0.6073 |      0.8059 |      1.8179 |      0.4534 |             0.8219 |                0.084  |                          0 |            1.94   |           nan      |
| mssa:no_disc    |       0.2 |      1.6526 |        nan |     1.2656 |      0.5777 |      2.2661 |      1.0258 |             1.6289 |                0.0708 |                          0 |           17.08   |           nan      |
| mssa:no_disc    |       0.4 |      1.2657 |        nan |     0.9874 |      0.6382 |      2.2104 |      0.7769 |             1.2479 |                0.0891 |                          0 |            5.275  |           nan      |
| mssa:no_disc    |       0.6 |      0.8405 |        nan |     0.6434 |      0.8322 |      2.0998 |      0.4761 |             0.837  |                0.0839 |                          0 |          nan      |           nan      |
| mssa:no_ms      |       0.2 |      1.603  |        nan |     1.267  |      0.4258 |      1.831  |      1.0557 |             1.6021 |                0.0819 |                          0 |           14.28   |           nan      |
| mssa:no_ms      |       0.4 |      1.2389 |        nan |     0.9702 |      0.5244 |      1.7793 |      0.7845 |             1.2002 |                0.1039 |                          0 |            5.7    |            18.82   |
| mssa:no_ms      |       0.6 |      0.8222 |        nan |     0.6162 |      0.7534 |      1.7055 |      0.4673 |             0.8489 |                0.0979 |                          0 |            1.94   |           nan      |
| mssa:no_proj    |       0.2 |      1.6337 |        nan |     1.2397 |      0.4516 |      1.7862 |      1.0318 |             1.5363 |                0.0615 |                          0 |           13.2171 |            18.44   |
| mssa:no_proj    |       0.4 |      1.2549 |        nan |     0.9922 |      0.5267 |      1.7374 |      0.7963 |             1.2502 |                0.0681 |                          0 |            4.2633 |            17.27   |
| mssa:no_proj    |       0.6 |      0.7867 |        nan |     0.5992 |      0.7774 |      1.6581 |      0.4467 |             0.7955 |                0.0548 |                          0 |            1.94   |           nan      |
| mssa:no_rev     |       0.2 |      1.6143 |        nan |     1.271  |      0.3794 |      1.611  |      1.0748 |             1.6456 |                0      |                          0 |           15.525  |           nan      |
| mssa:no_rev     |       0.4 |      1.2402 |        nan |     0.9859 |      0.4847 |      1.5872 |      0.8043 |             1.205  |                0      |                          0 |            8.09   |           nan      |
| mssa:no_rev     |       0.6 |      0.7035 |        nan |     0.5345 |      0.7557 |      1.5034 |      0.4047 |             0.6688 |                0      |                          0 |            3.08   |           nan      |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3918 |        nan |     0.2861 |      0.8988 |      1.2669 |      0.2116 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         3 |      0.5221 |        nan |     0.3958 |      0.865  |      1.4768 |      0.2899 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         6 |      0.6739 |        nan |     0.5157 |      0.8061 |      1.6318 |      0.3824 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |        12 |      0.8593 |        nan |     0.6618 |      0.7434 |      1.7614 |      0.5004 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3674 |        nan |     0.2654 |      0.9261 |      1.3198 |      0.196  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      0.4742 |        nan |     0.3633 |      0.9311 |      1.7527 |      0.2614 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      0.6131 |        nan |     0.479  |      0.9191 |      2.1261 |      0.3429 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      0.7864 |        nan |     0.6223 |      0.8924 |      2.5024 |      0.4452 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3942 |        nan |     0.2871 |      0.8942 |      1.2465 |      0.2129 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         3 |      0.5268 |        nan |     0.3966 |      0.8557 |      1.4554 |      0.2922 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         6 |      0.6812 |        nan |     0.5162 |      0.8023 |      1.6114 |      0.3851 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |        12 |      0.8712 |        nan |     0.6613 |      0.7414 |      1.7424 |      0.504  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3786 |        nan |     0.2758 |      0.9279 |      1.3562 |      0.2034 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.501  |        nan |     0.3819 |      0.9044 |      1.6221 |      0.2766 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.6508 |        nan |     0.5018 |      0.8468 |      1.8246 |      0.3663 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.8323 |        nan |     0.6413 |      0.7989 |      1.9955 |      0.4777 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3976 |        nan |     0.2952 |      0.8933 |      1.2481 |      0.217  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         3 |      0.5315 |        nan |     0.4087 |      0.8402 |      1.4318 |      0.3006 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         6 |      0.6826 |        nan |     0.5298 |      0.7554 |      1.5592 |      0.3972 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |        12 |      0.8628 |        nan |     0.6735 |      0.6858 |      1.6569 |      0.5166 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3947 |        nan |     0.2901 |      0.9002 |      1.2648 |      0.2137 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         3 |      0.5221 |        nan |     0.3947 |      0.8421 |      1.4171 |      0.29   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         6 |      0.6656 |        nan |     0.5065 |      0.7908 |      1.5207 |      0.3784 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |        12 |      0.8351 |        nan |     0.6355 |      0.7289 |      1.6018 |      0.487  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5398 |        nan |     0.4223 |      0.8027 |      1.3791 |      0.3121 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         3 |      0.5983 |        nan |     0.4674 |      0.7741 |      1.3933 |      0.3495 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         6 |      0.6746 |        nan |     0.5251 |      0.73   |      1.4135 |      0.3977 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |        12 |      0.7924 |        nan |     0.6152 |      0.6668 |      1.4473 |      0.4753 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         1 |      0.3918 |        nan |     0.2861 |      0.8988 |      1.2669 |      0.2116 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         2 |      0.4529 |        nan |     0.3394 |      0.8734 |      1.3468 |      0.2492 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.561  |        nan |     0.4245 |      0.8313 |      1.4504 |      0.3152 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.7215 |        nan |     0.5476 |      0.7731 |      1.5781 |      0.4133 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         1 |      0.3674 |        nan |     0.2654 |      0.9261 |      1.3198 |      0.196  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.415  |        nan |     0.3083 |      0.9251 |      1.4578 |      0.2246 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4907 |        nan |     0.374  |      0.9201 |      1.6565 |      0.2687 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.6209 |        nan |     0.4748 |      0.902  |      1.9211 |      0.3415 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         1 |      0.3942 |        nan |     0.2871 |      0.8942 |      1.2465 |      0.2129 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4563 |        nan |     0.339  |      0.8678 |      1.3258 |      0.2505 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.565  |        nan |     0.4234 |      0.823  |      1.4286 |      0.3159 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.7254 |        nan |     0.5428 |      0.7694 |      1.555  |      0.4122 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.3786 |        nan |     0.2758 |      0.9279 |      1.3562 |      0.2034 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.432  |        nan |     0.323  |      0.9085 |      1.4528 |      0.2357 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.5238 |        nan |     0.3996 |      0.8766 |      1.581  |      0.2905 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.6738 |        nan |     0.5146 |      0.8272 |      1.7385 |      0.3797 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         1 |      0.3976 |        nan |     0.2952 |      0.8933 |      1.2481 |      0.217  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4578 |        nan |     0.3483 |      0.8641 |      1.3212 |      0.2549 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5599 |        nan |     0.4326 |      0.8068 |      1.413  |      0.3199 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.717  |        nan |     0.5538 |      0.7204 |      1.5227 |      0.4207 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         1 |      0.3947 |        nan |     0.2901 |      0.9002 |      1.2648 |      0.2137 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.4491 |        nan |     0.3357 |      0.8748 |      1.3297 |      0.2466 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5387 |        nan |     0.4056 |      0.8332 |      1.4098 |      0.3003 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.669  |        nan |     0.5068 |      0.7884 |      1.5059 |      0.38   |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         1 |      0.5398 |        nan |     0.4223 |      0.8027 |      1.3791 |      0.3121 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.603  |        nan |     0.4723 |      0.7551 |      1.4072 |      0.3539 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6831 |        nan |     0.5377 |      0.714  |      1.4473 |      0.4082 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.8101 |        nan |     0.6362 |      0.6539 |      1.5033 |      0.4945 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:fixed_mat  |         2 |      0.4143 |        nan |     0.3098 |      0.8783 |      1.2879 |      0.2284 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         4 |      0.5304 |        nan |     0.4006 |      0.8345 |      1.4114 |      0.2974 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:fixed_mat  |         8 |      0.6963 |        nan |     0.528  |      0.7805 |      1.5563 |      0.3979 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      0.3832 |        nan |     0.2855 |      0.9226 |      1.3374 |      0.2082 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      0.4604 |        nan |     0.35   |      0.9212 |      1.5697 |      0.2521 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      0.5916 |        nan |     0.453  |      0.9077 |      1.8668 |      0.3249 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         2 |      0.4161 |        nan |     0.3088 |      0.8756 |      1.2672 |      0.2288 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         4 |      0.5334 |        nan |     0.3988 |      0.8277 |      1.3897 |      0.2978 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_defl    |         8 |      0.6995 |        nan |     0.5232 |      0.7747 |      1.5331 |      0.3966 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.3961 |        nan |     0.295  |      0.9106 |      1.378  |      0.2166 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.4921 |        nan |     0.3752 |      0.8843 |      1.5306 |      0.2728 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.647  |        nan |     0.4938 |      0.8359 |      1.7098 |      0.3637 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         2 |      0.4169 |        nan |     0.3173 |      0.8756 |      1.2695 |      0.2321 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         4 |      0.5311 |        nan |     0.4088 |      0.8135 |      1.3799 |      0.302  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_ms      |         8 |      0.6933 |        nan |     0.5357 |      0.7309 |      1.505  |      0.4057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         2 |      0.411  |        nan |     0.309  |      0.8866 |      1.2868 |      0.2265 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         4 |      0.5115 |        nan |     0.3849 |      0.8412 |      1.3826 |      0.2848 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_proj    |         8 |      0.6458 |        nan |     0.4889 |      0.7942 |      1.4913 |      0.366  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         2 |      0.5792 |        nan |     0.4532 |      0.765  |      1.4031 |      0.3378 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         4 |      0.6702 |        nan |     0.5262 |      0.7212 |      1.4434 |      0.399  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_rev     |         8 |      0.7975 |        nan |     0.6256 |      0.6596 |      1.5    |      0.4858 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:fixed_mat  | load_x2    |               1 |               0 |       0.4188 |
| mssa:fixed_mat  | temp_plus5 |               1 |               0 |       0.8312 |
| mssa:neural_ssm | load_x2    |               1 |               0 |       0.3812 |
| mssa:neural_ssm | temp_plus5 |               1 |               0 |       0.5881 |
| mssa:no_defl    | load_x2    |               1 |               0 |       0.4084 |
| mssa:no_defl    | temp_plus5 |               1 |               0 |       0.8582 |
| mssa:no_disc    | load_x2    |               1 |               0 |       0.387  |
| mssa:no_disc    | temp_plus5 |               1 |               0 |       0.8759 |
| mssa:no_ms      | load_x2    |               1 |               0 |       0.4544 |
| mssa:no_ms      | temp_plus5 |               1 |               0 |       0.7859 |
| mssa:no_proj    | load_x2    |               1 |               0 |       0.4727 |
| mssa:no_proj    | temp_plus5 |               1 |               0 |       0.8076 |
| mssa:no_rev     | load_x2    |               1 |               0 |       0.3248 |
| mssa:no_rev     | temp_plus5 |               1 |               0 |       0.707  |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |     IS |
|:----------------|:----------|-------:|-------:|-------:|
| mssa:fixed_mat  | aci       | 0.9649 | 1.8926 | 2.225  |
| mssa:fixed_mat  | native    | 0.8955 | 1.2611 | 2.3972 |
| mssa:neural_ssm | aci       | 0.9697 | 1.8311 | 2.1499 |
| mssa:neural_ssm | native    | 0.9241 | 1.3194 | 2.1908 |
| mssa:no_defl    | aci       | 0.9649 | 1.9263 | 2.2517 |
| mssa:no_defl    | native    | 0.8908 | 1.2415 | 2.4759 |
| mssa:no_disc    | aci       | 0.9663 | 1.8449 | 2.1926 |
| mssa:no_disc    | native    | 0.9235 | 1.3493 | 2.1997 |
| mssa:no_ms      | aci       | 0.9651 | 1.9081 | 2.2083 |
| mssa:no_ms      | native    | 0.892  | 1.2436 | 2.4002 |
| mssa:no_proj    | aci       | 0.9661 | 1.9042 | 2.2301 |
| mssa:no_proj    | native    | 0.8968 | 1.2597 | 2.4002 |
| mssa:no_rev     | aci       | 0.9516 | 2.339  | 2.7284 |
| mssa:no_rev     | native    | 0.7961 | 1.3673 | 3.7663 |
