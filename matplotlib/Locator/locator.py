#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from fractions import Fraction
from matplotlib.ticker import MultipleLocator, FuncFormatter


x = np.arange(0, 4*np.pi, 0.01)
fig, ax = plt.subplots(figsize=(8, 4))
plt.plot(x, np.sin(x), x, np.cos(x))


def pi_formatter(x, pos):
    frac = Fraction(int(np.round(x/(np.pi/4))), 4)
    d, n = frac.denominator, frac.numerator
    if frac == 0:
        return "0"
    elif frac == 1:
        return "$\pi$"
    elif d == 1:
        return r"${%d} \pi$" % n
    elif n == 1:
        return r"$\frac{\pi}{%d}$" % d
    return r"\frac{%d \pi}{%d}" % (n, d)


plt.ylim(-1.5, 1.5)
plt.xlim(0, np.max(x))

plt.subplots_adjust(bottom=0.15)

plt.grid()

ax.xaxis.set_major_locator(MultipleLocator(np.pi/4))

ax.xaxis.set_major_formatter(FuncFormatter(pi_formatter))

# ax.xaxis.set_minor_locator(MultipleLocator(np.pi/20))

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)


plt.savefig("locator", ftm="png")
plt.show()
