#!/usr/bin/python
import os
import sys
import math


class Heap(object):
    def __init__(self, num_array):
        self.array = []
        # not used first num
        self.array.append(0)
        self.heap_size = len(num_array)
        for x in num_array:
            self.array.append(x)

    def index(self, i):
        return self.array[i]

    def size(self):
        return self.heap_size

    def set_index(self, i, digital):
        self.array[i] = digital

    def set_size(self, n):
        self.heap_size = n

    def raw_size(self):
        return len(self.array)-1


def LEFT(i):
    return i*2


def RIGHT(i):
    return i*2+1


def MaxHeapify(A, i):
    l = LEFT(i)
    if l <= A.size() and A.index(l) > A.index(i):
        largest = l
    else:
        largest = i
    r = RIGHT(i)
    if r <= A.size() and A.index(r) > A.index(largest):
        largest = r
    if largest != i:
        tmp = A.index(i)
        A.set_index(i, A.index(largest))
        A.set_index(largest, tmp)
        MaxHeapify(A, largest)
    else:
        return


def BuildMaxHeap(A):
  # this is key number.
    for i in range(int(math.floor(A.size()/2)), 0, -1):
        MaxHeapify(A, i)


def HeapSort(A):
    BuildMaxHeap(A)
    for i in range(A.size(), 1, -1):
        tmp = A.index(i)
        A.set_index(i, A.index(1))
        # A[0] = tmp
        A.set_index(1, tmp)
        new_num = A.size()-1
        A.set_size(new_num)
        MaxHeapify(A, 1)


def main():
    test_num = [99, 6, 9, 8, 11, 5]
    my_heap = Heap(test_num)
    HeapSort(my_heap)
    for i in range(my_heap.raw_size()):
        print my_heap.index(i+1)


if __name__ == "__main__":
    main()
