#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import sympy


x = sympy.symbols("x", real=True)
f = sympy.symbols("f", cls=sympy.Function)
fdot = sympy.Derivative(f(x), x)

result = sympy.dsolve(fdot - f(x), f(x))
print(result)
