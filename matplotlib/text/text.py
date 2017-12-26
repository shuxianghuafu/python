#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 10)
y = x**2

fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
ax.plot(x, y)

for i, (_x, _y) in enumerate(zip(x, y)):
    ax.text(_x, _y, str(i), color="red", fontsize=i+10)


ax.text(0.5, 0.8, u"axes text", color="blue", ha="center",
        transform=ax.transAxes)

plt.figtext(0.1, 0.92, u"figure text", color="green")

plt.show()
