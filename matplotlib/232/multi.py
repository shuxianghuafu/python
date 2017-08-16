#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def func1(x):
    return 0.6*x + 0.3


def func2(x):
    return 0.4*x*x + 0.1*x + 0.2


def find_curve_intersects(x, y1, y2):
    d = y1 - y2
    idx = np.where(d[:-1]*d[1:] <= 0)[0]
    x1, x2 = x[idx], x[idx+1]
    d1, d2 = d[idx], d[idx+1]
    return -d1*(x2-x1)/(d2-d1) + x1


x = np.linspace(-3, 3, 100)
f1 = func1(x)
f2 = func2(x)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, f1)
ax.plot(x, f2)

x1, x2 = find_curve_intersects(x, f1, f2)
ax.plot(x1, func1(x1), "o")
ax.plot(x2, func2(x2), "o")

ax.fill_between(x, f1, f2, where = f1>f2, facecolor = "green", alpha = 0.5)
