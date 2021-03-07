'''
https://school.programmers.co.kr/courses/11117/lessons/71020
배달
기본적인 그래프 문제.
'''

from queue import PriorityQueue
def solution(N, road, K):
    pq = PriorityQueue()
    pq.put([1, 0])

    dist = [500001] * (N + 1)
    dist[1] = 0

    while not pq.empty():
        current, current_cost = pq.get()
        for src, dest, cost in road:
            next_cost = cost + current_cost
            if src == current and next_cost < dist[dest]:
                dist[dest] = next_cost
                pq.put([dest, next_cost])
            elif dest == current and next_cost < dist[src]:
                dist[src] = next_cost
                pq.put([src, next_cost])
    return len([x for x in dist if x <= K])

'''
'''