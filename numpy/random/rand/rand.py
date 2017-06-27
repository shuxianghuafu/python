#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.random.rand(1000)
sorted(x)
y = x * 1.2 + np.random.rand()

fig = plt.figure(1)
axe = fig.add_subplot(2, 2, 1)
plt.scatter(x, y)
plt.show()
