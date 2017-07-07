public class Solution 
{
    public int maxProfit(int[] prices) 
    {
        if(prices == null || prices.length < 2)
            return 0;
        int max = 0, currMax = 0;
        for(int i = 1; i < prices.length; i++)
        {
            currMax = Math.max((prices[i] - prices[i - 1]), (prices[i] - prices[i - 1] + currMax));
            max = Math.max(currMax, max);
        }
        return max;
    }
}