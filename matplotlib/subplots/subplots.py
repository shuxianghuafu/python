#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


(fig, axes) = plt.subplots(2, 3)
plt.sca(axes[1][1])
x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.savefig("subplots", ftm="png")
plt.show()
