import numpy as np
import cv2

def make_square(img: np.array, new_h: int = -1):
    ratio = new_h/max(img.shape[0:2])

    if new_h > 0:
        img = cv2.resize(img, (int(img.shape[1]*ratio), int(img.shape[0]*ratio)))

    s = max(img.shape[0:2])
    f = np.zeros((s,s,3),np.uint8)
    ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2
    f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img
    return f