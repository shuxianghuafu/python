#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import numpy as np
import matplotlib.pyplot as plt
import random


data1 = [random.gauss(15, 10) for i in range(5000)]
data2 = [random.gauss(5, 5) for i in range(5000)]
bins = np.arange(-60, 60, 2.5)
plt.xlim([min(data1+data2)-5, max(data1+data2)+5])

plt.hist(data1, bins=bins, alpha=0.3, label="class 1")
plt.hist(data2, bins=bins, alpha=0.3, label="class 2")
plt.title("Random Gaussian data")
plt.xlabel("variable x")
plt.ylabel("count")
plt.legend(loc="upper right")

plt.savefig("overlap.png")
plt.show()
