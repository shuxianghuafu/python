#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from traits.api import HasTraits, Color


class Circle(HasTraits):
    color = Color


c = Circle()
c.configure_traits()
