'''
https://programmers.co.kr/learn/courses/30/lessons/70128
소수 찾기
[풀이]
1. 주어진 숫자로 만들 수 있는 모든 수에 대한 소수 판별
2. 조합 사용
'''
from itertools import permutations
def solution(numbers):
    num = list(set(map(int, sum([list(map(''.join, permutations(numbers, i))) for i in range(1, len(numbers)+1)], []))))
    answer = 0
    for n in num:
        if all([(n%i) for i in range(2, int(n**0.5)+1)] + [n > 1]): answer += 1
    return answer
'''
에라토스테네스 채를 사용하고 싶었는데, 마땅히 생각이 안났다
아래와 같이 풀이 가능
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''