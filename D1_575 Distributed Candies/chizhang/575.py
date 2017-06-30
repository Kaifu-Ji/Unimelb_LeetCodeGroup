class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        distinct_candies = set()
        candies_len = len(candies)
        for i in candies:
            distinct_candies.add(i)
        distinct_candies_len = len(distinct_candies)
        if distinct_candies_len > candies_len / 2:
            return candies_len / 2
        else:
            return distinct_candies_len
