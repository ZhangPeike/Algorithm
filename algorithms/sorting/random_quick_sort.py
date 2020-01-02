#!/usr/bin/python
import random
from quick_sort import Partition
# print random.randint(1,10) 
def RandomizedPartition(A,p,r):
    i = random.randint(p,r)
    tmp=A[i]
    A[i]=A[r]
    A[r]=tmp
    return Partition(A,p,r)

def RandomizedQuickSort(A,p,r):
    if p<r:
        q=RandomizedPartition(A,p,r)
        RandomizedQuickSort(A,p,q-1)
        RandomizedQuickSort(A,q+1,r)

def main():
    A = [0, 6, 5, 2, 9, 7]
    RandomizedQuickSort(A, 1, 5)
    print A

if __name__ == "__main__":
    main()
