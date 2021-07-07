'''
https://programmers.co.kr/learn/courses/30/lessons/12938
징검다리 건너기
[풀이]
0. 이진탐색 문제
=> 하지만 이진탐색문제인지 몰랐다. 한참을 고민해도 몰랐음. 결국 참고.
1. 건너뛰어야 하는 돌의 개수가 k개 이하
=> n명이 이미 지나갔고, 돌에 적혀있는 수가 n이하
=> n이하의 수를 가진 돌이 연속적으로 k개 이하로 두어져 있어야 함
2. 이 n을 이진탐색으로 1 to max(stones) 범위에서 찾는다.
=> mid는 둘의 사이
=> dist는 mid보다 작은 수를 지닌 연속적으로 이어지는 돌의 개수
=> answer은 기본 1 (돌다리가 최소 하나이므로 하나는 무조건 건널 수 있음)
3. for-else continue를 이용해서 break시에 두 가지 흐름도를 설정
'''
def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        dist = 0
        for stone in stones:
            if stone < mid:
                dist += 1
            else:
                dist = 0
            if dist == k:
                break
        else:
            answer = max(answer, mid)
            left = mid + 1
            continue
        right = mid - 1

    return answer
'''
'''