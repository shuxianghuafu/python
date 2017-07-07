#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x, y = sympy.symbols("x, y")
anwser = sympy.solve((x**2 + x*y  +1, y**2 + x*y + 2), x, y)

for i in anwser:
    print i
