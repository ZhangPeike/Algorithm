# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        num = []
        while head != None:
            num.append(head.val)
            head = head.next
        n = len(num)
        if n == 1:
            return True
        else:
            for i in range(n // 2):
                if num[i] != num[-(i + 1)]:
                    return False
        return True


def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    Solve = Solution()
    print(Solve.isPalindrome(a))


if __name__ == "__main__":
    main()
