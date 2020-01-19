#!/usr/bin/env python3
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def RotateLinkList(self, head, num):
        print("For solving rotating linkedlist")
        if num <= 0 or head == None or head.next == None:
            return head
        pre = None
        cur = head
        next = head.next
        while num > 0 and cur != None:
            num = num - 1
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = self.reverseList(cur)
        return pre


def main():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    Solve = Solution()
    # print(Solve.reverseList(a))
    head = Solve.RotateLinkList(a, 4)
    while head != None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    main()