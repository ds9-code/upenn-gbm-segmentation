# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

!pip install batchgenerators

"""https://github.com/MIC-DKFZ/nnUNet/blob/master/nnunetv2/dataset_conversion/generate_dataset_json.py"""

!pip install nnunetV2

# Set up all the parameters required by the metadata generation utility

output_folder = '/content/drive/MyDrive/TCIA/nnUNet/nnUNet_raw/Dataset501_Glioblastoma'
channel_names = {0: 'T1', 1: 'T1GD', 2:'T2', 3: 'FLAIR'}
labels = {'background': 0, 'ET': 1, 'NCR': 2, 'ED': 3}
file_ending = '.nii.gz'
region_class_order = {
  'background': 0,
  'whole tumor': (1, 2, 3),
  'tumor core': (2, 3),
  'enhancing tumor': 3
}
num_training_cases = 117
dataset_name = 'UPENN-GBM'
description = 'UPENN-GBM tumor segmentation'

from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json

generate_dataset_json(output_folder=output_folder,channel_names=channel_names, labels=labels,
                      file_ending=file_ending,region_class_order=region_class_order,
                      num_training_cases=num_training_cases, dataset_name=dataset_name, description=description)