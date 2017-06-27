#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


data = np.random.normal(0, 20, 1000)

bins = np.linspace(math.ceil(min(data)),
                   math.floor(max(data)),
                   20)

plt.xlim([min(data)-5, max(data)+5])

plt.hist(data, bins=bins, alpha=0.5)
plt.title("Random Gaussian data (fixed number of bins)")
plt.xlabel("variable x (20 enenly spaced bins)")
plt.ylabel("count")

plt.savefig("histgram.png")
plt.show()
