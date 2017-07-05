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
            tl = self.tree2str(t.left)
            tr = self.tree2str(t.right)
            if tr != "":
                return "{0}({1})({2})".format(t.val,tl,tr)
            if tr == "":
                if tl != "":
                    return "{0}({1})".format(t.val,tl)
                else:
                    return "{0}".format(t.val)

