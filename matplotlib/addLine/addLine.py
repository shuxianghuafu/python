#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


fig = plt.figure()
line1 = Line2D([0, 1], [0, 1], transform=fig.transFigure,
               figure=fig, color="r")
line2 = Line2D([0, 1], [1, 0], transform=fig.transFigure,
               figure=fig, color="g")
fig.lines.extend([line1, line2])

plt.savefig("addLine", ftm="png")
plt.show()
