# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ansNode = [[], [root]]
        while True:
            for node in ansNode[1]:
                if node.left:  ansNode[0].append(node.left)
                if node.right: ansNode[0].append(node.right)
            if ansNode[0]:
                ansNode.insert(0, [])
            else:
                del ansNode[0]
                break
        ans = []
        for level in ansNode:
            ans.append([])
            for node in level:
                ans[-1].append(node.val)
        return ans