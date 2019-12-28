class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        sp = s[::-1]
        for (x, y) in zip(s, sp):
            if x == y:
                continue
            else:
                return False
        return True

    def isPalindromeI(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        x_cp = x
        x_reverted = 0
        while x_cp > x_reverted:
            x_reverted = x_reverted * 10 + x_cp % 10
            x_cp = x_cp // 10
        return x_cp == x_reverted or (x_cp == x_reverted // 10)
