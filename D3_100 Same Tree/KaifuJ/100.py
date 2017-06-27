# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left,q.left) and self.isSameTree(q.right,p.right)
        else:
            return False