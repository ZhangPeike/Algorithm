#!/usr/bin/python
import numpy as np


# make index start from 0
def SolveCoefficients4NaturalCubicSpline(list_float_x, list_float_y):
    n = len(list_float_x)
    if n != len(list_float_y):
        # TODO: handle error
        return
    if n < 2:
        return
    # TODO: check grammer
    a = [list_float_y[i] for i in range(n - 1)]
    a = np.asarray(a)
    a.shape = (n - 1, 1)
    epsilon = [list_float_x[i + 1] - list_float_x[i] for i in range(n - 1)]
    delta = [list_float_y[i + 1] - list_float_y[i] for i in range(n - 1)]
    A = np.zeros((n, n), dtype=np.float64)
    A[0, 0] = 1.0
    A[n - 1, n - 1] = 1.0
    b = np.zeros((n, 1), dtype=np.float64)
    b[0] = 0
    b[n - 1] = 0
    for row in range(1, n - 1):
        i = row - 1
        A[row, row - 1:row + 2] = np.asarray(
            [epsilon[i], 2 * (epsilon[i] + epsilon[i + 1]), epsilon[i + 1]])
        b[row] = 3 * ((delta[i + 1] / epsilon[i + 1]) -
                      (delta[i] / epsilon[i]))
    print("Ax = b")
    print("A:")
    print(A)
    print("b:")
    print(b)
    c = np.linalg.solve(A, b)
    print("Result")
    print c
    b = np.zeros((n - 1, 1), dtype=np.float64)
    d = np.zeros((n - 1, 1), dtype=np.float64)
    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / (3.0 * epsilon[i])
        b[i] = delta[i] / epsilon[i] - epsilon[i] * (2 * c[i] + c[i + 1]) / 3
    return a, b, c, d


if __name__ == "__main__":
    np.set_printoptions(precision=3)
    list_x = [1, 2, 4, 5]
    list_y = [2, 1, 4, 3]
    ans = SolveCoefficients4NaturalCubicSpline(list_x, list_y)
    print ans[0]
    print ans[1]
    print ans[2]
    print ans[3]
