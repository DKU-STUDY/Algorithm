# 문제
# 행복이는 길이가 N인 수열 A에서 소수들을 골라 최소공배수를 구해보려고 한다.
#
# 행복이를 도와 이를 계산해주자.
#
# 입력
# 첫째 줄에 수열 A의 길이 N이 주어진다. 1 <= N <= 10,000
#
# 그 다음줄에는 수열 A의 원소 A_i가 공백으로 구분되어 주어진다. $(2 <= A_{i} <= 1,000,000
#
# 답이 2^63 미만인 입력만 주어진다.
#
# 출력
# 첫째 줄에 소수들의 최소공배수를 출력한다.
#
# 만약 소수가 없는 경우는 -1을 출력한다.


prime = [True for _ in range(1000000 + 1)]
for i in range(2, 1000 + 1):
    if prime[i]:
        for j in range(i + i, 1000000 + 1, i):
            prime[j] = False

N = int(input())
A = list(set(map(int, input().split())))
res = 1
for i in A:
    if prime[i]:
        res *= i

print(-1) if res == 1 else print(res)


