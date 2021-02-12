'''
https://leetcode.com/problems/climbing-stairs/
DP : 피보나치 이용
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(1, n):
            a, b = b, a+b
        return a

'''
'''