# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) >= 0
    def height(self, root):
        if root is None: return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left >= 0 and right >= 0 and abs(left - right)<=1:
            return max(left, right) + 1
        else:
            return -1
