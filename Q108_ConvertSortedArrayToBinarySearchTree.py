# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        idx = (len(nums) - 1) / 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[0:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root