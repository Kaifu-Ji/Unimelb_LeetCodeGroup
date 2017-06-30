# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root, dirc = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif dirc == 1 and root.left == None and root.right == None:
            return root.val
        elif dirc == 0 and root.left == None and root.right == None:
            return 0
        else:
            sum = 0
            sum += self.sumOfLeftLeaves(root.left,1)
            sum += self.sumOfLeftLeaves(root.right,0)
            return sum
