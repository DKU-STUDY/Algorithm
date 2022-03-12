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

arr = list(input())
N = len(arr)
is_palindrome = [[False for _ in range(N + 1)] for _ in range(N + 1)]

# 크기 1일때 -> 항상 true
for i in range(1, N+1):
    is_palindrome[i][i] = True

# 크기 2일때 -> 같으면 true
for i in range(N):
    is_palindrome[i][i+1] = arr[i] == arr[i+1]

# 크기 3일때 ~ 크기 N
for k in range(2, N):
    for i in range(N-k):
        if arr[i] == arr[i+k]:
            is_palindrome[i][i+k] = is_palindrome[i+1][i+k-1]

memo = [math.inf for _ in range(N+1)]
memo[1] = 1

for end in range(1, N):
    for begin in range(1, end + 1):
        if is_palindrome[begin][end]:
            memo[end+1] = min(memo[end + 1], memo[end] + 1)
print(memo[N])






for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    if a[i-1] == a[i]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(1, n+1-i):
        if a[j-1] == a[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, n+1):
    result[i] = min(result[i], result[i-1] + 1)
# result[i-1]+1인 이유는 result[i-1]까지의 팰린드롭에 j부터 i까지의 팰린드롭 한개를 더하는 것이기 때문이다
    for j in range(i+1, n+1):
        if dp[i][j] != 0:
          # 팰린드롭이면
            result[j] = min(result[j], result[i-1] + 1)

print(result[n])
