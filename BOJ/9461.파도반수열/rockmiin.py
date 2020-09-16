
test_case=int(input())
for i in range(test_case):
    n=int(input())
    dp=[1, 1, 1, 2, 2]
    if n>5:
        for i in range(n-5):
            dp.append(dp[-1]+dp[-5])
        print(dp[-1])
    else: print(dp[n-1])