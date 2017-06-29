#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8, 8), dpi=100)

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Times(s)")
plt.ylabel("Volt")
plt.title("Pyplot First Example")
plt.ylim(-1.2, 1.2)
plt.xlim(0, 10)
plt.legend(loc=("upper right"))

plt.savefig("fast.png")
plt.show()
