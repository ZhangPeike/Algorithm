#!/usr/bin/python
import numpy as np
def Partition(A,p,r):
    x=A[r]    
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            tmp=A[j]
            A[j]=A[i]
            A[i]=tmp
    A[r]=A[i+1]
    A[i+1]=x
    return i+1

def RandomizedPartition(A,p,r):
    i=np.random.randint(p,r+1)
    tmp=A[i]
    A[i]=A[r]
    A[r]=tmp
    return Partition(A,p,r)

if __name__ == "__main__":
    A=[2,8,7,1,3,5,6,4]
    print RandomizedPartition(A, 0, len(A)-1)
    print A