# 문제
# 아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)
#
# 입력
# 총 아홉개 줄에 1보다 크거나 같고 99보다 작거나 같은 자연수가 주어진다. 모든 숫자는 서로 다르다. 또, 항상 답이 유일한 경우만 입력으로 주어진다.
#
# 출력
# 일곱 난쟁이가 쓴 모자에 쓰여 있는 수를 한 줄에 하나씩 출력한다.
from itertools import combinations

dwalfs = [int(input()) for _ in range(9)]
for combi in combinations(dwalfs, 7):
    if sum(combi) == 100:
        for dwalf in combi:
            print(dwalf)
        break
