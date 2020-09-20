#%%
import gradients as gr
from matplotlib import pyplot as plt
import numpy as np


# %%
g = gr.GreenYellowRedGradient(0, 50, 100)
im = np.zeros((100,100,3)).astype(int)

for i in range(100):
    rgb = g.get_rgb(i)
    im[:,i,0] = rgb[0]
    im[:,i,1] = rgb[1]
    im[:,i,2] = rgb[2]
# %%
plt.imshow(im)
# %%
import cv2
cv2.imshow('1', im)
# %%

# %%
