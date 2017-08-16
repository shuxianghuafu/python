#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


img = plt.imread("./scatter.png")
fig, axes = plt.subplots(2, 4, figsize=(11, 4))
fig.subplots_adjust(0, 0, 1, 1, 0.05, 0.05)

axes = axes.ravel()

axes[0].imshow(img)
axes[1].imshow(img, origin="lower")
axes[2].imshow(img*1.0)
axes[3].imshow(img / 255.0)
axes[4].imshow(np.clip(img / 200.0, 0, 1))


axe_img = axes[5].imshow(img[:, :, 0])
plt.colorbar(axe_img, ax=axes[5])

axe_img = axes[6].imshow(img[:, :, 0], cmap="copper")
plt.colorbar(axe_img, ax=axes[6])

for ax in axes:
    ax.set_axis_off()

plt.savefig("img.png")
plt.show()
