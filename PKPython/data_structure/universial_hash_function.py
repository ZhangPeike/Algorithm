#!/usr/bin/python2
print little_primes
import math


def IsNumPrime(d):
    if d + 1 == 0:
        return False
    # if isinstance()
    sqrt_d = math.sqrt(d)
    n = 2
    while n <= sqrt_d:
        if d % n == 0:
            return False
        n = n + 1
    return True


#
def UniversialHash(a, b, m, p, k):
    return ((a * k + b) % p) % m


def main():
    max = 2**10
    little_primes = [x for x in range(2, max) if IsNumPrime(x)]
    print little_primes
    n = input('enter total number of elements:')
    alpha = input('enter expected query times:')
    m = (int)(n / alpha)
    print "slots num: %d" % m
    # error
    # m = (int) n / alpha
    id = 0
    index = id
    max = float('inf')
    for x in little_primes:
        diff = abs(m - x)
        if diff < max:
            max = diff
            index = id
        id = id + 1
    m = little_primes[index]
    print "computed the m: %d"%m
    # print max
    # while True:
    #     n = input("enter a number and determine it is a prime number or not:")
    #     if n==1 or n==0:
    #         break
    #     if IsNumPrime(n):
    #         print "%d is a prime num" % n
    #     else:
    #         print "%d is NOT a prime num" % n

    # a = input('enter a:')
    # b = input('enter b:')
    # m = input('enter m:')
    # p = input('enter p:')
    # k = input('enter k:')
    # print 'hash: ', UniversialHash(a, b, m, p, k)
    # name_US='USA'
    # print name_US
    # for x in name_US:
    #     print("%d"%ord(x))
    # name_CN='China'
    # print name_CN
    # for x in name_CN:
    #     print("%d"%ord(x))


if __name__ == "__main__":
    print "this is universial hash:"
    main()
