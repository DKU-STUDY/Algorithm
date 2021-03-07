'''
https://leetcode.com/problems/min-cost-climbing-stairs/
역으로 생각해서, 내가 이 계단과 저 계단 중 무얼 밞을 까 하는 단계
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for x in cost[::-1]:
            a, b = x + min(a, b), a
        return min(a, b)

'''
'''