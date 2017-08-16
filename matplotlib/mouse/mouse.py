#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class CurveHighLighter(object):
    """Documentation for CurveHighLighter
    """
    def __init__(self, ax, alpha=0.3, linewidth=3):
        self.ax = ax
        self.alpha = alpha
        self.linewidth = linewidth

        ax.figure.canvas.mpl_connect('motion_notify_event', self.on_move)

    def highlight(self, target):
        need_redraw = False
        if target is None:
            for line in self.ax.lines:
                line.set_alpha(1.0)
                if line.get_linewidth() != 1.0:
                    line.set_linewidth(1.0)
                    need_redraw = True

        else:
            for line in self.ax.lines:
                lw = self.linewidth if line is target else 1
                if line.get_linewidth() ！= lw:
                    line.set_linewidth(lw)
                    need_redraw = True
alpha = 1.0 if lw == self.linewidth else self.alpha
