/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const nodes = [];

const explore = (node) => {
    if (!node) return;
    
    explore(node.left);
    nodes.push(node.val);
    explore(node.right);
};

const getMode = (nodes) => {
    if (!nodes || !nodes.length) return [];
    
    let max = 0;
    let maxKey = [];
    let currStreak = 0;
    
    const isEndOfStreak = (i) => {
        return i >= nodes.length - 1 || nodes[i] !== nodes[i+1];
    };
    
    for (let i = 0; i < nodes.length; i++) {
        currStreak += 1;
        if (isEndOfStreak(i)) {
            if (currStreak > max) {
                max = currStreak;
                maxKey = [nodes[i]];
            } else if (currStreak === max) {
                maxKey.push(nodes[i]);
            }
            
            currStreak = 1;
        }
    }
    
    return maxKey;
}

var findMode = function(root) {
    explore(root);
    return getMode(nodes);
};
