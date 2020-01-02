#!/usr/bin/python
from numpy.linalg import inv
import numpy as np
a = np.array([[1, 0.1, 0.2], [0, 1, 0.3], [0, 0, 1]])
print a
b = inv(a)
print b
print a * b