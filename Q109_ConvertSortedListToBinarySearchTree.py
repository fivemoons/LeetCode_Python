# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        len = 0
        while p:
            p = p.next
            len += 1
        self.preHead = head
        return self.sortedListToBST2(0,len-1)
    def sortedListToBST2(self, st, ed):
        if (st > ed): return None
        md = st + (ed-st)/2
        p = TreeNode(0)
        p.left = self.sortedListToBST2(st, md-1)
        p.val = self.preHead.val
        self.preHead = self.preHead.next
        p.right = self.sortedListToBST2(md+1, ed)
        return p
        
        