'''
https://leetcode.com/problems/all-paths-from-source-to-target/
그래프 : DFS 방식
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        size = len(graph)
        ans = []
        while stack:
            path = stack.pop(0)
            if path[-1] == size - 1:
                ans.append(path)
                continue
            for node in graph[path[-1]]:
                stack.append(path + [node])

        return ans

'''
'''