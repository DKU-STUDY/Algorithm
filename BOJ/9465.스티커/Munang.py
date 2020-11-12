## dp 문제 

t = int(input())

for i in range(t):
    n = int(input())
    dp =[]
    memo =[]
    for j in range(2):
        score = list(map(int,input().split()))
        dp.append(score)
        memo.append([0]*n)
## 0이 아닐경우 출력이라는걸 구현해야함
    for k in range(n):
        if(k ==0):
            memo[0][k] = dp[0][k]
            memo[1][k] = dp[1][k]
        if(k ==1):
            memo[1][1] = dp[0][0] + dp[1][1]
            memo[0][1] = dp[1][0] + dp[0][1]

        memo[0][k] = max(memo[1][k-1], memo[1][k-2]) + dp[0][k]
        memo[1][k] = max(memo[0][k-1], memo[0][k-2]) + dp[1][k]

    print(max(memo[0][n-1],memo[1][n-1]))