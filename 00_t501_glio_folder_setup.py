# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma/imagesTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma/imagesTs
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma/labelsTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_preprocessed
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/inference
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet/nnUNet_results/postprocessed