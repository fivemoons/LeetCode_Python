# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ansNode = [[root], []]
        while True:
            for node in ansNode[-2]:
                if node.left:  ansNode[-1].append(node.left)
                if node.right: ansNode[-1].append(node.right)
            if ansNode[-1]:
                ansNode.append([])
            else:
                ansNode.pop()
                break
        ans = []
        for level in ansNode:
            ans.append([])
            for node in level:
                ans[-1].append(node.val)
        return ans