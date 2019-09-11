#!/usr/bin/python
import math
import time
import numpy as np


class DynamicProgramming(object):
    #c: a_cut_cost
    #p: price_list
    # TODO: make n adjustable, make p_ modified by setter
    def __init__(self, n, c=0.0):
        self.c_ = c
        self.r_ = [-float('inf') for i in range(n + 1)]
        self.s_ = [0 for i in range(n + 1)]
        self.r_bottom_up_ = [0 for i in range(n + 1)]
        self.p_ = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        # matrix chain multiply, the first 0 is no use.
        self.mat_sz_ = [30, 35, 15, 5, 10, 20, 25]
        self.mat_num_ = len(self.mat_sz_) - 1
        # be identical to the algo MatrixChainOrder
        self.mat_m_ = np.zeros((self.mat_num_ + 1, self.mat_num_ + 1),
                               dtype=float)
        self.mat_s_ = np.zeros((self.mat_num_ + 1, self.mat_num_ + 1),
                               dtype=float)
        self.cnt_recursive_ = 0
        self.cnt_dp_ = 0
        self.cnt_finbonacci_ = 0
        self.cnt_finbonacci_dp_ = 0
        self.Finbonacci_ = [0, 1]

    #n: the lenght of the steel rod
    def CutRod(self, n):
        self.cnt_recursive_ = self.cnt_recursive_ + 1
        # print("Recursive: %d" % self.cnt_recursive_)
        if n == 0:
            return 0
        q = -float('inf')
        for i in range(1, n + 1):
            if i < n:
                q = max(q, self.p_[i - 1] + self.CutRod(n - i) - self.c_)
            else:
                q = max(q, self.p_[i - 1])
        return q

    def MemoizedCutRod(self, n):
        print("cut cost: %.3f" % self.c_)
        return self.MemoizedCutRodAux(n)

    def MemoizedCutRodAux(self, n):
        self.cnt_dp_ = self.cnt_dp_ + 1
        # print("DynamicProgramming: %d" % self.cnt_dp_)
        q = -float('inf')
        if self.r_[n] >= 0:
            return self.r_[n]
        if n == 0:
            q = 0
        else:
            for i in range(1, n + 1):
                if i < n:
                    q = max(
                        q, self.p_[i - 1] + self.MemoizedCutRodAux(n - i) -
                        self.c_)
                else:
                    q = max(q, self.p_[i - 1])
            self.r_[n] = q
        return q

    def BottomUpCutRod(self, n):
        for j in range(1, n + 1):
            q = -float('inf')
            for i in range(1, j + 1):
                if i < j:
                    q = max(
                        q, self.p_[i - 1] + self.r_bottom_up_[j - i] - self.c_)
                else:
                    q = max(q, self.p_[i - 1])
            self.r_bottom_up_[j] = q
        return self.r_bottom_up_[n]

    def ExtendedBottomUpCutRod(self, n):
        for j in range(1, n + 1):
            q = -float('inf')
            for i in range(1, j + 1):
                if q < self.p_[i - 1] + self.r_bottom_up_[j - i]:
                    q = self.p_[i - 1] + self.r_bottom_up_[j - i]
                    self.s_[j] = i
            self.r_bottom_up_[j] = q
        return self.r_bottom_up_, self.s_

    def PrintCutRodSolution(self, n):
        r, s = self.ExtendedBottomUpCutRod(n)
        while n > 0:
            print s[n]
            n = n - s[n]

    def Finbonacci(self, n):
        self.cnt_finbonacci_ = self.cnt_finbonacci_ + 1
        if n > 1:
            return self.Finbonacci(n - 1) + self.Finbonacci(n - 2)
        elif n == 1:
            return 1
        elif n == 0:
            return 0

    def MemoizedFinbonacci(self, n):
        self.cnt_finbonacci_dp_ = self.cnt_finbonacci_dp_ + 1
        n_ready = len(self.Finbonacci_)
        if n < n_ready:
            return self.Finbonacci_[n]
        else:
            for i in range(n_ready, n + 1):
                self.Finbonacci_.append(
                    self.MemoizedFinbonacci(i - 1) +
                    self.MemoizedFinbonacci(i - 2))
            return self.Finbonacci_[n]

    def CountFinbonacci(self):
        return self.cnt_finbonacci_

    def CountFinbonacciDP(self):
        return self.cnt_finbonacci_dp_

    def MatrixChainOrder(self):
        for i in range(1, self.mat_num_ + 1):
            self.mat_m_[i, i] = 0
        for l in range(2, self.mat_num_ + 1):
            for i in range(1, self.mat_num_ - l + 2):
                j = i + l - 1
                self.mat_m_[i, j] = float('inf')
                for k in range(i, j):
                    q = self.mat_m_[i, k] + self.mat_m_[
                        k + 1, j] + self.mat_sz_[
                            i - 1] * self.mat_sz_[k] * self.mat_sz_[j]
                    if q < self.mat_m_[i, j]:
                        self.mat_m_[i, j] = q
                        self.mat_s_[i, j] = k
        return self.mat_m_, self.mat_s_


if __name__ == "__main__":
    dp = DynamicProgramming(10, 0.5)
    ts = time.time()
    print(dp.CutRod(4))
    te = time.time()
    print("Recursive cost time: %.6f" % (te - ts))
    ts = time.time()
    print(dp.MemoizedCutRod(4))
    te = time.time()
    print("DP cost time: %.6f" % (te - ts))
    print("BottomUpCutRod: ")
    print(dp.BottomUpCutRod(4))
    dp.PrintCutRodSolution(4)
    print("Finbonacci number n=10:")
    print(dp.Finbonacci(10))
    print(dp.CountFinbonacci())
    print("Finbonacci DP:")
    print(dp.MemoizedFinbonacci(10))
    a, b = dp.MatrixChainOrder()
    print("Matrix Chain Multiple:")
    print(a)
    print("solution:")
    print(b)
