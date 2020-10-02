import pycocotools
import numpy as np
import math

def computePdj(kp_pr: np.array, kp_gr: np.array):
    dist = np.sqrt((kp_gr[:,0] - kp_pr[:,0])**2 + (kp_gr[:,1] - kp_pr[:,1])**2)
    diag = math.sqrt((kp_gr[:,0].max() - kp_gr[:,0].min())**2 + (kp_gr[:,1].max() - kp_gr[:,1].min())**2)
    valid_dist = dist < diag * 0.05
    result = valid_dist.sum() / dist.shape[0]
    return result

def computeOks(kp_pr: np.array, kp_gr: np.array,
hips, ankles, knees, shoulders, elbows, ears, nose, eyes):
    hips_k = 0.107
    ankles_k = 0.089
    knees_k = 0.087
    shoulders_k = 0.079
    elbows_k = 0.072
    ears_k = 0.035
    nose_k = 0.026
    eyes_k = 0.025
    for i, gkp in enumerate(kp_gr):
        d = 
    pass

k1 = np.array([(1, 4), (101, 204), (301, 504)])
k2 = np.array([(30, 1), (98, 198), (309, 497)])

pdj = computePdj(k1,k2)
oks = computeOks([k1],[k2])
print(pdj, oks)