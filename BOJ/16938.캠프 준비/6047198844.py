'''
입력
N, L, R, X
A1, A2, ... , An

N : 개수
L <= 난이도의합 <= R
X : 난이도 차이 (가장 어려운 문제 - 가장 쉬운 문제)
'''

from itertools import combinations

N, L, R, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
result = 0

for i in range(1, N + 1):
    for c in combinations(A, i):
        if L <= sum(c) <= R and c[-1] - c[0] >= X:
            result += 1

print(result)
