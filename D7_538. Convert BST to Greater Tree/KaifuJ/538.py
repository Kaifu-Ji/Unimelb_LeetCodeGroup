# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.presum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.post_order(root)
        return root

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.right)
        root.val += self.presum
        self.presum = root.val
        self.post_order(root.left)
