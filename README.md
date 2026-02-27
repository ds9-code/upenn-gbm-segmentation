# Automated segmentation of glioblastoma tumors from MRI scans
Develop a deep learning medical segmentation model using the nnUNet framework to perform automated tumor sub-region segmentation of Glioblastoma multi-parametric MRI scans. Published paper in JEI: https://doi.org/10.59720/23-265; presented at NVIDIA Global Tech Conference.

# Aims and Goals
This repository contains code and notebooks for building, training, and evaluating a deep learning pipeline for automated Glioblastoma (GBM) tumor segmentation from multi-parametric MRI scans. The project was developed in collaboration with the University of Pennsylvania School of Medicine, with the goal of leveraging advanced neural networks to segment tumor sub-regions accurately and reproducibly for research and clinical applications.

The dataset used is based on the UPenn-GBM cohort, a publicly available MRI dataset with manually refined tumor labels suitable for segmentation benchmarking and radiomic analysis.

# Repository Structure
├── 00_t501_glio_folder_setup.py           # Project directory and organization script
├── 01_t501_glio_data_setup.py             # Download / prepare dataset directories
├── 02_t501_glio_process_labels.py         # Process and normalize segmentation masks
├── 03_t501_glio_gen_dataset_json.py       # Create nnU-Net dataset JSONs
├── 04_t501_glio_verify_data_integrity.py   # Check data integrity and consistency
├── 05_t501_glio_model_train.py            # Model training using nnU-Net framework
├── 06_t501_glio_model_inference.py         # Perform inference with a trained model
├── 08_t501_glio_volumetric_analysis.ipynb  # Notebook for post-processing and volumetric evaluation
├── README.md                              # This file
