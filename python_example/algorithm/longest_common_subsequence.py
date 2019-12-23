#!/usr/bin/python3
import math
import time
import numpy as np
import sys
import math
from enum import Enum


class Ax(Enum):
    up = 0
    left = 1
    corner = 2


#return: B the result index, C the longest length.
def LongestCommonSubsequence(X, Y):
    m = len(X)
    n = len(Y)
    B = np.zeros((m + 1, n + 1), Ax)
    C = np.zeros((m + 1, n + 1), int)
    C[:, 0] = 0
    C[0, :] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # attention: index starts from 0, the following index is same.
            if X[i - 1] == Y[j - 1]:
                C[i, j] = C[i - 1, j - 1] + 1
                B[i, j] = Ax.corner
            elif C[i - 1, j] >= C[i, j - 1]:
                C[i, j] = C[i - 1, j]
                B[i, j] = Ax.up
            else:
                C[i, j] = C[i, j - 1]
                B[i, j] = Ax.left
    return B, C


def LCS_Length_min_space(X, Y):
    m = len(X)
    n = len(Y)
    if m < n:
        X, Y = Y, X
        m, n = n, m
    C = np.zeros((2, n + 1), int)
    for i in range(1, n + 1):
        if X[0] == Y[i - 1]:
            C[0, i] = 1
        else:
            C[0, i] = 0
    for i in range(1, n + 1):
        if X[1] == Y[i - 1]:
            C[1, i] = C[0, i - 1] + 1
        elif C[0, i] > C[1, i - 1]:
            C[1, i] = C[0, i]
        else:
            C[1, i] = C[1, i - 1]
    for i in range(3, m + 1):
        C[0, :] = C[1, :]
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[1, j] = C[0, j - 1] + 1
            elif C[0, j] > C[1, j - 1]:
                C[1, j] = C[0, j]
            else:
                C[1, j] = C[1, j - 1]
    return C[1, n]


def PrintLongestCommonSubsequence(B, X, X_len, Y_len):
    if X_len == 0 or Y_len == 0:
        return
    elif B[X_len, Y_len] == Ax.corner:
        PrintLongestCommonSubsequence(B, X, X_len - 1, Y_len - 1)
        print(X[X_len - 1])
    elif B[X_len, Y_len] == Ax.up:
        PrintLongestCommonSubsequence(B, X, X_len - 1, Y_len)
    # elif B[X_len, Y_len] == Ax.left:
    else:
        PrintLongestCommonSubsequence(B, X, X_len, Y_len - 1)


#TODO: get the array of LCS
# LCS = []


def GetLongestCommonSubsequence(B, X, X_len, Y_len, LCS):
    if X_len == 0 or Y_len == 0:
        return
    if B[X_len, Y_len] == Ax.corner:
        GetLongestCommonSubsequence(B, X, X_len - 1, Y_len - 1, LCS)
        LCS.append(X[X_len - 1])
    elif B[X_len, Y_len] == Ax.up:
        GetLongestCommonSubsequence(B, X, X_len - 1, Y_len, LCS)
    else:
        GetLongestCommonSubsequence(B, X, X_len, Y_len - 1, LCS)


if __name__ == "__main__":
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    B, _ = LongestCommonSubsequence(X, Y)
    lcs = []
    GetLongestCommonSubsequence(B, X, len(X), len(Y), lcs)
    print(lcs)
    print("Compare with the printing method")
    PrintLongestCommonSubsequence(B, X, len(X), len(Y))
    print("2 row method result LCS lenght: %d" % LCS_Length_min_space(X, Y))
