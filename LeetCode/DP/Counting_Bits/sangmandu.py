'''
https://leetcode.com/problems/counting-bits/
Counting Bits
이진수 표현. format을 알면 쉽게 풀 수 있다
'''
class Solution(object):
    def countBits(self, n):
        return [format(i, 'b').count('1') for i in range(n + 1)]

'''
완벽하게 푼듯 하다
'''