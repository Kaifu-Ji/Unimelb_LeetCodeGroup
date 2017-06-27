# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        if not root:
            return 0
        ans = 0
        if root.left and (not root.left.left) and (not root.left.right):
            ans = root.left.val
        else:
            ans = self.sumOfLeftLeaves(root.left)
        return ans + self.sumOfLeftLeaves(root.right)
