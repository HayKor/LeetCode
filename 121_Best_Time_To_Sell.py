class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        res = 0
        for num in prices[1:]:
            if num < buy:
                buy = num
            res = max(res, num - buy)
        return res


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
prices = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))
