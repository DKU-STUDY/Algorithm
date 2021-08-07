import heapq


def solution(a):
    answer_balloon = set()

    left_heap = []
    right_heap = []

    # left_heap / right_heap은 왼쪽 / 오른쪽에서 최후까지 남아있는 풍선을 뜻한다.
    # 풍선은 왼쪽이나 오른쪽의 최후의 풍선중 하나라도 자신보다 크다면 무조건 마지막까지 살아남을수있다.
    # EX) 왼쪽 최후가 크고 오른쪽 최후가 작은 경우. 왼쪽 최후 터트리고 오른쪽 최후는 찬스 이용 오른쪽을 터트릴수있음.
    # 답을 answer_balloon에 넣는다.
    for idx in range(len(a)):
        left_balloon = a[idx]
        heapq.heappush(left_heap, left_balloon)
        if left_heap[0] >= left_balloon:
            answer_balloon.add(left_balloon)

        right_balloon = a[-1 - idx]
        heapq.heappush(right_heap, right_balloon)
        if right_heap[0] >= right_balloon:
            answer_balloon.add(right_balloon)

    return len(answer_balloon)