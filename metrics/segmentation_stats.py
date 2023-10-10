!pip install medpy

from google.colab import drive
drive.mount('/content/drive')

import nibabel as nib
import numpy as np
from medpy.metric.binary import hd95

def diceScore(pred, ground):

    if pred.shape != ground.shape:
        raise ValueError("Shape mismatch: pred and ground must have the same shape.")

    # Compute Dice coefficient
    intersection = np.logical_and(pred, ground)

    if ((pred.sum()==0) and (ground.sum()==0)):
        # label not present in either
        score = 1
    else:
        score = (2. * intersection.sum()) / (pred.sum() + ground.sum())

    return score

def sensitivity(pred, ground):

    numerator = np.sum(np.multiply(ground, pred))
    denominator =np.sum(ground)
    if denominator ==0:
        return np.nan
    else:
        return  numerator/denominator

def hausdorff95(pred, ground):

    if (np.count_nonzero(ground) == 0) or (np.count_nonzero(pred) == 0):
        return np.nan

    return hd95(ground, pred)

pred_path = '/content/drive/MyDrive/stats/pred_351_segm.nii.gz'
gt_path = '/content/drive/MyDrive/stats/gt_351_segm.nii.gz'

gt = nib.load(gt_path).get_fdata()
gt = np.rint(gt)

# load the predicted segmentation inference
pred = nib.load(pred_path).get_fdata()
pred = np.rint(pred)

# Convert to array for Sensitivity HD-95 calculation
pred_img = np.asarray(pred)
gt_img = np.asarray(gt)

# Calculate DICE Score -

ds_wt = diceScore(pred>0, gt>0) # For Whole Tumor
ds_1 = diceScore(pred==1, gt==1) # Tumor Core
ds_2 = diceScore(pred==2, gt==2) # For Edema subregion
ds_3 = diceScore(pred==3, gt==4) # For ET subregion
print("DSC-WT: ", ds_wt, ", DSC-TC: ", ds_1, ", DSC-ED: ", ds_2, ", DSC-ET: ", ds_3)

# Calculate Sensitivity -

s_wt = sensitivity(pred_img>0, gt_img>0) # For Whole Tumor
s_1 = sensitivity(pred_img==1, gt_img==1) # For Enhancing Tumor subregion
s_2 = sensitivity(pred_img==2, gt_img==2) # For Edema subregion
s_3 = sensitivity(pred_img==3, gt_img==4) # For ET subregion
print("Sen-WT: ", s_wt, ", Sen-TC: ", s_1, ", Sen-ED: ", s_2, ", Sen-ET: ", s_3)

# Calculate Hausdorff-95 distance -
h_wt = hausdorff95(pred_img>0, gt_img>0)
h_1 = hausdorff95(pred_img==1, gt_img==1)
h_2 = hausdorff95(pred_img==2, gt_img==2)
h_3 = hausdorff95(pred_img==3, gt_img==4)
print("HD95-WT: ", h_wt, ", HD95-TC: ", h_1, ", HD95-ED: ", h_2, ", HD95-ET: ", h_3)