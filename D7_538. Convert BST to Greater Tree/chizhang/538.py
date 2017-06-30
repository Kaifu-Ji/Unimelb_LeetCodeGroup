# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node_list, node_value = self.searchBST(root)
        for i in range(len(node_value)):
            node_value[i] += sum(node_value[i+1:])
        for i in range(len(node_list)):
            node_list[i].val = node_value[i]
        return root
        
    def searchBST(self, root):
        if root is None:
            return [],[]
        elif root.left == None and root.right == None:
            return [root],[root.val]
        elif root.left != None and root.right == None:
            node, node_value = self.searchBST(root.left)
            return node + [root], node_value + [root.val]
        elif root.left == None and root.right != None:
            node, node_value = self.searchBST(root.right)
            return [root] + node, [root.val] + node_value
        else:
            node1, node_value1 = self.searchBST(root.left)
            node2, node_value2 = self.searchBST(root.right)
            return node1 + [root] + node2, node_value1 + [root.val] + node_value2
                
