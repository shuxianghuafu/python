#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
result = ax.hist(np.random.randn(100000), bins=500, facecolor="blue")
print(len(result))

# 设置第一个条的颜色
result[2][0].set_facecolor('red')

plt.show()
