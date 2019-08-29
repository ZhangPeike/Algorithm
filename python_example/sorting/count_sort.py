#!/bin/python
# the number in A must be non-negtive interga
def count_sort(A):
    # find the min max value of A
    min = 0
    k = 6
    # initial a zeros which has k numbers
    C = []
    B = A
    for i in range(k):
        C.append(0)
    for i in range(1, len(A)):
        C[A[i]] = C[A[i]]+i
    for i in range(1, k+1):
        # error
        # C[A[i]] = C[A[i]]+C[A[i-1]]
        C[i]=C[i]+C[i-1]
    for i in range(len(A),0,-1):
        B[C[A[i]]]=A[i]
        C[A[i]]=C[A[i]]-1