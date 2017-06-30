# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
count = collections.Counter()
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        output = []
        try:
            max_value = count.most_common(1)
            for i in count:
                if count[i] == max_value[0][1]:
                    output.append(i)
            return output
        except:
            return output
        
    def dfs(self,root):
        if root == None:
            pass
        elif root.left == None and root.right == None:
            if root.val in count:
                count[root.val] += 1
            else:
                count[root.val] = 1
        else:
            if root.val in count:
                count[root.val] += 1
            else:
                count[root.val] = 1
            self.dfs(root.left)
            self.dfs(root.right)
           
