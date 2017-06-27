# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.cur_val = None
        self.cur_num = 0
        self.result = []
        self.max = 1

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorder(root)

    def inorder(self, root_node):
        if not root_node:
            return self.result
        self.inorder(root_node.left)
        if self.cur_val == root_node.val:
            self.cur_num += 1
            if self.cur_num == self.max:
                self.result.append(self.cur_val)
            elif self.cur_num > self.max:
                self.result = [self.cur_val]
                self.max = self.cur_num
        else:
            if self.max == 1:
                self.result.append(root_node.val)
            self.cur_num = 1
            self.cur_val = root_node.val
        self.inorder(root_node.right)
        return self.result

a = Solution()
b = TreeNode(1)
b.left = TreeNode(1)
b.right = TreeNode(2)
print(a.findMode(b))