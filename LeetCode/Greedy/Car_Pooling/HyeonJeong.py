class Solution(object):
    def carPooling(self, trips, capacity):
    # 모든 여행에서 모든 승객을 태우고 내릴 수 있는지를 확인하는 문제
        for trip in range(min([x[1] for x in trips]), max([x[2] for x in trips])+1):
            people = 0
            for num, start, end in trips:
                if start <= trip < end:
                    people += num
                if people > capacity:
                    return False
        return True
