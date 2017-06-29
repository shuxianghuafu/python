#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


plt.figure(1)
plt.figure(2)

ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

x = np.linspace(0, 3, 100)
for i in xrange(8):
    plt.figure(1)
    plt.plot(x, np.exp(i*x/3.))
    plt.sca(ax1)
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)
    plt.plot(x, np.cos(i*x))

plt.figure(1)
plt.savefig("exp", ftm="png")
plt.figure(2)
plt.savefig("sin and cos", ftm="png")
plt.show()
