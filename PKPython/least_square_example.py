#!/usr/bin/python
import numpy as np
import scipy as sp
from scipy.optimize import leastsq

poly_order = 7


def RealFun(x):
    return np.sin(2 * np.pi * x)


x = np.linspace(0, 3, 10)
y_real = RealFun(x)
y_noise = [y + np.random.normal(0, 0.1) for y in y_real]
print y
print type(y)
print type(y_noise)


def FitFun(p, x):
    f = np.poly1d(p)
    return f(x)


def ResidualFun(p, x, y):
    res = FitFun(p, x) - y
    return res


para_init = np.random.rand(poly_order)
print "Parameter init:"
print para_init

problem = leastsq(ResidualFun, para_init, args=(y_noise, x))
print "Least square result parameter:"
print problem[0]