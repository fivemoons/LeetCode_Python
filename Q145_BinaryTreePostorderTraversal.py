# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], []
        p = root
        last = None
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                if not stack[-1].right or stack[-1].right == last:
                    last = stack.pop()
                    ans.append(last.val)
                else:
                    p = stack[-1].right
        return ans
