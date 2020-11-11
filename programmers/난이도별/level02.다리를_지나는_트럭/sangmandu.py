'''
https://programmers.co.kr/learn/courses/30/lessons/42583
다리를 지나는 트럭 : 다리의 길이와 트럭의 무게 다리의 하중을 고려하여 모든 트럭이 지나는 시간 구하기
다리를 지나는 시간은 이전 트럭이 출발한 시점부터 자신이 출발한 시점까지의 대기 시간을 모두 합 + 다리 길이 + 1 이다.
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    b, w, t = bridge_length, weight, truck_weights
    time = deque([1])
    wsum = deque([t[0]])
    sec = 0
    for v, i in enumerate(t[1:]):
        if i <= weight - sum(wsum):
                time.append(1)
                wsum.append(i)
                if sum(time) - time[0] == b:
                    sec += time.popleft()
                    wsum.popleft()
                continue
        if i <= weight - sum(wsum) + wsum[0]:
            sec += time.popleft()
            wsum.popleft()
            time.append(b - sum(time))
            wsum.append(i)
            continue
        while i > weight - sum(wsum):
            sec += time.popleft()
            wsum.popleft()
        time.append(b - sum(time))
        wsum.append(i)
    return sum(time) + b


'''
100%의 모든 사람들이 1초에 대해서 반복문을 설정한데 비해
트럭의 순서에 대해서 반복문을 돌리려고 했음
=> 실제 1초에 대해서 구현한 대부분 코드는 1000.00ms가 넘는다.
=> 다음과 같이 0.1ms가 걸리지 않아 결과적으로 엄청나게 빠른 코드 생성
=> 실전에서 다음과 같이 풀었으면 스포트라이트를 받을 것 같다. 제한 시간 내에는 불가능 할 듯.

테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.40ms, 10.3MB)
테스트 5 〉	통과 (0.90ms, 10.3MB)
테스트 6 〉	통과 (0.79ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.48ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.07ms, 10.2MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
'''
