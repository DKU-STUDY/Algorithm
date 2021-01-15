'''
https://leetcode.com/problems/all-paths-from-source-to-target/
그래프 : 목적지만 제거. set 이용
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        st, ed = list(zip(*edges))
        return list(set(range(n)) - set(ed))

'''
'''