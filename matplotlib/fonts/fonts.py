#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os.path
import os


fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(1, 1, 1)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])

x, y = 0.05, 0.05
fonts = [font.name for font in fontManager.ttflist if path.exists(font.fname) and os.stat(font.fname).st_size > 1e6]
font = set(fonts)
dy = (1.0 -y) / (len(fonts) / 4 + len(fonts)%4 != 0)

for font in fonts:
    t = ax.text(x, y+dy/2, u"ÖĞÎÄ×ÖÌå", )
