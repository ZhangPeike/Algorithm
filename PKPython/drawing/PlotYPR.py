#!/usr/bin/python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
# TODO: add plot for IMU orientation
rec_file = sys.argv[1]
data = np.loadtxt(rec_file)
rows = data.shape[0]
# plt.plot(np.arange(0, rows), data[:, 0], linestyle='--', marker='.', color='r')
plt.plot(np.arange(0, rows),
         data[:, 1], linestyle='--', marker='.', color='g', label='pitch')
plt.plot(np.arange(0, rows),
         data[:, 2], linestyle='--', marker='.', color='b', label='roll')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()
