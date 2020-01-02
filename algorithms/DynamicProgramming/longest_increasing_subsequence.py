#!/usr/bin/python3


def LongestIncreasingSubsequence(s):
    n = len(s)
    LIS = [1 for i in range(n)]
    LIS[0] = 1
    if s[0] < s[1]:
        LIS[1] = 2
    else:
        LIS[1] = 1
    for i in range(2, n):
        for j in range(i):
            if s[j] < s[i]:
                if LIS[i] < (LIS[j] + 1):
                    LIS[i] = (LIS[j] + 1)
            else:
                continue
    v = max(LIS)
    return v, LIS.index(v)


def GetLongestIncreasingSubsequence(s, LIS):
    pass


def main():
    s = "characterz"
    s1 = "3567812"
    print(LongestIncreasingSubsequence(s))
    print(LongestIncreasingSubsequence(s1))


if __name__ == "__main__":
    main()