

n = int(input())

dp = [[0 for i in range(10)]for _ in range(0,n+1)]

for i in range(0,n+1):
    for j in range(10):
        if(i==1):
            dp[i][j] =1
        else:
            for k in range(10):
                if(k<=j):
                    dp[i][j] = dp[i-1][j-k]+dp[i][j]

print(sum(dp[n][0:10])%10007)
