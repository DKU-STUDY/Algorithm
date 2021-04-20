
n= int(input())
p= [0] + list(map(int, input().split()))
dp= [0 for _ in range(n+1)]
dp[1]= p[1]
for i in range(1, n+1):
    for j in range(1, i+1):
        # print(i, j, dp)
        dp[i]= max(dp[i], dp[i-j]+ p[j])

print(dp[-1])