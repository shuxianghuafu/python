#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 1000)
y = np.sin(x)
y2 = np.cos(x)


fig = plt.figure(figsize=(6, 6), dpi=100)
axes = fig.add_subplot(1, 1, 1)
axes.fill_between(x, y, y2, where=(y>y2))

plt.show()
