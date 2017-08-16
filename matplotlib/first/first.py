#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import sympy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

fig = plt.figure(figsize=(8, 4))

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Pyplot First Example")
plt.ylim(-1.2, 1.2)
plt.legend()

plt.show()
