#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import optimize


def func(x, p):
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)


def residuals(p, y, x):
    return y-func(x, p)


x = np.linspace(0, 2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6
y0 = func(x, [A, k, theta])

np.random.seed(0)
y1 = y0 + 2*np.random.randn(len(x))

p0 = [7, 0.4, 0]

plsq = optimize.leastsq(residuals, p0, args=(y1, x))

print u"真实:", [A, k, theta]
print u"n拟合:", plsq[0]

plt.plot(x, y1, "o", label=u"实验")
plt.plot(x, y0, label=u"真实")
plt.plot(x, func(x, plsq[0]), label=u"拟合")
plt.legend(loc="best")

plt.savefig("fit", ftm="png")
plt.show()
