'''
https://programmers.co.kr/learn/courses/30/lessons/17680
캐시
CS지식이 적용된 문제라 순간 놀랐다. Cache를 모르는 사람은 풀기 어려웠을 듯...
'''

def solution(cacheSize, cities):
    if not cacheSize: return len(cities) * 5
    cache = []
    time = 0
    for i in cities:
        i = i.lower()
        if i in cache:
            time += 1
            cache.remove(i)
            cache.append(i)
            continue
        time += 5
        if len(cache) == cacheSize:
            cache.pop(0)
        cache.append(i)
    return time

'''
deque 에는 다음과 같은 maxlen 속성이 있다.
이 이상 append 되면 이전에 있던 data가 자동 pop
collections.deque(maxlen=cacheSize)
'''