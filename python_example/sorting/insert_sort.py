#!/usr/bin/python
def InsertSort(A):
    for j in range(2, len(A)):
        key = A[j]
        i = j-1
        while i > 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    # return A

def main():
    A=[0,5,2,3,6,7,1]
    InsertSort(A)
    print A

if __name__ == "__main__":
    main()