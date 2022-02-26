# 개요
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
# 산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
#
# 입력
# 전체 용액의 수 N이 입력된다. 2 <= N <= 100,000 이하의 정수이다.
# 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 오름차순으로 입력 -1,000,000,000 <= i <= 1,000,000,000
# N개의 용액들의 특성값은 모두 서로 다르다
#
# 출력
# 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다.
# 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다.
# 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.
import math
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
begin, end = 0, N - 1
rb, red = begin, end

target = 0
diff = math.inf
while begin < end:
    s = arr[begin] + arr[end]
    if abs(s) < diff:
        rb, re = begin, end
        diff = abs(s)

    if s < target:
        begin += 1
    else:
        end -= 1
print(arr[rb], arr[re])