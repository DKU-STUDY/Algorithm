class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - min_price
            if tmp > res:
                res = tmp
            if min_price > prices[i]:
                min_price = prices[i]
        
        return res
#100000 = 십만
#10000 = 만

#브루트 포스로 풀면안된다.