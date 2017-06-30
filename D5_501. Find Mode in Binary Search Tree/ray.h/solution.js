/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const freq = {};

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

const find = function (root) {
    if (!root) return;
    const {val} = root;

    if (!freq[val]) {
        freq[val] = 1;
    } else {
        freq[val] = freq[val] + 1;
    }

    find(root.left);
    find(root.right);
}

const getMaxKey = function (obj) {
    let max = Number.MIN_SAFE_INTEGER;
    let maxKey = [];
    Object.entries(obj).forEach(entry => {
        if (entry[1] > max) {
            max = entry[1];
            maxKey = [entry[0]];
        } else if (entry[1] === max) {
            maxKey.push(entry[0]);
        }
    });

    return maxKey.map(key => +key);
}

var findMode = function (root) {
    find(root);
    return getMaxKey(freq);
};

a = new TreeNode(10);
findMode(a)
