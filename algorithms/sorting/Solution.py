#!/usr/bin/env python3
from quick_sort import QuickSort


class Solution():
    def __init__(self):
        print("Wen gu er zhi xin")

    #para a is a list or array
    #p is start index for sorting
    #r is end index for sorting
    def QuickSort(self, a, p, r):
        if p < r:
            # q is the pivot
            q = self.Partition(a, p, r)
            self.QuickSort(a, p, q - 1)
            self.QuickSort(a, q + 1, r)

    #Aux for quick sorting, parti the array into two section,
    #the small numbers in front, the pivot, the big numbers
    def Partition(self, a, p, r):
        x = a[r]
        i = p - 1
        # attention: end with r-1
        for j in range(p, r):
            if a[j] < x:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1


def main():
    A = [0, 2, 8, 3, 6, 9, 5, 99, 10, 7]
    # QuickSort(A, 1, 9)
    # print(f'ref algo QuickSort: {A}')
    pro = Solution()
    pro.QuickSort(A, 1, len(A) - 1)
    print(f'ref algo QuickSort: {A}')


if __name__ == "__main__":
    main()