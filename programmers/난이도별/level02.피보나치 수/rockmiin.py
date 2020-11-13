def solution(n):
    # A(n)= A(n-1)+A(n-2)
    dp=[0, 1]
    for i in range(2, n+1):
        dp.append((dp[i-1]+dp[i-2])%1234567)
    return dp[-1]

print(
    solution(5)==5
)
