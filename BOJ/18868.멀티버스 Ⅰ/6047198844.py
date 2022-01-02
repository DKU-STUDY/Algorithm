# 문제
# M개의 우주가 있고, 각 우주에는 1부터 N까지 번호가 매겨진 행성이 N개 있다.
# 행성의 크기를 알고 있을때, 균등한 우주의 쌍이 몇 개인지 구해보려고 한다. 구성이 같은데 순서만 다른 우주의 쌍은 한 번만 센다. (조합)
#
# 두 우주 A와 B가 있고, 우주 A에 있는 행성의 크기는 A1, A2, ..., AN, 우주 B에 있는 행성의 크기는 B1, B2, ..., BN라고 하자.
# 두 우주의 행성 크기가 모든 1 ≤ i, j ≤ N에 대해서 아래와 같은 조건을 만족한다면, 두 우주를 균등하다고 한다.
#
# Ai < Aj → Bi < Bj
# Ai = Aj → Bi = Bj
# Ai > Aj → Bi > Bj
# 입력
# 첫째 줄에 우주의 개수 M과 각 우주에 있는 행성의 개수 N이 주어진다. 둘째 줄부터 M개의 줄에 공백으로 구분된 행성의 크기가 한 줄에 하나씩 1번 우주부터 차례대로 주어진다.
#
# 출력
# 첫째 줄에 균등한 우주의 쌍의 개수를 출력한다.
#
# 제한
# 2 ≤ M ≤ 10
# 3 ≤ N ≤ 100
# 1 ≤ 행성의 크기 ≤ 10,000
from itertools import combinations


# 균등한지 판단하는 함수
def is_equal(a_mar, b_mar, n):
    for i, j in combinations(range(n), 2):
        if a_mar[i] < a_mar[j] and b_mar[i] < b_mar[j]:
            pass
        elif a_mar[i] == a_mar[j] and b_mar[i] == b_mar[j]:
            pass
        elif a_mar[i] > a_mar[j] and b_mar[i] > b_mar[j]:
            pass
        else:
            return 0
    else:
        return 1


M, N = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(M)]
res = 0
for i, j in combinations(range(M), 2):
    res += is_equal(mars[i], mars[j], N)
print(res)
