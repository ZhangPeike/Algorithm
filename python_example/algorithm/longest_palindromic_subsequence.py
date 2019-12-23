#!/usr/bin/python
#Method I: direct DP
#Method II: find LCS of the sequence and its reverse
from longest_common_subsequence import LongestCommonSubsequence
from longest_common_subsequence import GetLongestCommonSubsequence


#TODO: method I.
def LongestPalindromicSubsequence(s):
    print


def LongestPalindromicSubsequenceUsingCommonSubsequence(s):
    lps = []
    sp = s[::-1]
    B, _ = LongestCommonSubsequence(s, sp)
    length = len(s)
    GetLongestCommonSubsequence(B, s, length, length, lps)
    return lps


def main():
    str1 = "hello"
    str2 = "abalab"
    str3 = "racecar"
    print(LongestPalindromicSubsequenceUsingCommonSubsequence(str1))
    print(LongestPalindromicSubsequenceUsingCommonSubsequence(str2))
    print(LongestPalindromicSubsequenceUsingCommonSubsequence(str3))


if __name__ == "__main__":
    main()
