#!/usr/bin/python
class BucketSort(object):
    pass
    # for x in xrange(9):
    #     print x
def bucket_sort(A):
    n = len(A)
    # let's creat an array of linked list, the size of array is same with the size of A
    B = [[] for i in xrange(n)]
    for i in A:
        # B[int(i*10)].append(i)
        B[int(i*n)].append(i)
    for unit_list in B:
        unit_list_len=len(unit_list)
        if unit_list_len<2:
            pass
        else:
            # let's do insert soring for unit_list
            for i in range(1, unit_list_len):
                key=unit_list[i]
                j=i-1
                while key<unit_list[j] and j>=0:
                    unit_list[j+1]=unit_list[j]
                    j=j-1 
                unit_list[j+1]=key
    # like:
    # C = []
    # for unit_list_tmp in B:
    #     for num in unit_list_tmp:
    #         C.append(num)
    # return C
    return [num for unit_list_tmp in B for num in unit_list_tmp]


if __name__ == "__main__":
    from random import random
    from timeit import Timer 
    a = [random() for i in xrange(15)]
    print "Original list: ",a
    b = bucket_sort(a)
    print "Sorted list: ",b

