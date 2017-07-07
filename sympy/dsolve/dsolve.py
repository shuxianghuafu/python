#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
from sympy import *
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = sympy.symbols("x")
f = sympy.symbols("f", cls=Function)
anwser = sympy.dsolve(Derivative(f(x), x) - f(x), f(x))

print anwser
