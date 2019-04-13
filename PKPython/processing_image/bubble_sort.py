#!/usr/bin/python
# A[0] is invalid!


def BubbleSort(A):
    for i in range(1, len(A)):
        # print range(len(A), i, -1)
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp


def main():
    A = [0, 1, 2, 9, 7]
    BubbleSort(A)
    print A


if __name__ == "__main__":
    main()
