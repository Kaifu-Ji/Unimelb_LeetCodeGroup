/**
 * @param {number[]} candies
 * @return {number}
 */

var distributeCandies = function(candies) {
    const limit = candies.length / 2;
    const s = new Set(candies);
       
    return s.size > limit ? limit : s.size;
}
