# #%%
# import numpy as np
# import pandas as pd
# import seaborn as sns
# %matplotlib inline
# import matplotlib.pyplot as plt
# from IPython.display import display, HTML
# display(HTML("<style>.container {width: 100%; !important}</style>"))
# import sys
# import os
# import collections
# import cv2
# from ipywidgets import interact
# import ipywidgets as widgets
# import ffmpeg
# import re
# from pathos.multiprocessing import ProcessingPool as Pool
# import difflib
# import collections
# from sklearn.cluster import DBSCAN

# import uuid

# #%%
# %matplotlib inline
# import matplotlib.pyplot as plt
# from IPython.display import display, HTML
# display(HTML("<style>.container {width: 100%; !important}</style>"))

#%%
import ffmpeg


# Просмотр выбранного видео
#%%
file_full_name = '/somepath/0000000A.XI1'
out, err = (
    ffmpeg
    .input(file_full_name, f='H264')
    .filter('fps', fps=1, round='down')
    .filter('scale', 256, 144)
    .output('pipe:', format ='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)
video = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1,144,256,3])
)

vv=np.array(video)

# Показ кадров
@interact(frame=(0,vv.shape[0]-1))
def show_frame (frame=0):
    plt.rcParams['figure.figsize'] = (20,25)
    plt.imshow(vv[frame,:,:,:])
