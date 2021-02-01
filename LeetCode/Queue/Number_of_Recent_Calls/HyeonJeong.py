class RecentCounter:
# 최근 3000밀리 초 이내에 요청된 개수를 계산하는 클래스
    def __init__(self):
        self.time = []
        self.t = 0

    def ping(self, t: int) -> int:
        newTime = []
        for i in self.time:
            if t-3000 <= i <= t:
                newTime += [i]
        newTime += [t]
        self.time = newTime
        if t == 0:
            return null
        return len(newTime)
