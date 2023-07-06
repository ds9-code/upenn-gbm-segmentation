# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

!pip install nnunetv2

!pip install --upgrade git+https://github.com/FabianIsensee/hiddenlayer.git

import os
os.environ['nnUNet_raw'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw"
os.environ['nnUNet_preprocessed'] =  "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_preprocessed"
os.environ['nnUNet_results'] = "/content/drive/MyDrive/TCIA/nnUNet/nnUNet_results"
!nnUNetv2_train Dataset501_Glioblastoma 3d_fullres 4 --npz
#!nnUNetv2_train Dataset501_Glioblastoma 3d_fullres 4 --npz
#!nnUNetv2_train Dataset501_Glioblastoma 3d_fullres 4 --npz
#!nnUNetv2_train Dataset501_Glioblastoma 3d_fullres 4 --npz
#!nnUNetv2_train Dataset501_Glioblastoma 3d_fullres 4 --npz