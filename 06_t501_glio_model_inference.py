# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

!pip install nnunetv2

import os
os.environ['nnUNet_raw'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw"
os.environ['nnUNet_preprocessed'] =  "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_preprocessed"
os.environ['nnUNet_results'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_results"

!nnUNetv2_find_best_configuration Dataset501_Glioblastoma -c 3d_fullres

!nnUNetv2_predict -d Dataset501_Glioblastoma -i /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma/imagesTs -o /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/Dataset501_Glioblastoma/inference -f  0 1 2 3 4 -tr nnUNetTrainer -c 3d_fullres -p nnUNetPlans

!nnUNetv2_apply_postprocessing -i /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/Dataset501_Glioblastoma/inference -o /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/Dataset501_Glioblastoma/postprocessing -pp_pkl_file /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/Dataset501_Glioblastoma/nnUNetTrainer__nnUNetPlans__3d_fullres/crossval_results_folds_0_1_2_3_4/postprocessing.pkl -np 8 -plans_json /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/Dataset501_Glioblastoma/nnUNetTrainer__nnUNetPlans__3d_fullres/crossval_results_folds_0_1_2_3_4/plans.json