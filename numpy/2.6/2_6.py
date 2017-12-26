#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


a = np.arange(24)
print(a)
b = a.reshape(2, 3, 4)
print(b)
c = b.ravel()
print(c)
print(b)
d = b.flatten()
print(d)
print(b)
f = b.transpose()
print(f)
print(b)
g = b.resize((2, 12))
print(g)
print(b)
