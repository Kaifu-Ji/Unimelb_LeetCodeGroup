class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        currMax = 0
        res = 0
        for i in xrange(1, len(prices)):
            currMax = max((prices[i] - prices[i - 1]), (prices[i] - prices[i - 1] + currMax))
            res = max(currMax, res)
        return res