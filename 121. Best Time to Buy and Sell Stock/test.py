class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)

        if l <= 1:
            return 0

        smaller = 0
        profit = 0
        for index in range(1, len(prices)):
            p = prices[index] - prices[smaller]
            if p >= profit:
                profit = p
            if prices[smaller] >= prices[index]:
                smaller = index
        return profit

assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0

