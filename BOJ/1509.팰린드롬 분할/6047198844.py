# 문제
# 세준이는 어떤 문자열을 팰린드롬으로 분할하려고 한다. 예를 들어, ABACABA를 팰린드롬으로 분할하면, {A, B, A, C, A, B, A}, {A, BACAB, A}, {ABA, C, ABA}, {ABACABA}등이 있다.
#
# 분할의 개수의 최솟값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 문자열이 주어진다. 이 문자열은 알파벳 대문자로만 이루어져 있고, 최대 길이는 2,500이다.
#
# 출력
# 첫째 줄에 팰린드롬 분할의 개수의 최솟값을 출력한다.
import math

line = input()
n = len(line)

dp = [[0 for i in range(n + 1)]for j in range(n + 1)]
result = [math.inf] * (n+1)
result[0] = 0

for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    if line[i-1] == line[i]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(1, n+1-i):
        if line[j-1] == line[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, n+1):
    result[i] = min(result[i], result[i-1] + 1)
    for j in range(i+1, n+1):
        if dp[i][j] != 0:
            result[j] = min(result[j], result[i-1] + 1)

print(result[n])