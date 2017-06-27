#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.random.randn(100000)
plt.hist(x, bins=50, range=(x.min(), x.max()), histtype="step")
plt.show()
