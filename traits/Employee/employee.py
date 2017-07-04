#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from traits.api import HasTraits, Str, Int


class Employee(HasTraits):
    """Documentation for Employee
    """
    name = Str
    department = Str
    salary = Int
    bonus = Int
    

Employee().configure_traits()
