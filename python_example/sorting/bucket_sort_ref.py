#!/usr/bin/python
class bucketSort(object):
    def insertSort(self,a):
        n=len(a)
        if n<=1:
            pass
        for i in range(1,n):
            key=a[i]
            j=i-1
            while key<a[j] and j>=0:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
    def sort(self,a):
        n=len(a)
        s=[[] for i in xrange(n)]
        for i in a:
            s[int(i*n)].append(i)
        for i in s:
            self.insertSort(i)
        return [i for j in s for i in j]
    def __call__(self,a):
        return self.sort(a)
                       
if __name__=='__main__':
    from random import random
    from timeit import Timer
    a=[random() for i in xrange(12)]
    def test_bucket_sort():
        print bucketSort()(a)
    def test_builtin_sort():
        print sorted(a)
    tests=[test_bucket_sort,test_builtin_sort]
    for test in tests:       
        name=test.__name__
        t=Timer(name+'()','from __main__ import '+name)
        print t.timeit(1)