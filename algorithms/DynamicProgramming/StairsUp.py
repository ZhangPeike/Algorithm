class Stairs():
    def __init__(self):
        print(f"")

    def Recursive(self, n):
        if n <= 2:
            return n
        return self.Recursive(n - 1) + self.Recursive(n - 2) * 2

    def DP(self, n):
        c = [-float('inf') for i in range(max(3, n + 1))]
        c[0] = 0
        c[1] = 1
        c[2] = 2
        return self.DPAux(n, c)

    def DPAux(self, n, c):
        if c[n] > 0:
            return c[n]
        c[n] = self.DPAux(n - 1, c) + 2 * self.DPAux(n - 2, c)
        return c[n]


def main():
    UpStairs = Stairs()
    for i in range(1, 100):
        # print(f"{i} stairs have {UpStairs.Recursive(i)} method")
        print(f"{i} stairs have {UpStairs.DP(i)} method")


if __name__ == "__main__":
    main()
