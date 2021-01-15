'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
기본적인 dp 문제인데 아직 분할 개념은 없는 듯
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = ret = 0
        for p in prices[::-1]:
            m = max(m, p)
            ret = max(m-p, ret)
        return ret



'''
'''