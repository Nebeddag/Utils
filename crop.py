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

#resizing image for model training or inference
def soft_resize(img: np.array, size):
    old_ratio = img.shape[0]/img.shape[1]
    new_ratio = size[0]/size[1]

    if(new_ratio > old_ratio):
        new_w = size[0]
        new_h = new_w / old_ratio
    else:
        new_h = size[1]
        new_w = new_h * old_ratio

    img = cv2.resize(img, new_w, new_h)

    f = np.zeros((size[0],size[1],3),np.uint8)
    f[0:img.shape[0],0:img.shape[1]] = img
    return f

def change_ratio_soft(img: np.array, new_ratio):
    old_ratio = img.shape[0]/img.shape[1]

    if(new_ratio > old_ratio):
        new_h = img.shape[1]
        new_w = new_h * new_ratio
    else:
        new_w = img.shape[0]
        new_h = new_w / new_ratio

    f = np.zeros((new_w, new_h,3),np.uint8)
    f[0:img.shape[0],0:img.shape[1]] = img
    return f