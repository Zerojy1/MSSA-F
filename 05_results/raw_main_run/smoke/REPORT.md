# MSSA-Rut experiment report

Run directory: `results/smoke`

## E1E2

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      2.4475 |        nan |     1.6656 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      2.4885 |        nan |     2.1605 |      0.9678 |     10.0675 |      1.433  |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         0 |      2.4952 |        nan |     2.218  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         0 |      4.7826 |        nan |     4.108  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      2.1616 |        nan |     1.7301 |      0.4644 |      2.3761 |      1.4703 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         0 |      4.8355 |        nan |     4.1667 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      4.8456 |        nan |     4.1825 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.9305 |        nan |     1.4041 |    nan      |    nan      |    nan      |             1.911  |                0.026  |                        nan |            nan    |             nan    |
| gbm_residual |       0.4 |      0.7794 |        nan |     0.6322 |    nan      |    nan      |    nan      |             0.8483 |                0.0735 |                        nan |            nan    |              15.35 |
| gbm_residual |       0.6 |      0.5832 |        nan |     0.4787 |    nan      |    nan      |    nan      |             0.5705 |                0.0464 |                        nan |            nan    |               9.54 |
| jtg_enkf     |       0.2 |      1.4647 |        nan |     1.2061 |      0.5731 |      2.7266 |      0.9198 |             1.5771 |                0      |                        nan |              1.4  |               7.27 |
| jtg_enkf     |       0.4 |      0.3918 |        nan |     0.3133 |      0.9008 |      1.3762 |      0.2278 |             0.1834 |                0      |                        nan |            nan    |               2.75 |
| jtg_enkf     |       0.6 |      0.5979 |        nan |     0.4592 |      0.608  |      1.0444 |      0.366  |             0.5789 |                0      |                        nan |            nan    |              13.41 |
| jtg_global   |       0.2 |      2.7283 |        nan |     2.5114 |    nan      |    nan      |    nan      |             3.2611 |                0      |                        nan |            nan    |             nan    |
| jtg_global   |       0.4 |      2.9472 |        nan |     2.7591 |    nan      |    nan      |    nan      |             3.2611 |                0      |                        nan |            nan    |             nan    |
| jtg_global   |       0.6 |      3.1302 |        nan |     2.9594 |    nan      |    nan      |    nan      |             3.2611 |                0      |                        nan |            nan    |             nan    |
| lstm         |       0.2 |      3.2967 |        nan |     2.5443 |    nan      |    nan      |    nan      |             3.9261 |                0.078  |                        nan |            nan    |             nan    |
| lstm         |       0.4 |      1.5207 |        nan |     1.2807 |    nan      |    nan      |    nan      |             2.0937 |                0.0386 |                        nan |            nan    |             nan    |
| lstm         |       0.6 |      0.8926 |        nan |     0.667  |    nan      |    nan      |    nan      |             0.9524 |                0      |                        nan |            nan    |             nan    |
| mssa         |       0.2 |      1.9113 |        nan |     1.5842 |      0.2464 |      1.1769 |      1.4325 |             2.2624 |                0.0029 |                          0 |             31.37 |             nan    |
| mssa         |       0.4 |      1.5912 |        nan |     1.3167 |      0.3053 |      1.1609 |      1.1747 |             1.8173 |                0.0077 |                          0 |            nan    |             nan    |
| mssa         |       0.6 |      1.1709 |        nan |     0.9981 |      0.3125 |      1.1012 |      0.8633 |             1.3061 |                0      |                          0 |            nan    |             nan    |
| patchtst     |       0.2 |      3.3326 |        nan |     2.5815 |    nan      |    nan      |    nan      |             4.0228 |                0.1502 |                        nan |            nan    |             nan    |
| patchtst     |       0.4 |      1.5831 |        nan |     1.3394 |    nan      |    nan      |    nan      |             2.1905 |                0.1042 |                        nan |            nan    |             nan    |
| patchtst     |       0.6 |      0.9363 |        nan |     0.7076 |    nan      |    nan      |    nan      |             1.0491 |                0.0519 |                        nan |            nan    |             nan    |
| persistence  |       0.2 |      3.3654 |        nan |     2.6284 |    nan      |    nan      |    nan      |             3.9807 |                0      |                        nan |            nan    |             nan    |
| persistence  |       0.4 |      1.5846 |        nan |     1.3621 |    nan      |    nan      |    nan      |             2.1483 |                0      |                        nan |            nan    |             nan    |
| persistence  |       0.6 |      0.9252 |        nan |     0.6919 |    nan      |    nan      |    nan      |             1.007  |                0      |                        nan |            nan    |             nan    |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4679 |        nan |     0.3362 |      0.9745 |      2.3089 |      0.2567 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.503  |        nan |     0.3546 |      0.9601 |      2.3089 |      0.2735 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5654 |        nan |     0.4075 |      0.9544 |      2.3089 |      0.3031 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6327 |        nan |     0.4792 |      0.9223 |      2.3089 |      0.3479 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4248 |        nan |     0.3187 |      0.7222 |      0.8349 |      0.2448 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.48   |        nan |     0.3666 |      0.669  |      0.8648 |      0.2843 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5628 |        nan |     0.4346 |      0.6019 |      0.9368 |      0.3411 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7126 |        nan |     0.5234 |      0.5664 |      1.0897 |      0.4167 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      2.503  |        nan |     2.2282 |      0.6528 |      5.3086 |      1.6216 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         3 |      2.5191 |        nan |     2.25   |      0.6479 |      5.3086 |      1.6379 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         6 |      2.5432 |        nan |     2.2812 |      0.6403 |      5.3086 |      1.6622 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |        12 |      2.589  |        nan |     2.3379 |      0.6241 |      5.3086 |      1.7074 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.3959 |        nan |     0.2662 |      0.9653 |      1.8812 |      0.2113 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         3 |      0.4606 |        nan |     0.3204 |      0.939  |      1.8812 |      0.2439 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         6 |      0.5196 |        nan |     0.3785 |      0.9233 |      1.8812 |      0.2801 |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |        12 |      0.5304 |        nan |     0.3918 |      0.8972 |      1.8812 |      0.2894 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.5016 |        nan |     0.4018 |      0.6296 |      0.9171 |      0.3106 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.6566 |        nan |     0.5352 |      0.5188 |      0.9864 |      0.4286 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.7953 |        nan |     0.6546 |      0.4269 |      1.0272 |      0.5382 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.965  |        nan |     0.8054 |      0.3559 |      1.0616 |      0.678  |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3769 |        nan |     0.267  |      0.9676 |      1.7514 |      0.2035 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         3 |      0.4417 |        nan |     0.3217 |      0.9366 |      1.7514 |      0.2372 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         6 |      0.4729 |        nan |     0.34   |      0.9257 |      1.7514 |      0.2537 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |        12 |      0.5087 |        nan |     0.3751 |      0.8972 |      1.7514 |      0.2777 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4181 |        nan |     0.2789 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.54   |        nan |     0.3788 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7135 |        nan |     0.5138 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.0135 |        nan |     0.7396 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4679 |        nan |     0.3362 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.4935 |        nan |     0.3529 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.5017 |        nan |     0.3603 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5904 |        nan |     0.4141 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4248 |        nan |     0.3187 |      0.7222 |      0.8349 |      0.2448 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4407 |        nan |     0.3262 |      0.7431 |      0.8719 |      0.2481 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4556 |        nan |     0.3399 |      0.7245 |      0.9217 |      0.2603 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5008 |        nan |     0.3688 |      0.7569 |      1.0039 |      0.2783 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         1 |      2.503  |        nan |     2.2282 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      2.503  |        nan |     2.2282 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      2.503  |        nan |     2.2282 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      2.503  |        nan |     2.2282 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         1 |      0.3959 |        nan |     0.2662 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.4323 |        nan |     0.284  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.5089 |        nan |     0.3406 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.655  |        nan |     0.4279 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.5016 |        nan |     0.4018 |      0.6296 |      0.9171 |      0.3106 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.608  |        nan |     0.4891 |      0.5509 |      0.9519 |      0.3908 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.755  |        nan |     0.6096 |      0.4722 |      0.9939 |      0.5033 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.9375 |        nan |     0.7589 |      0.4074 |      1.0466 |      0.6429 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         1 |      0.3769 |        nan |     0.267  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.4114 |        nan |     0.2819 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4982 |        nan |     0.3424 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.6407 |        nan |     0.427  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.4181 |        nan |     0.2789 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4734 |        nan |     0.304  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5659 |        nan |     0.3724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7441 |        nan |     0.4841 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4678 |        nan |     0.3484 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4808 |        nan |     0.3476 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5634 |        nan |     0.3978 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4063 |        nan |     0.3    |      0.7742 |      0.8638 |      0.2282 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4408 |        nan |     0.3266 |      0.7354 |      0.9103 |      0.2501 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.4798 |        nan |     0.3587 |      0.7652 |      0.9921 |      0.2695 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         2 |      2.4964 |        nan |     2.2066 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         4 |      2.4959 |        nan |     2.2115 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_global   |         8 |      2.4997 |        nan |     2.2176 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         2 |      0.3868 |        nan |     0.2647 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         4 |      0.4929 |        nan |     0.3281 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| lstm         |         8 |      0.6247 |        nan |     0.4112 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.5558 |        nan |     0.4438 |      0.5899 |      0.9318 |      0.3522 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.7373 |        nan |     0.5925 |      0.4831 |      0.9822 |      0.4893 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.9226 |        nan |     0.7453 |      0.4142 |      1.0406 |      0.6313 |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         2 |      0.3804 |        nan |     0.2742 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         4 |      0.4936 |        nan |     0.3384 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| patchtst     |         8 |      0.6083 |        nan |     0.4109 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4223 |        nan |     0.2777 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5424 |        nan |     0.3559 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7164 |        nan |     0.4666 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |          -0.0511 |  -1.3872 |    1.1265 |                       2 |              3 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.2047 |  -1.5671 |    0.9985 |                       1 |              3 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.6898 |  -1.1326 |   -0.067  |                       0 |              3 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.5223 |  -1.0219 |    0.1057 |                       1 |              3 |
| horizon           |       1   | gbm_residual | mssa        |          -0.0183 |  -0.1865 |    0.1326 |                       1 |              3 |
| horizon           |       3   | gbm_residual | mssa        |          -0.1235 |  -0.3552 |    0.0961 |                       1 |              3 |
| horizon           |       6   | gbm_residual | mssa        |          -0.1894 |  -0.5001 |    0.0847 |                       1 |              3 |
| horizon           |      12   | gbm_residual | mssa        |          -0.27   |  -0.6091 |    0.1199 |                       1 |              3 |
| sparse_all        |       1   | gbm_residual | mssa        |          -0.0183 |  -0.1865 |    0.1326 |                       1 |              3 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0836 |  -0.3334 |    0.1129 |                       1 |              3 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.2113 |  -0.5127 |    0.0784 |                       1 |              3 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.2958 |  -0.7501 |    0.0646 |                       1 |              3 |
| sparse_unobserved |       2   | gbm_residual | mssa        |          -0.0566 |  -0.3178 |    0.1216 |                       2 |              3 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.2135 |  -0.4807 |    0.0607 |                       1 |              3 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.307  |  -0.7495 |    0.0442 |                       1 |              3 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.4186 |  -1.3897 |    1.3753 |                       2 |              3 |
| early_life        |       0.2 | jtg_enkf     | mssa        |          -0.3996 |  -0.8689 |   -0.0106 |                       0 |              3 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -1.0263 |  -1.7256 |   -0.0051 |                       0 |              3 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.5482 |  -1.1313 |    0.0441 |                       1 |              3 |
| horizon           |       1   | jtg_enkf     | mssa        |          -0.0654 |  -0.2301 |    0.0484 |                       1 |              3 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.1505 |  -0.3815 |    0.0374 |                       1 |              3 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.1928 |  -0.464  |    0.0544 |                       1 |              3 |
| horizon           |      12   | jtg_enkf     | mssa        |          -0.1999 |  -0.4984 |    0.0982 |                       1 |              3 |
| sparse_all        |       1   | jtg_enkf     | mssa        |          -0.0654 |  -0.2301 |    0.0484 |                       1 |              3 |
| sparse_all        |       2   | jtg_enkf     | mssa        |          -0.1396 |  -0.3901 |    0.0392 |                       1 |              3 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.2541 |  -0.5225 |    0.0394 |                       1 |              3 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.3651 |  -0.7422 |    0.056  |                       1 |              3 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |          -0.1198 |  -0.365  |    0.0389 |                       1 |              3 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.2507 |  -0.4865 |    0.0335 |                       1 |              3 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.3701 |  -0.7312 |    0.0532 |                       1 |              3 |
| cold_start        |       0   | jtg_global   | mssa        |           0.4883 |  -0.6833 |    1.0991 |                       2 |              3 |
| early_life        |       0.2 | jtg_global   | mssa        |           0.9114 |   0.3144 |    1.2192 |                       3 |              3 |
| early_life        |       0.4 | jtg_global   | mssa        |           1.4016 |   0.9654 |    1.8852 |                       3 |              3 |
| early_life        |       0.6 | jtg_global   | mssa        |           1.9275 |   1.4068 |    2.7417 |                       3 |              3 |
| horizon           |       1   | jtg_global   | mssa        |           1.9231 |   1.3033 |    2.7119 |                       3 |              3 |
| horizon           |       3   | jtg_global   | mssa        |           1.7987 |   1.2697 |    2.5094 |                       3 |              3 |
| horizon           |       6   | jtg_global   | mssa        |           1.6989 |   1.2576 |    2.3577 |                       3 |              3 |
| horizon           |      12   | jtg_global   | mssa        |           1.5907 |   1.2417 |    2.212  |                       3 |              3 |
| sparse_all        |       1   | jtg_global   | mssa        |           1.9231 |   1.3033 |    2.7119 |                       3 |              3 |
| sparse_all        |       2   | jtg_global   | mssa        |           1.8344 |   1.301  |    2.5223 |                       3 |              3 |
| sparse_all        |       4   | jtg_global   | mssa        |           1.7037 |   1.2846 |    2.3642 |                       3 |              3 |
| sparse_all        |       8   | jtg_global   | mssa        |           1.5484 |   1.268  |    2.0996 |                       3 |              3 |
| sparse_unobserved |       2   | jtg_global   | mssa        |           1.8765 |   1.2935 |    2.5739 |                       3 |              3 |
| sparse_unobserved |       4   | jtg_global   | mssa        |           1.7102 |   1.2656 |    2.3741 |                       3 |              3 |
| sparse_unobserved |       8   | jtg_global   | mssa        |           1.5547 |   1.2524 |    2.11   |                       3 |              3 |
| cold_start        |       0   | lstm         | mssa        |           2.54   |   1.1279 |    3.9246 |                       3 |              3 |
| early_life        |       0.2 | lstm         | mssa        |           1.0934 |  -1.0819 |    3.0392 |                       2 |              3 |
| early_life        |       0.4 | lstm         | mssa        |           0.0573 |  -0.4696 |    0.5717 |                       2 |              3 |
| early_life        |       0.6 | lstm         | mssa        |          -0.2947 |  -0.9356 |    0.1293 |                       1 |              3 |
| horizon           |       1   | lstm         | mssa        |          -0.0944 |  -0.2527 |    0.018  |                       1 |              3 |
| horizon           |       3   | lstm         | mssa        |          -0.1689 |  -0.3717 |    0.0133 |                       1 |              3 |
| horizon           |       6   | lstm         | mssa        |          -0.2357 |  -0.458  |    0.0031 |                       1 |              3 |
| horizon           |      12   | lstm         | mssa        |          -0.3752 |  -0.6018 |   -0.0074 |                       0 |              3 |
| sparse_all        |       1   | lstm         | mssa        |          -0.0944 |  -0.2527 |    0.018  |                       1 |              3 |
| sparse_all        |       2   | lstm         | mssa        |          -0.1484 |  -0.3829 |    0.02   |                       1 |              3 |
| sparse_all        |       4   | lstm         | mssa        |          -0.206  |  -0.4822 |    0.0538 |                       1 |              3 |
| sparse_all        |       8   | lstm         | mssa        |          -0.2302 |  -0.6734 |    0.1139 |                       1 |              3 |
| sparse_unobserved |       2   | lstm         | mssa        |          -0.1376 |  -0.3796 |    0.0353 |                       1 |              3 |
| sparse_unobserved |       4   | lstm         | mssa        |          -0.2024 |  -0.4429 |    0.0512 |                       1 |              3 |
| sparse_unobserved |       8   | lstm         | mssa        |          -0.2411 |  -0.6633 |    0.1049 |                       1 |              3 |
| cold_start        |       0   | patchtst     | mssa        |           2.6011 |   1.2229 |    3.9683 |                       3 |              3 |
| early_life        |       0.2 | patchtst     | mssa        |           1.1446 |  -1.0005 |    3.0716 |                       2 |              3 |
| early_life        |       0.4 | patchtst     | mssa        |           0.1206 |  -0.3721 |    0.6183 |                       2 |              3 |
| early_life        |       0.6 | patchtst     | mssa        |          -0.2431 |  -0.8619 |    0.1607 |                       1 |              3 |
| horizon           |       1   | patchtst     | mssa        |          -0.1125 |  -0.2664 |    0.004  |                       1 |              3 |
| horizon           |       3   | patchtst     | mssa        |          -0.1881 |  -0.3987 |   -0.0026 |                       0 |              3 |
| horizon           |       6   | patchtst     | mssa        |          -0.2776 |  -0.5193 |    0.0054 |                       1 |              3 |
| horizon           |      12   | patchtst     | mssa        |          -0.3916 |  -0.6708 |    0.0171 |                       1 |              3 |
| sparse_all        |       1   | patchtst     | mssa        |          -0.1125 |  -0.2664 |    0.004  |                       1 |              3 |
| sparse_all        |       2   | patchtst     | mssa        |          -0.168  |  -0.4078 |    0.0136 |                       1 |              3 |
| sparse_all        |       4   | patchtst     | mssa        |          -0.2151 |  -0.4823 |    0.0506 |                       1 |              3 |
| sparse_all        |       8   | patchtst     | mssa        |          -0.2376 |  -0.6644 |    0.1276 |                       1 |              3 |
| sparse_unobserved |       2   | patchtst     | mssa        |          -0.1436 |  -0.3982 |    0.0406 |                       1 |              3 |
| sparse_unobserved |       4   | patchtst     | mssa        |          -0.2    |  -0.4321 |    0.0621 |                       1 |              3 |
| sparse_unobserved |       8   | patchtst     | mssa        |          -0.2511 |  -0.658  |    0.1199 |                       1 |              3 |
| cold_start        |       0   | persistence  | mssa        |           2.61   |   1.2096 |    3.9856 |                       3 |              3 |
| early_life        |       0.2 | persistence  | mssa        |           1.1697 |  -1.0106 |    3.1251 |                       2 |              3 |
| early_life        |       0.4 | persistence  | mssa        |           0.1236 |  -0.381  |    0.632  |                       2 |              3 |
| early_life        |       0.6 | persistence  | mssa        |          -0.2602 |  -0.8995 |    0.1542 |                       1 |              3 |
| horizon           |       1   | persistence  | mssa        |          -0.0747 |  -0.261  |    0.0415 |                       1 |              3 |
| horizon           |       3   | persistence  | mssa        |          -0.0929 |  -0.3485 |    0.089  |                       1 |              3 |
| horizon           |       6   | persistence  | mssa        |          -0.0517 |  -0.4107 |    0.1784 |                       2 |              3 |
| horizon           |      12   | persistence  | mssa        |           0.0946 |  -0.3281 |    0.3896 |                       2 |              3 |
| sparse_all        |       1   | persistence  | mssa        |          -0.0747 |  -0.261  |    0.0415 |                       1 |              3 |
| sparse_all        |       2   | persistence  | mssa        |          -0.1108 |  -0.3792 |    0.0534 |                       1 |              3 |
| sparse_all        |       4   | persistence  | mssa        |          -0.1559 |  -0.4844 |    0.0975 |                       1 |              3 |
| sparse_all        |       8   | persistence  | mssa        |          -0.1534 |  -0.6637 |    0.178  |                       2 |              3 |
| sparse_unobserved |       2   | persistence  | mssa        |          -0.1077 |  -0.3933 |    0.0517 |                       2 |              3 |
| sparse_unobserved |       4   | persistence  | mssa        |          -0.1594 |  -0.4516 |    0.0794 |                       1 |              3 |
| sparse_unobserved |       8   | persistence  | mssa        |          -0.1625 |  -0.6535 |    0.1635 |                       2 |              3 |

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|
| gbm_residual |         0 |      1.675  |        nan |     1.4588 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         0 |      1.3659 |        nan |     1.2447 |      0.8627 |      7.1389 |      0.8891 |                nan |                   nan |                        nan |               nan |
| mssa         |         0 |      0.6654 |        nan |     0.5636 |      0.9588 |      2.472  |      0.383  |                nan |                   nan |                        nan |               nan |
| persistence  |         0 |      3.8936 |        nan |     3.576  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|
| gbm_residual |       0.2 |      0.6917 |        nan |     0.5783 |    nan      |    nan      |    nan      |             0.545  |                0.0259 |                        nan |            nan    |
| gbm_residual |       0.4 |      0.3401 |        nan |     0.2739 |    nan      |    nan      |    nan      |             0.1651 |                0.05   |                        nan |            nan    |
| gbm_residual |       0.6 |      0.5066 |        nan |     0.4449 |    nan      |    nan      |    nan      |             0.3262 |                0.0347 |                        nan |            nan    |
| jtg_enkf     |       0.2 |      2.2605 |        nan |     1.9425 |      0.2229 |      2.7323 |      1.5603 |             3.0404 |                0      |                        nan |             22.06 |
| jtg_enkf     |       0.4 |      0.5513 |        nan |     0.4315 |      0.7833 |      1.31   |      0.314  |             0.6003 |                0      |                        nan |              0.78 |
| jtg_enkf     |       0.6 |      0.4181 |        nan |     0.3421 |      0.7386 |      0.9963 |      0.2514 |             0.4185 |                0      |                        nan |              0.42 |
| mssa         |       0.2 |      0.5349 |        nan |     0.4517 |      0.6857 |      1.1864 |      0.3332 |             0.5018 |                0.0029 |                          0 |            nan    |
| mssa         |       0.4 |      0.4555 |        nan |     0.3799 |      0.7719 |      1.1704 |      0.2751 |             0.3866 |                0      |                          0 |            nan    |
| mssa         |       0.6 |      0.3829 |        nan |     0.3115 |      0.8409 |      1.1305 |      0.2236 |             0.2467 |                0      |                          0 |            nan    |
| persistence  |       0.2 |      1.7976 |        nan |     1.5469 |    nan      |    nan      |    nan      |             2.517  |                0      |                        nan |            nan    |
| persistence  |       0.4 |      0.9489 |        nan |     0.8221 |    nan      |    nan      |    nan      |             1.3753 |                0      |                        nan |            nan    |
| persistence  |       0.6 |      0.4409 |        nan |     0.3627 |    nan      |    nan      |    nan      |             0.4747 |                0      |                        nan |            nan    |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|
| gbm_residual |         1 |      0.4165 |        nan |     0.314  |      0.9862 |      2.4154 |      0.2412 |                nan |                   nan |                        nan |               nan |
| gbm_residual |         3 |      0.4447 |        nan |     0.3246 |      0.9813 |      2.4154 |      0.2527 |                nan |                   nan |                        nan |               nan |
| gbm_residual |         6 |      0.4794 |        nan |     0.371  |      0.9809 |      2.4154 |      0.271  |                nan |                   nan |                        nan |               nan |
| gbm_residual |        12 |      0.5276 |        nan |     0.398  |      0.9601 |      2.4154 |      0.2935 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         1 |      0.3546 |        nan |     0.2695 |      0.7972 |      0.8273 |      0.2    |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         3 |      0.3909 |        nan |     0.2999 |      0.75   |      0.8484 |      0.2242 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         6 |      0.4318 |        nan |     0.335  |      0.7088 |      0.893  |      0.2523 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |        12 |      0.5318 |        nan |     0.3899 |      0.6933 |      0.9889 |      0.3002 |                nan |                   nan |                        nan |               nan |
| mssa         |         1 |      0.3329 |        nan |     0.2434 |      0.8618 |      0.9694 |      0.1815 |                nan |                   nan |                        nan |               nan |
| mssa         |         3 |      0.3956 |        nan |     0.2995 |      0.8341 |      1.0408 |      0.2229 |                nan |                   nan |                        nan |               nan |
| mssa         |         6 |      0.4386 |        nan |     0.3336 |      0.8091 |      1.0803 |      0.2489 |                nan |                   nan |                        nan |               nan |
| mssa         |        12 |      0.4986 |        nan |     0.3745 |      0.788  |      1.1087 |      0.2833 |                nan |                   nan |                        nan |               nan |
| persistence  |         1 |      0.3695 |        nan |     0.2608 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         3 |      0.4754 |        nan |     0.3539 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         6 |      0.6135 |        nan |     0.4605 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |        12 |      0.8763 |        nan |     0.636  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|
| gbm_residual |         1 |      0.4165 |        nan |     0.314  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| gbm_residual |         2 |      0.4138 |        nan |     0.314  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| gbm_residual |         4 |      0.402  |        nan |     0.3049 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| gbm_residual |         8 |      0.4172 |        nan |     0.3269 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         1 |      0.3546 |        nan |     0.2695 |      0.7972 |      0.8273 |      0.2    |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         2 |      0.3788 |        nan |     0.2839 |      0.8226 |      0.8612 |      0.2105 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         4 |      0.3605 |        nan |     0.2718 |      0.8318 |      0.9093 |      0.2005 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         8 |      0.4181 |        nan |     0.3199 |      0.8226 |      0.9908 |      0.2349 |                nan |                   nan |                        nan |               nan |
| mssa         |         1 |      0.3329 |        nan |     0.2434 |      0.8618 |      0.9694 |      0.1815 |                nan |                   nan |                        nan |               nan |
| mssa         |         2 |      0.3492 |        nan |     0.262  |      0.8618 |      1.0052 |      0.1944 |                nan |                   nan |                        nan |               nan |
| mssa         |         4 |      0.3791 |        nan |     0.2877 |      0.841  |      1.0477 |      0.2127 |                nan |                   nan |                        nan |               nan |
| mssa         |         8 |      0.428  |        nan |     0.3234 |      0.8226 |      1.0997 |      0.2409 |                nan |                   nan |                        nan |               nan |
| persistence  |         1 |      0.3695 |        nan |     0.2608 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         2 |      0.3914 |        nan |     0.2841 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         4 |      0.4378 |        nan |     0.3258 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         8 |      0.5664 |        nan |     0.3982 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|
| gbm_residual |         2 |      0.408  |        nan |     0.3171 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| gbm_residual |         4 |      0.3764 |        nan |     0.2906 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| gbm_residual |         8 |      0.4061 |        nan |     0.3188 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         2 |      0.3341 |        nan |     0.2571 |      0.8394 |      0.8556 |      0.1886 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         4 |      0.3433 |        nan |     0.2592 |      0.8528 |      0.9015 |      0.1904 |                nan |                   nan |                        nan |               nan |
| jtg_enkf     |         8 |      0.412  |        nan |     0.3171 |      0.8263 |      0.9831 |      0.2323 |                nan |                   nan |                        nan |               nan |
| mssa         |         2 |      0.3087 |        nan |     0.2282 |      0.8761 |      0.9845 |      0.1702 |                nan |                   nan |                        nan |               nan |
| mssa         |         4 |      0.3699 |        nan |     0.2746 |      0.8497 |      1.0359 |      0.2048 |                nan |                   nan |                        nan |               nan |
| mssa         |         8 |      0.428  |        nan |     0.3211 |      0.8211 |      1.0938 |      0.24   |                nan |                   nan |                        nan |               nan |
| persistence  |         2 |      0.3648 |        nan |     0.2563 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         4 |      0.4068 |        nan |     0.3036 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |
| persistence  |         8 |      0.543  |        nan |     0.3852 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.9472 |   0.3793 |    1.4121 |                       3 |              3 |
| early_life        |       0.2 | gbm_residual | mssa        |           0.1407 |  -0.0397 |    0.3676 |                       2 |              3 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.112  |  -0.198  |   -0.0604 |                       0 |              3 |
| early_life        |       0.6 | gbm_residual | mssa        |           0.1241 |   0.0302 |    0.203  |                       3 |              3 |
| horizon           |       1   | gbm_residual | mssa        |           0.0832 |   0.0524 |    0.0996 |                       3 |              3 |
| horizon           |       3   | gbm_residual | mssa        |           0.0494 |   0.0161 |    0.0708 |                       3 |              3 |
| horizon           |       6   | gbm_residual | mssa        |           0.0419 |   0.0145 |    0.0569 |                       3 |              3 |
| horizon           |      12   | gbm_residual | mssa        |           0.032  |  -0.0639 |    0.1224 |                       2 |              3 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0832 |   0.0524 |    0.0996 |                       3 |              3 |
| sparse_all        |       2   | gbm_residual | mssa        |           0.0644 |   0.032  |    0.084  |                       3 |              3 |
| sparse_all        |       4   | gbm_residual | mssa        |           0.0235 |  -0.008  |    0.0535 |                       2 |              3 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.0089 |  -0.0555 |    0.0338 |                       1 |              3 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0982 |   0.0837 |    0.1199 |                       3 |              3 |
| sparse_unobserved |       4   | gbm_residual | mssa        |           0.0073 |  -0.0141 |    0.0368 |                       1 |              3 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.0201 |  -0.0655 |    0.0194 |                       1 |              3 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.6435 |   0.3318 |    1.2202 |                       3 |              3 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.5857 |   0.7647 |    2.6965 |                       3 |              3 |
| early_life        |       0.4 | jtg_enkf     | mssa        |           0.0573 |  -0.1467 |    0.4084 |                       1 |              3 |
| early_life        |       0.6 | jtg_enkf     | mssa        |           0.0392 |  -0.0037 |    0.1122 |                       2 |              3 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.022  |   0.0125 |    0.0353 |                       3 |              3 |
| horizon           |       3   | jtg_enkf     | mssa        |          -0.0042 |  -0.0137 |    0.0098 |                       1 |              3 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0065 |  -0.0221 |    0.0093 |                       1 |              3 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.0297 |  -0.0289 |    0.079  |                       2 |              3 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.022  |   0.0125 |    0.0353 |                       3 |              3 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.0293 |   0.0212 |    0.0368 |                       3 |              3 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0175 |  -0.0312 |    0.0091 |                       1 |              3 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0082 |  -0.0687 |    0.0381 |                       2 |              3 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0253 |   0.0212 |    0.0283 |                       3 |              3 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0256 |  -0.0441 |    0.0083 |                       1 |              3 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0146 |  -0.0778 |    0.0393 |                       1 |              3 |
| cold_start        |       0   | persistence  | mssa        |           3.1989 |   2.5303 |    3.6246 |                       3 |              3 |
| early_life        |       0.2 | persistence  | mssa        |           1.2185 |   0.7221 |    1.5719 |                       3 |              3 |
| early_life        |       0.4 | persistence  | mssa        |           0.4913 |   0.4015 |    0.5841 |                       3 |              3 |
| early_life        |       0.6 | persistence  | mssa        |           0.0527 |  -0.0883 |    0.1605 |                       2 |              3 |
| horizon           |       1   | persistence  | mssa        |           0.0353 |   0.0117 |    0.0681 |                       3 |              3 |
| horizon           |       3   | persistence  | mssa        |           0.0791 |   0.0548 |    0.1194 |                       3 |              3 |
| horizon           |       6   | persistence  | mssa        |           0.1744 |   0.146  |    0.2194 |                       3 |              3 |
| horizon           |      12   | persistence  | mssa        |           0.3786 |   0.3452 |    0.4345 |                       3 |              3 |
| sparse_all        |       1   | persistence  | mssa        |           0.0353 |   0.0117 |    0.0681 |                       3 |              3 |
| sparse_all        |       2   | persistence  | mssa        |           0.0406 |   0.006  |    0.0806 |                       3 |              3 |
| sparse_all        |       4   | persistence  | mssa        |           0.0585 |   0.02   |    0.0783 |                       3 |              3 |
| sparse_all        |       8   | persistence  | mssa        |           0.1394 |   0.0967 |    0.1634 |                       3 |              3 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0523 |   0.0183 |    0.0989 |                       3 |              3 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0368 |  -0.0008 |    0.0639 |                       2 |              3 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.1163 |   0.0635 |    0.1448 |                       3 |              3 |

## E6_ablation

### cold_start

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:neural_ssm |         0 |     11.3189 |        nan |     7.296  |      0.2529 |      2.7574 |      6.954  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         0 |      2.1973 |        nan |     1.7493 |      0.4552 |      2.3742 |      1.4931 |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:neural_ssm |       0.2 |     12.7641 |        nan |     9.2666 |      0.0716 |      1.6995 |      9.0252 |            18.9776 |                0      |                          0 |              3.3  |              16.77 |
| mssa:neural_ssm |       0.4 |     11.2992 |        nan |     9.0253 |      0.0229 |      1.6446 |      8.7894 |            16.2376 |                0      |                          0 |            nan    |              13.68 |
| mssa:neural_ssm |       0.6 |      7.6123 |        nan |     6.1652 |      0.0057 |      1.4165 |      5.9614 |            11.0806 |                0      |                          0 |            nan    |               2.75 |
| mssa:no_disc    |       0.2 |      1.9403 |        nan |     1.6006 |      0.255  |      1.1754 |      1.4507 |             2.2845 |                0      |                          0 |             32.16 |             nan    |
| mssa:no_disc    |       0.4 |      1.6159 |        nan |     1.333  |      0.3053 |      1.1596 |      1.192  |             1.8346 |                0.0077 |                          0 |            nan    |             nan    |
| mssa:no_disc    |       0.6 |      1.1858 |        nan |     1.008  |      0.3182 |      1.1001 |      0.8738 |             1.3163 |                0      |                          0 |            nan    |             nan    |

### horizon

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:neural_ssm |         1 |      1.0031 |        nan |     0.8534 |      0.2662 |      1.0256 |      0.7259 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         3 |      1.609  |        nan |     1.3592 |      0.1831 |      1.1243 |      1.212  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         6 |      2.2954 |        nan |     1.9171 |      0.1463 |      1.1953 |      1.7563 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |        12 |      3.3941 |        nan |     2.7978 |      0.1028 |      1.2741 |      2.6211 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.5046 |        nan |     0.4045 |      0.6204 |      0.9162 |      0.3132 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         3 |      0.6617 |        nan |     0.5393 |      0.5164 |      0.9853 |      0.4327 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         6 |      0.8024 |        nan |     0.6602 |      0.4269 |      1.026  |      0.5439 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |        12 |      0.9749 |        nan |     0.8129 |      0.3584 |      1.0604 |      0.6857 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:neural_ssm |         1 |      1.0031 |        nan |     0.8534 |      0.2662 |      1.0256 |      0.7259 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         2 |      4.0646 |        nan |     2.6484 |      0.2106 |      1.0728 |      2.5124 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      6.8439 |        nan |     4.4195 |      0.1921 |      1.1333 |      4.2738 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      8.771  |        nan |     5.667  |      0.1968 |      1.2131 |      5.5094 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         1 |      0.5046 |        nan |     0.4045 |      0.6204 |      0.9162 |      0.3132 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.6132 |        nan |     0.4934 |      0.5486 |      0.9508 |      0.3949 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.7639 |        nan |     0.617  |      0.4676 |      0.9928 |      0.5103 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.9498 |        nan |     0.7684 |      0.4028 |      1.0454 |      0.6524 |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model           |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:----------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| mssa:neural_ssm |         2 |      3.7586 |        nan |     2.4148 |      0.2396 |      1.0448 |      2.2873 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         4 |      6.6437 |        nan |     4.2693 |      0.1908 |      1.1153 |      4.1278 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:neural_ssm |         8 |      8.7082 |        nan |     5.597  |      0.2005 |      1.2027 |      5.4419 |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         2 |      0.5606 |        nan |     0.4479 |      0.5853 |      0.9308 |      0.356  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         4 |      0.7457 |        nan |     0.5996 |      0.4769 |      0.9811 |      0.496  |                nan |                   nan |                        nan |               nan |                nan |
| mssa:no_disc    |         8 |      0.9348 |        nan |     0.7547 |      0.409  |      1.0394 |      0.6406 |                nan |                   nan |                        nan |               nan |                nan |

## Counterfactual physical consistency (E4) [E1E2]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8296 |          0.1429 |       0.0661 |
| gbm_residual | temp_plus5 |          0.6466 |          0      |       0.0481 |
| jtg_enkf     | load_x2    |          0.5338 |          0.4637 |       0.0294 |
| jtg_enkf     | temp_plus5 |          0.7193 |          0.2807 |       0.05   |
| jtg_global   | load_x2    |          1      |          0      |       1.4832 |
| jtg_global   | temp_plus5 |          1      |          0      |       2.5253 |
| lstm         | load_x2    |          0.8368 |          0.1632 |       0.5644 |
| lstm         | temp_plus5 |          0.9034 |          0.0966 |       0.0581 |
| mssa         | load_x2    |          1      |          0      |       0.5033 |
| mssa         | temp_plus5 |          1      |          0      |       0.6475 |
| patchtst     | load_x2    |          0.9126 |          0.0874 |       0.6349 |
| patchtst     | temp_plus5 |          0.8069 |          0.1931 |       0.0138 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.5461 |          0.4539 |      -0.022  |
| gbm_residual | temp_plus5 |          0.6284 |          0      |       0.0612 |
| jtg_enkf     | load_x2    |          0.4963 |          0.5037 |       0.0336 |
| jtg_enkf     | temp_plus5 |          0.788  |          0.212  |       0.0458 |
| mssa         | load_x2    |          1      |          0      |       0.4592 |
| mssa         | temp_plus5 |          1      |          0      |       0.6113 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Counterfactual physical consistency (E4) [E6_ablation]

| model           | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:----------------|:-----------|----------------:|----------------:|-------------:|
| mssa:neural_ssm | load_x2    |          1      |          0      |       2.2325 |
| mssa:neural_ssm | temp_plus5 |          0.1918 |          0.8082 |      -0.0089 |
| mssa:no_disc    | load_x2    |          1      |          0      |       0.4992 |
| mssa:no_disc    | temp_plus5 |          1      |          0      |       0.6452 |

## Native vs ACI intervals [E1E2]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9425 | 2.0543 | 2.4665 |
| jtg_enkf | native    | 0.7084 | 0.8251 | 3.7133 |
| mssa     | aci       | 0.9627 | 1.9682 | 2.2801 |
| mssa     | native    | 0.6049 | 0.9134 | 4.9689 |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9469 | 1.6628 | 2.0975 |
| jtg_enkf | native    | 0.7871 | 0.8191 | 2.6385 |
| mssa     | aci       | 0.953  | 1.7338 | 2.02   |
| mssa     | native    | 0.854  | 0.9654 | 2.1335 |

## Native vs ACI intervals [E6_ablation]

| model           | setting   |   PICP |   MPIW |      IS |
|:----------------|:----------|-------:|-------:|--------:|
| mssa:neural_ssm | aci       | 0.9325 | 2.786  |  3.3794 |
| mssa:neural_ssm | native    | 0.2311 | 1.022  | 17.9414 |
| mssa:no_disc    | aci       | 0.9627 | 1.9615 |  2.2716 |
| mssa:no_disc    | native    | 0.5948 | 0.9124 |  5.048  |

## First-passage Monte Carlo [E1E2]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.6667 |                  15.06 |
|    0.2 |          10 |           0.3333 |                 nan    |
|    0.4 |           8 |           0.5    |                 nan    |
|    0.4 |          10 |           0.1933 |                 nan    |
|    0.6 |           8 |           0.5    |                 nan    |
|    0.6 |          10 |           0.3133 |                  14.93 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.56   |                   2.34 |
|    0.2 |          10 |           0      |                 nan    |
|    0.4 |           8 |           0.4667 |                   2.76 |
|    0.4 |          10 |           0      |                 nan    |
|    0.6 |           8 |           0.44   |                   1.94 |
|    0.6 |          10 |           0      |                 nan    |

## E0 synthetic identifiability

| exp   |   seed |   sig_m_true |   beta_true |   beta_hat |   gamma_true |   gamma_hat |   phi_true |   phi_hat |   sig_m_hat |   sig_r_true |   sig_r_hat |   u_spearman |   u_rmse |   Rperm_rmse |   rev_rmse |   rev_sd_true |
|:------|-------:|-------------:|------------:|-----------:|-------------:|------------:|-----------:|----------:|------------:|-------------:|------------:|-------------:|---------:|-------------:|-----------:|--------------:|
| E0    |      0 |          0.1 |         0.4 |     0.4514 |          3.2 |      3.0802 |        0.6 |    0.7095 |       0.178 |         0.08 |      0.1136 |       0.4406 |   0.1502 |       0.1679 |     0.1546 |        0.2982 |

## E5 learned parameters

| exp   |   seed |   beta_hat |   gamma_hat |   wu_load_exp_min |   wu_load_exp_max |   wu_temp_exp_min |   wu_temp_exp_max |   R0eff_Surf_AC13_I_SBS |   R0eff_Surf_AC13_II_SBS |   R0eff_Surf_SMA13 |   R0eff_Surf_PAC13 |   R0eff_Mid_AC20_AH30 |   R0eff_Mid_AC20_SBS |   R0eff_Mid_AC20_AH50 |   R0eff_Bot_AC25_AH30 |   R0eff_Bot_AC25_AH50 |   R0eff_Bot_AC25_AH70 |   R0eff_Bot_AC25_Re_AH70 |   R0eff_Bot_AC10_SBS |   scale_I_SemiRigid_12cmAC |   scale_II_RigidComposite_12cmAC |   scale_III_SemiRigid_16_18cmAC |   scale_IV_Inverted_24_28cmAC |   scale_V_ThickAC_I_24_28cm |   scale_VI_ThickAC_II_36cm |   scale_VII_FullDepth_48_52cm |
|:------|-------:|-----------:|------------:|------------------:|------------------:|------------------:|------------------:|------------------------:|-------------------------:|-------------------:|-------------------:|----------------------:|---------------------:|----------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|---------------------:|---------------------------:|---------------------------------:|--------------------------------:|------------------------------:|----------------------------:|---------------------------:|------------------------------:|
| E5    |      0 |     0.4551 |       2.988 |             0.176 |             0.292 |             3.499 |             3.735 |                   1.716 |                   1.7063 |             1.5985 |             1.9615 |                 1.483 |               1.4823 |                2.3811 |                1.7171 |                2.2876 |                3.2264 |                   2.2064 |               2.1054 |                     0.3696 |                           0.3351 |                          0.4351 |                        0.4341 |                      0.4363 |                      0.345 |                        0.3385 |

## E5 H1 discrepancy test

|   seed |   mean_abs_g_II_VII |   mean_abs_g_others |   U |   p_one_sided |
|-------:|--------------------:|--------------------:|----:|--------------:|
|      0 |              0.0666 |              0.0819 |  13 |          0.96 |
