#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from os import path


fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(1, 1, 1)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])

x, y = 0.05, 0.05
fonts = [font.name for font in fontManager.ttflist if path.exists(font.name) and
         os.stat(font.fname).st_size > 1e6]
font = set(fonts)

dy = (1.0-y) / (len(fonts)) // 4 + (len(fonts)%4 != 0)

for font in fonts:
    t = ax.text(x, y+dy/2, u"中文字体",
                {"fontname":font, "fontsize":14}, transform=ax.transAxes)
    ax.text(x, y, font, {"fontsize":12}, transform=ax.transAxes)
    x += 0.25
    if x >= 1.0:
        y += dy
        x = 0.05

plt.show()
