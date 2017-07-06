# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        else:
            left = "({})".format(self.tree2str(t.left)) if t.left or t.right else ''
            right = "({})".format(self.tree2str(t.right)) if t.right else ''
            return str(t.val) + left + right
