#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


for idx, color in enumerate("rgbyck"):
    plt.subplot(321+idx, facecolor=color)

plt.savefig("subplot", fmt="png")
plt.show()
