from collections import deque

class RecentCounter:
# 최근 3000밀리 초 이내에 요청된 개수를 계산하는 클래스
    def __init__(self):
        self.time = deque()

    def ping(self, t: int) -> int:
        self.time.append(t) # 인덱스 0이 항상 존재하게 됨
        while t-3000 > self.time[0]:
            self.time.popleft() # 큐에서 처음 요소 제거
        if len(self.time) == 0:
            return null
        return len(self.time)
