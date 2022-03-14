# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
#
# 둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.
import bisect

N = int(input())
arr = list(map(int, input().split()))

memo = []
increase_arr = []
for i in arr:
    idx = bisect.bisect_left(increase_arr, i)
    if idx == len(increase_arr):
        increase_arr.append(i)
    else:
        increase_arr[idx] = i
    memo.append(idx)
print(len(increase_arr))

res = []
p = len(increase_arr) - 1
for idx, i in enumerate(memo[::-1]):
    if i == p:
        res.append(arr[- 1 - idx])
        p -= 1
for i in res[::-1]:
    print(i, end = ' ')
