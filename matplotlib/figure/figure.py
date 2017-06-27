#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 1000)
y1 = 2*x + 1
y2 = x**2

fig1 = plt.figure(1)
plt.plot(x, y1, color="r", linestyle="--", linewidth=10)

fig2 = plt.figure(2)
plt.plot(x, y2)

fig1.savefig("figure1.png")
fig2.savefig("figure2.png")
plt.show()
