#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import sympy


x = sympy.symbols("x")
f = sympy.symbols("f", cls=sympy.Function)

eq = sympy.Eq(f(x).diff(x) + f(x), (sympy.cos(x)-sympy.sin(x))*f(x)**2)
solution = sympy.classify_ode(eq, f(x))
print(solution)

result = sympy.dsolve(eq, f(x), hint="lie_group")
print(result)
