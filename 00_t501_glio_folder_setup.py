# -*- coding: utf-8 -*-
"""00_t501_glio_folder_setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TiKbd7XEL_exeOQiX7RQMUozw2FKS_0H
"""

from google.colab import drive
drive.mount('/content/drive')

!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Task501_Glioblastoma
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Task501_Glioblastoma/imagesTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Task501_Glioblastoma/imagesTs
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Task501_Glioblastoma/labelsTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_preprocessed
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_results