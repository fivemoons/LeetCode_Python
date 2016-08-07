# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder, inl=0, inr=None, postl=0, postr=None):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inr   = inr   if inr!=None  else len(inorder) - 1
        postr = postr if postr!=None else len(postorder) - 1
        if (inr - inl) < 0 or (postr - postl) < 0:
            return None
        else:
            idx = inorder.index(postorder[postr])
            root = TreeNode(postorder[postr])
            root.left  = self.buildTree(inorder, postorder, inl, idx-1, postl, idx-inl+postl-1)
            root.right = self.buildTree(inorder, postorder, idx+1, inr, idx-inl+postl, postr-1)
            return root