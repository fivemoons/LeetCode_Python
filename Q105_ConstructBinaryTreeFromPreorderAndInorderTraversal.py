# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder, prel=0, prer=None, inl=0, inr=None):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        prer = prer if prer!=None else len(preorder) - 1
        inr  = inr  if inr!=None  else len(inorder) - 1
        if (prer - prel) < 0 or (inr - inl) < 0:
            return None
        else:
            idx = inorder.index(preorder[prel])
            root = TreeNode(preorder[prel])
            root.left  = self.buildTree(preorder, inorder, prel+1, idx-inl+prel, inl, idx-1)
            root.right = self.buildTree(preorder, inorder, idx-inl+prel+1, prer, idx+1, inr)
            return root