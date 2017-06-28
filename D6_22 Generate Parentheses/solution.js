/**
 * @param {number} n
 * @return {string[]}
 */
const l = "(";
const r = ")";

const generate = (p, left, right, arr) => {
    if (left) generate(p+l, left-1, right, arr);
    if (right > left) generate(p+r, left, right-1, arr);
    if (!right) arr.push(p);
    return arr;
}
 
var generateParenthesis = function(n) {
    return generate("", n, n, [])
};
