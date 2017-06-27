#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


x = symbols("x")
a = Integral(cos(x)*exp(x), x)
print(Eq(a, a.doit()))
