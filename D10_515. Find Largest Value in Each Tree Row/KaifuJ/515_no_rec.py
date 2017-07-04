# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = [root]
        res = []
        while any(cur):
            res.append(max([node.val for node in cur]))
            cur = [kid for node in cur for kid in (node.left, node.right) if kid]
        return res