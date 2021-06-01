'''
https://programmers.co.kr/learn/courses/30/lessons/72412
순위 검색
dictionary 고급 문제
'''
from itertools import product
from bisect import bisect_left as bisl

def solution(info, query):
    dic = {}
    for words in info:
        words = words.split()
        words, score = words[:-1], int(words[-1])
        for word in product(*zip(words, '-' * 4)):
            key = ''.join(word)
            dic.setdefault(key, [])
            dic[''.join(word)].append(score)

    for key in dic.keys():
        dic[key].sort()

    answer = []
    for q in query:
        q = q.replace('and ', '').split()
        q, score = ''.join(q[:-1]), int(q[-1])
        arr = dic.get(q)
        if arr == None:
            answer.append(0)
        else:
            answer.append(len(arr) - bisl(arr, score))

    return answer
'''
이건 미친 문제이다. 설마 이거야? 했던 풀이방법으로 풀어야 되는 문제.
정답률이 5%에 안되는 문제인데 level02 에 존재하면 안된다.
실제 시험볼 때도 못풀었다 ㅠ 지금도 못풀어서 카카오 공식 풀이 보다가
dictionary로 풀으라길래 푼 문제..

미친 풀이가 있는데, 각 매칭을 비트 연산자 방식으로 생각한 것이 독특하다.
심지어 코드도 간결

from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]
'''