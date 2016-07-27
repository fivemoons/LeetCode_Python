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
        car = 0
        while l1 and l2:
            p.next = ListNode(0)
            p = p.next
            p.val, car = (l1.val + l2.val + car) % 10, (l1.val + l2.val + car) / 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            p.next = ListNode(0)
            p = p.next
            p.val, car = (l1.val + car) % 10, (l1.val + car) / 10
            l1 = l1.next
        while l2:
            p.next = ListNode(0)
            p = p.next
            p.val, car = (l2.val + car) % 10, (l2.val + car) / 10
            l2 = l2.next
        if car != 0:
            p.next = ListNode(0)
            p = p.next
            p.val = car
        return ans.next