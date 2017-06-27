#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


data = np.random.normal(0, 20, 1000)

# fixed bin size
bins = np.arange(-100, 100, 5)

plt.xlim([min(data)-5, max(data)+5])
plt.hist(data, bins=bins, alpha=0.5)
plt.title("Random Gausian data (fixed bin size)")
plt.xlabel("variable x (bin size = 5)")
plt.ylabel("count")

plt.savefig("hist1.png")
plt.show()
