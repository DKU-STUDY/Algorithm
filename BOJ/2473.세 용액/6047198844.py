# 문제
# 같은 양의 세 가지 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
# 이 연구소에서는 같은 양의 세 가지 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
# 참고로, 세 종류의 알칼리성 용액만으로나 혹은 세 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
# 산성 용액과 알칼리성 용액이 주어졌을 때, 이 중 같은 양의 세 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 세 용액을 찾는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 전체 용액의 수 N이 입력된다. N은 3 이상 5,000 이하의 정수이다.
# 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다.
# N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
import math
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
# O(N^2)
min_diff = math.inf
res = (arr[0], arr[1], arr[2])

for k in range(N):
    begin, end = 0, N - 1

    while begin < end:
        if k == begin:
            begin += 1
        if k == end:
            end -= 1
        if begin >= end:
            break

        s = arr[begin] + arr[end] + arr[k]
        if abs(s) < min_diff:
            res = (arr[begin], arr[end], arr[k])
            min_diff = abs(s)

        # target 만들기
        if s < 0:
            begin += 1
        else:
            end -= 1

for i in sorted(res):
    print(i, end=' ')
