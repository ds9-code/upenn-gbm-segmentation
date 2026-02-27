# Automated segmentation of glioblastoma tumors from MRI scans
Develop a deep learning medical segmentation model using the nnUNet framework to perform automated tumor sub-region segmentation of Glioblastoma multi-parametric MRI scans. Published paper in JEI: https://doi.org/10.59720/23-265; presented at NVIDIA Global Tech Conference.

# Aims and Goals
This repository contains code and notebooks for building, training, and evaluating a deep learning pipeline for automated Glioblastoma (GBM) tumor segmentation from multi-parametric MRI scans. The project was developed in collaboration with the University of Pennsylvania School of Medicine, with the goal of leveraging advanced neural networks to segment tumor sub-regions accurately and reproducibly for research and clinical applications.

The dataset used is based on the UPenn-GBM cohort, a publicly available MRI dataset with manually refined tumor labels suitable for segmentation benchmarking and radiomic analysis.

# Repository Structure
| Path | Description |
|------|-------------|
| `00_t501_glio_folder_setup.py` | Initializes and organizes the project directory structure for nnU-Net compatibility. |
| `01_t501_glio_data_setup.py` | Prepares and structures the UPenn-GBM MRI dataset for training and inference. |
| `02_t501_glio_process_labels.py` | Processes and standardizes segmentation masks (label normalization and formatting). |
| `03_t501_glio_gen_dataset_json.py` | Generates the nnU-Net dataset configuration JSON file. |
| `04_t501_glio_verify_data_integrity.py` | Performs dataset validation checks to ensure file consistency and completeness. |
| `05_t501_glio_model_train.py` | Launches nnU-Net model training for GBM segmentation. |
| `06_t501_glio_model_inference.py` | Runs inference using trained nnU-Net models and outputs predicted segmentation masks. |
| `08_t501_glio_volumetric_analysis.ipynb` | Notebook for volumetric evaluation, Dice computation, and post-processing analysis. |
| `README.md` | Project documentation, setup instructions, and usage guide. |
