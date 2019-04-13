#!/usr/bin/python
import math


def Merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    L.append(0)
    R.append(0)
    for i in range(p, q+1):
        L.append(A[i])
    for i in range(q+1, r+1):
        R.append(A[i])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 1
    j = 1
    for n in range(p, r+1):
        if L[i] <= R[j]:
            A[n] = L[i]
            i = i+1
        else:
            A[n] = R[j]
            j = j+1


def MergeSort(A, p, r):
    if p < r:
        q = int(math.floor((p+r)/2))
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)


def main():
    A = [0, 6, 5, 2, 9, 7]
    MergeSort(A, 1, 5)
    print A


if __name__ == "__main__":
    main()
