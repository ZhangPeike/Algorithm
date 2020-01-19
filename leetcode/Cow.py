#!/usr/bin/env python3
# HD(杭电)OJ
def CowNum(n):
    if n < 2:
        return 2
    else:
        # index is starting from 1
        # each line index represent elder of cow: 0 1 2 3 and +
        a = [[0 for j in range(5)] for i in range(n + 1)]
        a[1][0] = 1
        a[1][4] = 1
        for i in range(2, n + 1):
            a[i][1:4] = a[i - 1][0:3]
            a[i][4] = a[i - 1][4] + a[i - 1][3]
            a[i][0] = a[i][4]
        return sum(a[-1][:])


def main():
    print(f"{CowNum(1)}")
    print(f"{CowNum(2)}")
    print(f"{CowNum(3)}")
    print(f"{CowNum(8)}")
    print(f"{CowNum(9)}")


if __name__ == "__main__":
    main()
