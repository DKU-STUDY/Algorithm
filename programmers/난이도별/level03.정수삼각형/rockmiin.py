def solution(triangle):
    dp=[[0]* i for i in range(1, len(triangle)+1)]
    for i in range(0, len(triangle)):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            elif j>=1:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
    return max(dp[len(triangle)-1])

print(
    solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])==30
)
