
# %%
from gradient import Gradient
from matplotlib import pyplot as plt
import numpy as np


stgs = []
stgs.append((100, (0,0,0)))
stgs.append((80, (255,0,255)))
stgs.append((0, (0,0,255)))
stgs.append((60, (0,255,255)))
stgs.append((20, (0,255,0)))
stgs.append((40, (255,255,0)))

gr = Gradient(stgs)
im = np.zeros((100,100,3)).astype(int)

for i in range(100):
    rgb = gr.get_color(i)
    im[:,i,0] = rgb[0]
    im[:,i,1] = rgb[1]
    im[:,i,2] = rgb[2]
    
plt.imshow(im)
# %%
