from collections import deque

class MyCircularDeque:
# 순환 양방향 큐 구현을 설계
    def __init__(self, k: int):
        self.q = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[len(self.q)-1]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.q) == self.k:
            return True
        return False
