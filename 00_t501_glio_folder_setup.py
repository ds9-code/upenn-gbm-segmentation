from google.colab import drive
drive.mount('/content/drive')

!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Dataset501_Glioblastoma
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Dataset501_Glioblastoma/imagesTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Dataset501_Glioblastoma/imagesTs
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_raw_data/Dataset501_Glioblastoma/labelsTr
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_preprocessed
!mkdir -p /content/drive/MyDrive/TCIA/nnUNet_raw_data_base/nnUNet_results