#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.random.randn(100)
y = np.random.randn(100)

plt.hist2d(x, y, bins=[40, 40], range=[[-6, 6], [-6, 6]])
plt.show()
