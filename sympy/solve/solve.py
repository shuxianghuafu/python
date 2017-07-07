#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


a, b, c = sympy.symbols("a, b, c")
x = sympy.symbols("x")
anwser = sympy.solve(a*x**2 + b*x + c, x)

for i in anwser:
    print i
