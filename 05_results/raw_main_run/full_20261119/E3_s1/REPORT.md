# MSSA-Rut experiment report

Run directory: `/home/zyl105/Zerojy/projects/rut-mssa-20261119/results/full_20261119/E3_s1`

## E3

### cold_start

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         0 |      1.8761 |        nan |     1.4392 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         0 |      1.8829 |        nan |     1.5261 |      0.9684 |      9.3981 |      1.0558 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         0 |      1.4078 |        nan |     1.0974 |      0.7385 |      3.1096 |      0.8347 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         0 |      5.1334 |        nan |     4.6169 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### early_life

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |       0.2 |      1.3032 |        nan |     1.026  |    nan      |    nan      |    nan      |             1.1859 |                0.1199 |                        nan |           12.6838 |           nan      |
| gbm_residual |       0.4 |      0.6881 |        nan |     0.5469 |    nan      |    nan      |    nan      |             0.7143 |                0.1484 |                        nan |            1.77   |            12.3867 |
| gbm_residual |       0.6 |      0.6159 |        nan |     0.4933 |    nan      |    nan      |    nan      |             0.5688 |                0.1396 |                        nan |            0.38   |             7.87   |
| jtg_enkf     |       0.2 |      2.7621 |        nan |     2.3435 |      0.2549 |      3.3585 |      1.8978 |             3.4486 |                0      |                        nan |            9.4118 |            21.8767 |
| jtg_enkf     |       0.4 |      0.894  |        nan |     0.7136 |      0.5583 |      1.4598 |      0.558  |             0.9758 |                0      |                        nan |            5.828  |             5.2883 |
| jtg_enkf     |       0.6 |      0.5359 |        nan |     0.4273 |      0.6257 |      1.002  |      0.332  |             0.4153 |                0      |                        nan |          nan      |             6.6733 |
| mssa         |       0.2 |      1.297  |        nan |     1.0418 |      0.5533 |      2.0092 |      0.8318 |             1.3225 |                0.0027 |                          0 |           20.9389 |           nan      |
| mssa         |       0.4 |      1.0337 |        nan |     0.8265 |      0.6266 |      1.9567 |      0.6393 |             0.9821 |                0.0097 |                          0 |            8.91   |            21.77   |
| mssa         |       0.6 |      0.7554 |        nan |     0.597  |      0.7993 |      1.8791 |      0.436  |             0.7095 |                0.0082 |                          0 |            0.79   |           nan      |
| persistence  |       0.2 |      2.9861 |        nan |     2.4977 |    nan      |    nan      |    nan      |             3.6266 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.4 |      1.084  |        nan |     0.8738 |    nan      |    nan      |    nan      |             1.3919 |                0      |                        nan |          nan      |           nan      |
| persistence  |       0.6 |      0.7818 |        nan |     0.6055 |    nan      |    nan      |    nan      |             0.8049 |                0      |                        nan |          nan      |           nan      |

### horizon

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4227 |        nan |     0.3103 |      0.8862 |      1.2451 |      0.2285 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         3 |      0.4671 |        nan |     0.3432 |      0.8461 |      1.2451 |      0.2553 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         6 |      0.5521 |        nan |     0.4082 |      0.7958 |      1.2451 |      0.3082 |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |        12 |      0.6577 |        nan |     0.4951 |      0.7224 |      1.2451 |      0.3827 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         3 |      0.4858 |        nan |     0.3651 |      0.691  |      0.8904 |      0.2832 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         6 |      0.5746 |        nan |     0.4352 |      0.6154 |      0.9742 |      0.3421 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |        12 |      0.7377 |        nan |     0.5557 |      0.5608 |      1.1445 |      0.4413 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3784 |        nan |     0.2851 |      0.9261 |      1.3494 |      0.2066 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         3 |      0.4876 |        nan |     0.3869 |      0.8935 |      1.553  |      0.2759 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         6 |      0.6086 |        nan |     0.4906 |      0.831  |      1.698  |      0.3536 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |        12 |      0.7412 |        nan |     0.5992 |      0.7747 |      1.812  |      0.4404 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         3 |      0.5304 |        nan |     0.3716 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         6 |      0.7586 |        nan |     0.538  |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |        12 |      1.1077 |        nan |     0.7733 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_all

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         1 |      0.4227 |        nan |     0.3103 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         2 |      0.434  |        nan |     0.3162 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4556 |        nan |     0.3326 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5219 |        nan |     0.3818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         1 |      0.4224 |        nan |     0.3135 |      0.7421 |      0.8474 |      0.2406 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4343 |        nan |     0.3253 |      0.7366 |      0.8878 |      0.2483 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4586 |        nan |     0.3419 |      0.7491 |      0.9484 |      0.2607 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5532 |        nan |     0.3999 |      0.7403 |      1.0632 |      0.3057 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         1 |      0.3784 |        nan |     0.2851 |      0.9261 |      1.3494 |      0.2066 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.4276 |        nan |     0.3304 |      0.9155 |      1.4294 |      0.2372 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.5091 |        nan |     0.4027 |      0.8804 |      1.5315 |      0.2886 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6326 |        nan |     0.5029 |      0.8043 |      1.654  |      0.3672 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         1 |      0.3988 |        nan |     0.2724 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4424 |        nan |     0.3023 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.5269 |        nan |     0.3564 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.7457 |        nan |     0.4885 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### sparse_unobserved

| model        |   setting |   RMSE_mean |   RMSE_std |   MAE_mean |   PICP_mean |   MPIW_mean |   CRPS_mean |   end_abs_err_mean |   mono_viol_frac_mean |   perm_mono_viol_frac_mean |   FPTerr_8.0_mean |   FPTerr_10.0_mean |
|:-------------|----------:|------------:|-----------:|-----------:|------------:|------------:|------------:|-------------------:|----------------------:|---------------------------:|------------------:|-------------------:|
| gbm_residual |         2 |      0.4289 |        nan |     0.3147 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         4 |      0.4393 |        nan |     0.3226 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| gbm_residual |         8 |      0.5053 |        nan |     0.3696 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         2 |      0.4151 |        nan |     0.3137 |      0.7454 |      0.8778 |      0.2389 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         4 |      0.4418 |        nan |     0.3301 |      0.7527 |      0.9357 |      0.2513 |                nan |                   nan |                        nan |               nan |                nan |
| jtg_enkf     |         8 |      0.5299 |        nan |     0.388  |      0.7461 |      1.0494 |      0.2955 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         2 |      0.3965 |        nan |     0.3048 |      0.922  |      1.372  |      0.2195 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         4 |      0.4886 |        nan |     0.3842 |      0.8866 |      1.4942 |      0.2754 |                nan |                   nan |                        nan |               nan |                nan |
| mssa         |         8 |      0.6143 |        nan |     0.4884 |      0.8159 |      1.6336 |      0.3555 |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         2 |      0.4118 |        nan |     0.2818 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         4 |      0.4919 |        nan |     0.3332 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |
| persistence  |         8 |      0.71   |        nan |     0.4661 |    nan      |    nan      |    nan      |                nan |                   nan |                        nan |               nan |                nan |

### Paired structure-level RMSE difference (model - MSSA), bootstrap 95% CI

| protocol          |   setting | model        | reference   |   mean_RMSE_diff |   ci_low |   ci_high |   structures_ref_better |   n_structures |
|:------------------|----------:|:-------------|:------------|-----------------:|---------:|----------:|------------------------:|---------------:|
| cold_start        |       0   | gbm_residual | mssa        |           0.3758 |   0.122  |    0.6442 |                      14 |             19 |
| early_life        |       0.2 | gbm_residual | mssa        |          -0.0379 |  -0.229  |    0.141  |                      10 |             19 |
| early_life        |       0.4 | gbm_residual | mssa        |          -0.2931 |  -0.446  |   -0.1492 |                       4 |             19 |
| early_life        |       0.6 | gbm_residual | mssa        |          -0.1248 |  -0.2451 |    0.0005 |                       8 |             19 |
| horizon           |       1   | gbm_residual | mssa        |           0.0288 |  -0.0078 |    0.0775 |                      10 |             19 |
| horizon           |       3   | gbm_residual | mssa        |          -0.0316 |  -0.0614 |    0.0037 |                       5 |             19 |
| horizon           |       6   | gbm_residual | mssa        |          -0.0651 |  -0.0998 |   -0.0269 |                       2 |             19 |
| horizon           |      12   | gbm_residual | mssa        |          -0.0904 |  -0.1441 |   -0.0358 |                       4 |             19 |
| sparse_all        |       1   | gbm_residual | mssa        |           0.0288 |  -0.0082 |    0.0772 |                      10 |             19 |
| sparse_all        |       2   | gbm_residual | mssa        |          -0.0067 |  -0.0389 |    0.033  |                       5 |             19 |
| sparse_all        |       4   | gbm_residual | mssa        |          -0.0628 |  -0.0981 |   -0.0218 |                       2 |             19 |
| sparse_all        |       8   | gbm_residual | mssa        |          -0.1132 |  -0.1525 |   -0.0736 |                       2 |             19 |
| sparse_unobserved |       2   | gbm_residual | mssa        |           0.0186 |  -0.0173 |    0.0642 |                       9 |             19 |
| sparse_unobserved |       4   | gbm_residual | mssa        |          -0.0599 |  -0.0941 |   -0.0215 |                       2 |             19 |
| sparse_unobserved |       8   | gbm_residual | mssa        |          -0.1129 |  -0.1514 |   -0.0747 |                       1 |             19 |
| cold_start        |       0   | jtg_enkf     | mssa        |           0.4223 |   0.12   |    0.7501 |                      14 |             19 |
| early_life        |       0.2 | jtg_enkf     | mssa        |           1.391  |   0.8135 |    1.9848 |                      16 |             19 |
| early_life        |       0.4 | jtg_enkf     | mssa        |          -0.1092 |  -0.4422 |    0.2223 |                       9 |             19 |
| early_life        |       0.6 | jtg_enkf     | mssa        |          -0.1747 |  -0.3793 |    0.0139 |                       9 |             19 |
| horizon           |       1   | jtg_enkf     | mssa        |           0.0455 |   0.0208 |    0.0671 |                      15 |             19 |
| horizon           |       3   | jtg_enkf     | mssa        |           0.0046 |  -0.0374 |    0.0409 |                      14 |             19 |
| horizon           |       6   | jtg_enkf     | mssa        |          -0.0228 |  -0.0817 |    0.029  |                      11 |             19 |
| horizon           |      12   | jtg_enkf     | mssa        |           0.0117 |  -0.0735 |    0.0902 |                      12 |             19 |
| sparse_all        |       1   | jtg_enkf     | mssa        |           0.0455 |   0.0203 |    0.0668 |                      15 |             19 |
| sparse_all        |       2   | jtg_enkf     | mssa        |           0.0106 |  -0.026  |    0.0411 |                      13 |             19 |
| sparse_all        |       4   | jtg_enkf     | mssa        |          -0.0412 |  -0.0893 |    0.0041 |                       9 |             19 |
| sparse_all        |       8   | jtg_enkf     | mssa        |          -0.0658 |  -0.1431 |    0.0036 |                       7 |             19 |
| sparse_unobserved |       2   | jtg_enkf     | mssa        |           0.0206 |  -0.011  |    0.0486 |                      13 |             19 |
| sparse_unobserved |       4   | jtg_enkf     | mssa        |          -0.0382 |  -0.0845 |    0.0059 |                      10 |             19 |
| sparse_unobserved |       8   | jtg_enkf     | mssa        |          -0.0694 |  -0.1434 |   -0.0025 |                       7 |             19 |
| cold_start        |       0   | persistence  | mssa        |           3.7112 |   2.9949 |    4.3697 |                      19 |             19 |
| early_life        |       0.2 | persistence  | mssa        |           1.5695 |   1.0342 |    2.0842 |                      17 |             19 |
| early_life        |       0.4 | persistence  | mssa        |           0.1009 |  -0.0512 |    0.2408 |                      13 |             19 |
| early_life        |       0.6 | persistence  | mssa        |           0.0369 |  -0.1305 |    0.21   |                      10 |             19 |
| horizon           |       1   | persistence  | mssa        |           0.0184 |  -0.0143 |    0.0451 |                      16 |             19 |
| horizon           |       3   | persistence  | mssa        |           0.0448 |  -0.0093 |    0.0897 |                      16 |             19 |
| horizon           |       6   | persistence  | mssa        |           0.151  |   0.0573 |    0.2288 |                      16 |             19 |
| horizon           |      12   | persistence  | mssa        |           0.3693 |   0.2333 |    0.4864 |                      16 |             19 |
| sparse_all        |       1   | persistence  | mssa        |           0.0184 |  -0.0141 |    0.0449 |                      16 |             19 |
| sparse_all        |       2   | persistence  | mssa        |           0.0148 |  -0.0248 |    0.0471 |                      15 |             19 |
| sparse_all        |       4   | persistence  | mssa        |           0.0195 |  -0.0326 |    0.064  |                      14 |             19 |
| sparse_all        |       8   | persistence  | mssa        |           0.1101 |   0.0088 |    0.1976 |                      16 |             19 |
| sparse_unobserved |       2   | persistence  | mssa        |           0.0148 |  -0.0226 |    0.0465 |                      15 |             19 |
| sparse_unobserved |       4   | persistence  | mssa        |           0.0044 |  -0.0402 |    0.0419 |                      14 |             19 |
| sparse_unobserved |       8   | persistence  | mssa        |           0.094  |  -0.0004 |    0.1775 |                      15 |             19 |

## Counterfactual physical consistency (E4) [E3]

| model        | setting    |   frac_increase |   frac_decrease |   mean_delta |
|:-------------|:-----------|----------------:|----------------:|-------------:|
| gbm_residual | load_x2    |          0.8506 |          0.1494 |       0.1435 |
| gbm_residual | temp_plus5 |          0.6677 |          0.3318 |       0.005  |
| jtg_enkf     | load_x2    |          0.5786 |          0.4194 |       0.0421 |
| jtg_enkf     | temp_plus5 |          0.7568 |          0.2432 |       0.1561 |
| mssa         | load_x2    |          1      |          0      |       0.4289 |
| mssa         | temp_plus5 |          1      |          0      |       0.8461 |
| persistence  | load_x2    |          0      |          0      |       0      |
| persistence  | temp_plus5 |          0      |          0      |       0      |

## Native vs ACI intervals [E3]

| model    | setting   |   PICP |   MPIW |     IS |
|:---------|:----------|-------:|-------:|-------:|
| jtg_enkf | aci       | 0.9607 | 2.0412 | 2.4893 |
| jtg_enkf | native    | 0.7276 | 0.8364 | 3.805  |
| mssa     | aci       | 0.9655 | 1.8097 | 2.1489 |
| mssa     | native    | 0.9226 | 1.343  | 2.1168 |

## First-passage Monte Carlo [E3]

|   frac |   threshold |   p_cross_by_end |   median_abs_err_Mload |
|-------:|------------:|-----------------:|-----------------------:|
|    0.2 |           8 |           0.7456 |                 8.641  |
|    0.2 |          10 |           0.2359 |                10.2967 |
|    0.4 |           8 |           0.5617 |                 9.385  |
|    0.4 |          10 |           0.2343 |                 8.7083 |
|    0.6 |           8 |           0.4658 |                 5.77   |
|    0.6 |          10 |           0.1799 |                 6.365  |
