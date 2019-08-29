#!/usr/bin/python
import numpy as np


# x - y is observation data, beta is the model's param
# jacobian
def J(x, beta):
    ans = np.zeros((7, 2))
    for i in range(7):
        ans[i, 0] = -x[i] / (beta[1] + x[i])
        ans[i, 1] = beta[0] * x[i] / ((beta[1] + x[i])**2)
    return ans


# residual
def R(x, y, beta):
    ans = np.zeros((7, 1))
    for i in range(7):
        ans[i, 0] = y[i] - (beta[0] * x[i] / (beta[1] + x[i]))
    return ans


# delta of beta
def D(j, r):
    ans = np.zeros((2, 1))
    jt = np.transpose(j)
    ans = -np.dot(np.dot(np.linalg.inv(np.dot(jt, j)), jt), r)
    return ans


if __name__ == "__main__":
    x = np.asarray([0.038, 0.194, 0.425, 0.626, 1.253, 2.500, 3.740])
    y = np.asarray([0.050, 0.127, 0.094, 0.2122, 0.2729, 0.2665, 0.3317])
    x.shape = (7, 1)
    y.shape = (7, 1)
    print "x: \n", x
    print "y: \n", y
    num_iter = 5
    beta = np.zeros((2, 1))
    beta[0] = 0.9
    beta[1] = 0.2
    print beta
    for i in range(5):
        beta = beta + D(J(x, beta), R(x, y, beta))
    print beta
