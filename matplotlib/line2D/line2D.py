#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 8))
x = np.arange(0, 5, 0.1)

line = plt.plot(x, 0.05*x*x)[0]
line.set_alpha(0.5)
line.set_color("red")

plt.savefig("line2D", fmt="png")
plt.show()
