

n= int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]= [0]+[1]*9

for i in range(1, n+1):
    for j in range(1, 9):
        dp[i][j]+= (dp[i-1][j-1]+ dp[i-1][j+1])
    dp[i][0]+= dp[i-1][1]
    dp[i][9]+= dp[i-1][8]

print(sum(dp[-1])%1000000000)
