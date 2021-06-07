'''
https://programmers.co.kr/learn/courses/30/lessons/43238
입국심사
[풀이]
1. 사람이 10억명. 따라서 O(N) 이하의 시간복잡도를 가져야 한다
2. 시간을 1초부터 세지 말고 최대 걸리는 시간의 범위에서 이진탐색 실행
=> 최대 시간은 max(times) * n => 심사를 오래하는 사람에게 모두 심사를 받는 경우
'''
def solution(n, times):
    low = 0
    high = max(times) * n

    while low < high:
        mid = (low + high) // 2
        sum = 0
        for t in times:
            sum += (mid // t)

        if sum < n:
            low = mid + 1
        else:
            high = mid

    return low


'''
'''