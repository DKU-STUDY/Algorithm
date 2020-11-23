# 실패 -> 정답을 분석한 것

import heapq #이진트리 기반 최소 힙(원소가 항상 정렬된 상태에서 추가, 삭제) 자료구조 제공

def solution(s, K):
    a = 0 # 섞은 횟수가 추가될 변수
    heapq.heapify(s)
    if s[0] >= K : return 0 # 가장 작은 원소가 K이상이면 반환
    while len(s) > 1 :
        heapq.heappush(s, heapq.heappop(s) + heapq.heappop(s) * 2)
        # heappush()는 두 번째 인자를 첫 번째 인자인 리스트에 추가, O(logN)의 시간복잡도를 가짐
        # heappop()은 대상 리스트에서 가장 작은 원소 삭제후 값 리턴
        a += 1 # 섞은 횟수 추가
        if s[0] >= K : return a # 가장 작은 원소가 K이상이면 섞은 횟수 반환
    return -1 # 다 섞었는데도 K미만인 경우

print(solution([1, 2, 3, 9, 10, 12], 7) == 2)