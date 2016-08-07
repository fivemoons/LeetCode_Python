# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSame(root.left, root.right) if root else True
        