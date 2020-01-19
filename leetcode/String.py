#!/usr/bin/env python3
def Reverse(s, start, stop):
    snew = list(s)
    while start < stop:
        snew[start], snew[stop] = snew[stop], snew[start]
        start = start + 1
        stop = stop - 1
    return "".join(snew)


def RotationString(s, n):
    sh = Reverse(s, 0, n)
    # print(sh)
    m = len(s) - 1
    st = Reverse(s, n + 1, m)
    # print(st)
    tmp = sh[0:n + 1] + (st[n + 1:m + 1])
    # print(tmp)
    return Reverse(tmp, 0, m)


def ReverseWord(words):
    list_word = words.split()
    # print(list_word)
    return (" ".join(list_word[::-1]))


def main():
    str = "abcdef"
    print(RotationString(str, 2))


if __name__ == "__main__":
    main()
    print(ReverseWord("Hello world!"))