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

# Algorithm Architecture
<img width="899" height="337" alt="Screenshot 2026-02-27 at 2 17 54 PM" src="https://github.com/user-attachments/assets/d2905b18-d3a2-45e0-8236-bb3681005a4f" />
Figure 1: Deep neural network processing pipeline. The end-to-end pipeline shows the ingestion of MRI scans, data preprocessing, model training, model inference, and post-processing stages. MRI scans were ingested into the pipeline and normalized, then split into training (n=286) and test (n=72) cohorts. The training cohort was used to train the nnU-Net model, and the trained model was used to conduct automated segmentation on the unseen test cohort. The model performance was then evaluated using quantitative and volumetric similarity
metrics. The nn-Unet architecture was adapted from the original U-Net paper by Ronneberger et al.

# Results

<img width="431" height="534" alt="Screenshot 2026-02-27 at 2 18 35 PM" src="https://github.com/user-attachments/assets/023aeb6e-4771-4b9d-81bf-d78ac7c05356" />
Performance metrics for the nnU-Net neural network models on the test dataset. Summary statistics of the models’ prediction performance on the test dataset across the whole tumor (WT), enhancing tumor (ET) and edema (ED) subregions. Model inference was run on the test dataset and the summary statistics for the DSC score, Sensitivity, and the 95% Hausdorff distance were calculated. Since MRI sequences are specific to certain tumor regions, results were not computed for non-relevant regions when not all MRI sequences were utilized.

<img width="444" height="225" alt="Screenshot 2026-02-27 at 2 19 35 PM" src="https://github.com/user-attachments/assets/5550d031-ff90-4378-b614-f989306ce280" />
Correlation of VASARI volumetric features between the predicted segmentation and ground truth segmentation for the 3D mpMRI model on the enhancing tumor subregion using the test dataset. Correlation plot showing linear trend of predicted voxel volume to ground truth voxel volume for the enhancing tumor subregion (n=72). The ratio of the enhancing tumor volume to the whole tumor volume (ET/WT) was calculated for both the predicted segmentation (predicted ET/WT) and the ground truth segmentation (ground truth ET/WT) of each patient in the test dataset and plotted in a correlation plot. The Pearson’s correlation coefficient was calculated for the predicted and ground truth segmentation volumes (r2 = 0.92, p-value = 0.000995).

<img width="384" height="744" alt="Screenshot 2026-02-27 at 2 20 35 PM" src="https://github.com/user-attachments/assets/65cdc2d7-01c5-44d7-8e1b-73d7b8b4dc80" />
Sample predicted and ground truth segmentation of Grade 1, Grade 2 and Grade 3 meningiomas. Individual samples of patient MRI sequences for each meningioma tumor grade, along with the ground truth segmentation map and the predicted segmentation map with associated DSC scores for the whole tumor, enhancing tumor and edema subregions. Model inference was run on three patients’ MRIs with Grade 1, Grade 2 and Grade 3 meningioma tumors, and the DSC scores were calculated on the predicted segmentation. The ground truth and predicted segmentation maps were visualized using ITKSnap software.
