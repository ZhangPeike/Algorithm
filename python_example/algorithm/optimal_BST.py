#!/usr/bin/python
import numpy as np

# Alg15.5: find the optimal Binary-Search-Tree
# Recursive solution:
# e[i,j]=q_{i-1},if j=i-1;
# e[i,j]=min{e[i,r-1]+e[r+1,j]+w[i,j]},if i<=j;
# w[i,j]=w[i,j-1]+p_j+q_j
#index range explain: e[1~n+1,0~n],w[1~n,0~n]


# Attention the index is identical to the ref book
def OptimalBST(p, q, n):
    e = np.zeros((n + 2, n + 1), np.float)
    w = np.zeros((n + 2, n + 1), np.float)
    root = np.zeros((n + 1, n + 1), np.int)
    for i in range(1, n + 1):
        e[i, i - 1] = p[i - 1]
        w[i, i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i, j] = np.inf
            w[i, j] = w[i, j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = w[i, j] + e[i, r - 1] + e[r + 1, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j] = r
    return e, root


#Like middle-order
#ERROR
def ConstructOptimalBST(root, i, j, r_prime, root_flag):
    if i >= root.shape[0] or j >= root.shape[0]:
        return
    r = root[i, j]
    if root_flag:
        print("k%d is the root" % r)
        root_flag = False
        ConstructOptimalBST(root, i, r - 1, r, root_flag)
        ConstructOptimalBST(root, r + 1, j, r, root_flag)
        # attention, return must be used.
        return
    if i > (j + 1):
        return
    elif i == (j + 1):
        if j < r_prime:
            print("d%d is the left child of k%d" % (i - 1, r))
            print("d%d is the right child of k%d" % (i, r))
        return
    else:
        if r < r_prime:
            print("k%d is the left child of k%d" % (r, r_prime))
        else:
            print("k%d is the left child of k%d" % (r, r_prime))
    ConstructOptimalBST(root, i, r - 1, r, root_flag)
    ConstructOptimalBST(root, r + 1, j, r, root_flag)


def main():
    # the first 0 is left to make index correct.
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    _, root = OptimalBST(p, q, 5)
    # ConstructOptimalBST(root, 1, 5, 0, True)


if __name__ == "__main__":
    main()