#!/usr/bin/python
def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1


def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)


def main():
    A = [0, 2, 8, 3, 6, 9, 5, 99, 10, 7]
    QuickSort(A, 1, 9)
    print(A)


if __name__ == "__main__":
    main()
