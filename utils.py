import io
import cv2
import numpy as np
from PIL import Image
import copy

import torch
import torchvision.transforms as transforms

def get_object_images(image, boxes):
    images = []

    for box in boxes:
        x1 = int(box[0] * image.shape[1])
        y1 = int(box[1] * image.shape[0])
        x2 = int(box[2] * image.shape[1])
        y2 = int(box[3] * image.shape[0])

        x1,x2,y1,y2 = max(x1,0),max(x2,0),max(y1,0),max(y2,0)

        img_cropped = image[y1:y2, x1:x2]
        images.append(img_cropped)

    return images

def expand_boxes(boxes, rate = 0.2):
    bxs = copy.deepcopy(boxes)
    for box in bxs:
        w = abs(box[2] - box[0])
        h = abs(box[3] - box[1])
        e = max(w,h)*(rate/2)
        box[0] -= e
        box[2] += e
        box[1] -= e
        box[3] += e
    return bxs

def draw_boxes(image, boxes, color = (0,255,0), label = None):
    img = image.copy()
    for box in boxes:
        x1 = int(box[0] * img.shape[1])
        y1 = int(box[1] * img.shape[0])
        x2 = int(box[2] * img.shape[1])
        y2 = int(box[3] * img.shape[0])
        x1,x2,y1,y2 = max(x1,0),max(x2,0),max(y1,0),max(y2,0)
        img = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        if label:
            img = cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)
            img = cv2.putText(img, label, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return img

def get_batch(images, pretrained_size = (224, 224), use_padding = False, normalize = False):
    pretrained_means = [0.485, 0.456, 0.406]
    pretrained_stds= [0.229, 0.224, 0.225]

    with torch.no_grad():
        batch = torch.zeros((len(images), 3, pretrained_size[0], pretrained_size[1]))
        for i in range(len(images)):
            out_img = copy.deepcopy(images[i])
            # out_img = cv2.cvtColor(out_img, cv2.COLOR_BGR2RGB)
            out_img = Image.fromarray(out_img)
            if use_padding:
                out_img = transforms.Resize(pretrained_size, get_padding(out_img))(out_img)
            else:
                out_img = transforms.Resize(pretrained_size)(out_img)
            out_img = transforms.ToTensor()(out_img)
            if normalize:
                out_img = transforms.Normalize(mean = pretrained_means, std=pretrained_stds)(out_img)
            batch[i] = out_img
    return batch

def get_padding(image, size):
    max_w, max_h = size
    
    imsize = image.size
    h_padding = (max_w - imsize[0]) / 2
    v_padding = (max_h - imsize[1]) / 2
    l_pad = h_padding if h_padding % 1 == 0 else h_padding+0.5
    t_pad = v_padding if v_padding % 1 == 0 else v_padding+0.5
    r_pad = h_padding if h_padding % 1 == 0 else h_padding-0.5
    b_pad = v_padding if v_padding % 1 == 0 else v_padding-0.5
    
    padding = (int(l_pad), int(t_pad), int(r_pad), int(b_pad))
    
    return padding


def iou(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA) * max(0, yB - yA)

    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea)

    return iou

def ios(boxA, boxB):
    '''Returns intersection over first box square'''
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA) * max(0, yB - yA)

    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])

    iou = interArea / float(boxAArea)

    return iou

def get_average_box(boxes):
    b_sum = [0,0,0,0]

    for b in boxes:
        for j in range(4):
            b_sum[j] += b[j]
    
    avg_box = [
        b_sum[0]/len(boxes),
        b_sum[1]/len(boxes),
        b_sum[2]/len(boxes),
        b_sum[3]/len(boxes),
        ]
    
    return avg_box


from typing import List, Tuple

Color = Tuple[int, int, int]
Value = float
Stage = Tuple[float, Color]

class Gradient:
    def __init__(self, stages: List[Stage]):
        assert len(stages) > 1, 'less than two values passed'

        values = [st[0] for st in stages]
        assert len(values) == len(set(values)), 'values is not unique'

        self.min = min(values)
        self.max = max(values)
        self.stages = sorted(stages, key=lambda x:x[0])
    
    def get_color(self, value: float) -> Tuple[int, int, int]:
        if value <= self.min:
            return self.stages[0][1]

        if value >= self.max:
            return self.stages[-1][1]

        for i in range(len(self.stages)):
            st1 = self.stages[i]
            st2 = self.stages[i + 1]
            if value > st1[0] and value <= st2[0]:
                r_dif = st2[1][0] - st1[1][0]
                g_dif = st2[1][1] - st1[1][1]
                b_dif = st2[1][2] - st1[1][2]
                v_norm = (value - st1[0]) / (st2[0] - st1[0])
                r = st1[1][0] + int(r_dif * v_norm)
                g = st1[1][1] + int(g_dif * v_norm)
                b = st1[1][2] + int(b_dif * v_norm)
                return (r, g, b)
