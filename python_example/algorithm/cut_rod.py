#!/usr/bin/python
import math
import time


#p: price_list
class DynamicProgramming(object):
    def __init__(self, n):
        self.r_ = [-float('inf') for i in range(n + 1)]
        self.p_ = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.cnt_recursive_ = 0
        self.cnt_dp_ = 0

    #n: the lenght of the steel rod
    def CutRod(self, n):
        self.cnt_recursive_ = self.cnt_recursive_ + 1
        print("Recursive: %d" % self.cnt_recursive_)
        if n == 0:
            return 0
        q = -float('inf')
        for i in range(1, n + 1):
            q = max(q, self.p_[i - 1] + self.CutRod(n - i))
        return q

    def MemoizedCutRod(self, n):
        return self.MemoizedCutRodAux(n)

    def MemoizedCutRodAux(self, n):
        self.cnt_dp_ = self.cnt_dp_ + 1
        print("DynamicProgramming: %d" % self.cnt_dp_)
        q = -float('inf')
        if self.r_[n] >= 0:
            return self.r_[n]
        if n == 0:
            q = 0
        else:
            for i in range(1, n + 1):
                q = max(q, self.p_[i - 1] + self.MemoizedCutRodAux(n - i))
        self.r_[n] = q
        return q


if __name__ == "__main__":
    dp = DynamicProgramming(10)
    ts = time.time()
    print(dp.CutRod(10))
    te = time.time()
    print("Recursive cost time: %.6f" % (te - ts))
    ts = time.time()
    print(dp.MemoizedCutRod(10))
    te = time.time()
    print("DP cost time: %.6f" % (te - ts))
