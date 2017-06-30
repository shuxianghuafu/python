#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
n, bins, rects = ax.hist(np.random.randn(1000), bins=50, facecolor="blue")
rects[0] is ax.patches[0]

plt.savefig("patch", ftm="png")
plt.show()
