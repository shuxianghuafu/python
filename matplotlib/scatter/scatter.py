#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
t = ax.scatter(np.random.rand(20), np.random.rand(20))

plt.savefig("scatter", ftm="png")
plt.show()
