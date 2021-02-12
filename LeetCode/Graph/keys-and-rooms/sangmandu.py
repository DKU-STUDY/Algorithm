'''
https://leetcode.com/problems/keys-and-rooms/
GRAPH
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        stack = [0]
        while stack:
            key = stack.pop()
            if not visited[key]:
                visited[key] = 1
                for room in rooms[key]:
                    stack.append(room)
        return visited.count(1) == n

'''
'''