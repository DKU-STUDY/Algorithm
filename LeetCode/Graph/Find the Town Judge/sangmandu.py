'''
https://leetcode.com/problems/find-the-town-judge/
기본적인 그래프 문제이지만 그래프 개념은 없는 듯
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        g1 = set()
        g2 = []
        for a, b in trust:
            g1.add(a)
            g2.append(b)
        g1 = set(range(1, N+1)) - g1
        if len(g1) != 1:
            return -1
        ret = list(g1)[0]
        return ret if g2.count(ret) == N-1 else -1

'''
'''