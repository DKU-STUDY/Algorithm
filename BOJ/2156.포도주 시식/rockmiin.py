
n= int(input())
wine=[0]
dp=[0 for _ in range((n+1))]
for i in range(n):
    wine.append(int(input()))
# print(wine)

for i in range(1, n+1):
    if i<3: dp[i]= sum(wine[:i+1]); continue
    dp[i]= max(dp[i-1], dp[i-2]+ wine[i], dp[i-3]+ wine[i-1]+ wine[i])

print(dp[-1])
