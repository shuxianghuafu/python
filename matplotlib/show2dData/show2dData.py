#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm


y, x = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp(-x**2 - y**2)

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.figure(figsize=(10, 3))
plt.subplot(1, 2, 1)
plt.imshow(z, extent=extent, origin="lower")
plt.colorbar()
plt.subplot(1, 2, 2)
plt.imshow(z, extent=extent, cmap=cm.gray, origin="lower")
plt.colorbar()

plt.savefig("show2D.png")
plt.show()
