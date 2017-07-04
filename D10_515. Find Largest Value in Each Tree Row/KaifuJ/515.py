# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.level_visit([root],res)
        return res
    def level_visit(self,cur,res):
        next_nodes = []
        max_value = float("-inf")
        count = 0
        for node in cur:
            if node:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
                if max_value < node.val:
                    max_value = node.val
                count += 1
        if count:
            res.append(max_value)
            self.level_visit(next_nodes,res)
        return

a = Solution()
b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.left = TreeNode(4)
b.right.left = TreeNode(5)
a.largestValues(b)