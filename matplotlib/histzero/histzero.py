#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.random.rand(10000)
plt.hist(x, bins=100, range=(0, 2))
plt.savefig("zero.png")
plt.show()
