#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


y, x = np.ogrid[-2: 2: 200j, -3: 3: 200j]
z = * np.exp( -x**2 - y**2)

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
