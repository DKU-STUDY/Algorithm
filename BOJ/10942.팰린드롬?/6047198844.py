import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# True 인 경우 펠린드롬이다.
memo = [[False for _ in range(N)] for _ in range(N)]
# 팰린드롬을 만들자.
# 기저는 2개가 존재.
# 구간의 길이가 1일때 -> 무조건 True
# 구간의 길이가 2일때 -> 둘이 같으면 True

for k in range(2):
    for i in range(N - k):
        j = i + k
        memo[i][j] = numbers[i] == numbers[j]

# 구간이 3이상일때
# 3은 기저가 1이고, 4는 기저가 2이다.
# 5는 3, 6은 4 ... 따라서 구간 1, 구간 2이 기저가된다.
# 구간의 길이는 3에서 N - 1 이다.
for k in range(2, N):
    for i in range(N - k):
        j = i + k
        if memo[i + 1][j - 1] and numbers[i] == numbers[j]:
            memo[i][j] = True

for _ in range(M):
    S, E = map(lambda i: int(i) - 1, sys.stdin.readline().split())
    print(int(memo[S][E]))
