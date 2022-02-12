# 문제
# N(2 ≤ N ≤ 50)개의 그림이 있다. 각각의 그림은 5×7의 크기이고, 두 가지 색으로 되어 있다.
# 이때 두 가지의 색을 각각 ‘X’와 ‘.’으로 표현하기로 하자.
# 이러한 그림들이 주어졌을 때, 가장 비슷한 두 개의 그림을 찾아내는 프로그램을 작성하시오.
# 두 개의 그림에서 다른 칸의 개수가 가장 적을 때, 두 개의 그림이 가장 비슷하다고 하자.
#
# 입력
# 첫째 줄에 N이 주어진다. 다음 5×N개의 줄에 7개의 문자로 각각의 그림이 주어진다.
#
# 출력
# 첫째 줄에 가장 비슷한 두 그림의 번호를 출력한다. 그림의 번호는 입력되는 순서대로 1, 2, …, N이다. 번호를 출력할 때에는 작은 것을 먼저 출력한다. 입력은 항상 답이 한 가지인 경우만 주어진다.

# N 입력
import sys
from itertools import combinations

N = int(sys.stdin.readline())

pictures = list()
# 그림 입력
for i in range(N):
    picture = list()
    for j in range(5):
        picture.append(sys.stdin.readline().rstrip())
    pictures.append(picture)

res_dif = 36
res_combination = tuple()


# 조합 차이 계산
def picture_dif(i, j):
    picture_a, picture_b = pictures[i], pictures[j]
    diff = 0
    for y in range(5):
        for x in range(7):
            diff += int(picture_a[y][x] != picture_b[y][x])
    return diff


# 조합
for i, j in combinations(range(N), 2):
    # 둘의 차이 계산
    dif = picture_dif(i, j)
    if res_dif > dif:
        res_combination = (i+1, j+1)
        res_dif = dif

print(res_combination[0], res_combination[1])
