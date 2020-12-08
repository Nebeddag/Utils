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

def resize_with_pad(self, img: np.array, new_size):
    old_ratio = img.shape[1]/img.shape[0]
    new_ratio = new_size[0]/new_size[1]

    if(new_ratio < old_ratio):
        new_h = new_size[0]
        new_w = int(new_h / old_ratio)
    else:
        new_w = new_size[1]
        new_h = int(new_w * old_ratio)

    img = cv2.resize(img, (new_h, new_w))

    f = np.zeros((new_size[1],new_size[0],3),np.uint8)
    shift_x = int((new_size[1] - img.shape[0])/2)
    shift_y = int((new_size[0] - img.shape[1])/2)
    f[shift_x:img.shape[0]+shift_x,shift_y:img.shape[1]+shift_y] = img
    return f

def change_ratio_soft(img: np.array, new_ratio, shift = 0):
    if shift < 0 or shift > 1:
        raise Exception('Shift must be from 0 to 1')

    old_w = img.shape[1]
    old_h = img.shape[0]
    old_ratio = old_w/old_h
    shift_w = 0
    shift_h = 0

    if new_ratio > old_ratio:
        new_h = old_h
        new_w = int(new_h * new_ratio)
        shift_w = int((new_w - old_w) * shift)
    elif new_ratio < old_ratio:
        new_w = old_w
        new_h = int(new_w / new_ratio)
        shift_h = int((new_h - old_h) * shift)
    else:
        return img, ((0, 1), (0, 1))

    f = np.zeros((new_h, new_w, 3), np.uint8)
    f[shift_h:old_h+shift_h, shift_w:old_w+shift_w] = img

    transforms = ((shift_h/new_h, new_h/old_h), (shift_w/new_w, new_w/old_w)) #bias and coefficient
    return f, transforms