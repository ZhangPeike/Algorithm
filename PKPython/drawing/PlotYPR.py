#!/usr/bin/python
import os
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
rec_file = sys.argv[1]
data = np.loadtxt(rec_file)
num = data.shape[0]
ticks = data[:, 0] - data[0, 0]
ticks = ticks / 1e6
plt.plot(ticks, data[:, 1], linestyle='--', marker='.', color='r')
plt.plot(ticks, data[:, 2], linestyle='--', marker='.', color='g')
plt.plot(ticks, data[:, 3], linestyle='--', marker='.', color='b')
plt.plot(ticks, [1.0 for x in data[:, 0]],
         linestyle='--',
         marker='.',
         color='r')
plt.grid(True)
plt.xlim((0, ticks[-1]))
plt.ylim((-2, 2))
plt.xticks(np.arange(0, math.ceil(ticks[-1]), 2))
plt.yticks(np.arange(-2, 2.1, 0.1))
plt.xlabel("/s")
plt.ylabel("m/s^2")
plt.legend(loc='upper left')
plt.title("IMU data")
plt.show()
