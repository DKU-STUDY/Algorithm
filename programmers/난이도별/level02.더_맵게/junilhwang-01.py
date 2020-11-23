# https://programmers.co.kr/learn/courses/30/lessons/42626
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def solution(s, K):
    h = []
    for v in s : insert(h, v)
    if h[0] >= K : return 0
    for i in range(1, len(h)) :
        insert(h, delete(h) + delete(h) * 2)
        if h[0] >= K : return i
    return -1

def insert (h, n) :
    i = len(h)
    h.append(n)
    while i > 0 and n < h[int(i/2)] : h[i], i = h[int(i/2)], int(i/2)
    h[i] = n
    
def delete (h) :
    n, h[0] = h[0], h[-1]
    hlen = len(h)
    i = 0
    while i * 2 + 1 < hlen :
        next = i * 2 if i != 0 else 1
        if next + 1 < hlen and h[next] > h[next + 1] : next += 1
        h[next], h[i], i = h[i], h[next], next
    del h[-1]
    return n

print(solution([1, 2, 3, 9, 10, 12], 100))
print(solution([1, 2], 7))
print(solution([1], 2))
print(solution([5], 5))
print(solution([1,2,7], 5))
print(solution([2,3,7], 7))
print(solution([0], 0))