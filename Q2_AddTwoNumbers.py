# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        p = ans
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + p.val / 10)
            p.val = p.val % 10
            p, l1, l2 = p.next, l1.next, l2.next
        while l1:
            p.next = ListNode(l1.val + p.val / 10)
            p.val = p.val % 10
            p, l1 = p.next, l1.next
        while l2:
            p.next = ListNode(l2.val + p.val / 10)
            p.val = p.val % 10
            p, l2 = p.next, l2.next
        if (p.val / 10 > 0):
            p.next = ListNode(p.val / 10)
            p.val = p.val % 10
            p = p.next
        return ans.next