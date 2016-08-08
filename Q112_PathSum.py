# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        ro = (root.val == sum and root.left is None and root.right is None)
        le = (self.hasPathSum(root.left, sum - root.val) and root.left != None)
        ri = (self.hasPathSum(root.right, sum - root.val) and root.right != None)
        return ro or le or ri
        