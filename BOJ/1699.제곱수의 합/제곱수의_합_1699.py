n=int(input())
dp=[0]*(n+1)
s=[]
dp[1]=1
for i in range(1, 400):
    if i**2 >= 100000: break
    s.append(i)
for i in range(1, n+1):
    q=[]
    for j in s:
        if i>=j**2:
            q.append(dp[i-j**2])
        else: break;
    dp[i]=min(q)+1
print(dp[n])
