class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = deque(s)
        for _ in range(len(s)-1):
            tmp = ''.join(s)
            if tmp == goal:
                return True
            s.rotate(1)
        return False