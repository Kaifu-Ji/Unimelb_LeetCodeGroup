/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 
var sumOfLeftLeaves = function(root) {
    if (!root) {
        return 0;
    }
    else if (root.left && root.left.left === null && root.left.right === 
null) {
        return root.left.val + sumOfLeftLeaves(root.right);
    } else {
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    }
};
