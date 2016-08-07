# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.traversal(root, ans, 0)
        return ans
    def traversal(self, root, ans, level):
    	if not root: return
    	if level == len(ans):
    		ans.append([])
    	if level % 2 == 0:
    		ans[level].append(root.val)
    	else:
    		ans[level].insert(0, root.val)
    	self.traversal(root.left,  ans, level+1)
    	self.traversal(root.right, ans, level+1)