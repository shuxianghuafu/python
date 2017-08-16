#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


for idx, color in enumerate("rgbyck"):
    ax = plt.subplot(321+idx, facecolor=color)
    ax.subplots_adjust(left=0.1, right=0.1, bottom=0.1)


plt.show()
