# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

!pip install nnunetv2

import os
os.environ['nnUNet_raw'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw"
os.environ['nnUNet_preprocessed'] =  "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_preprocessed"
os.environ['nnUNet_results'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_results"

# Verify dataset integrity has to be executed only the first time you are pre-processing the data
# After successful plan and preprocessing
!nnUNetv2_plan_and_preprocess -d 501 --verify_dataset_integrity