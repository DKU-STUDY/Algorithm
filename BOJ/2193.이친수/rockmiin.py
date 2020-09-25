
# n=int(input())
# arr=[[] for _ in range(n+1)]
# arr[1].append(1)
#
# for i in range(1, n):
#     for j in arr[i]:
#         j=str(j)
#         if j[-1]=='0':
#             arr[i+1].append((j+'0'))
#             arr[i+1].append(j+'1')
#         else: arr[i+1].append(j+'0')
# print(len(arr[n]))

n= int(input())
dp= [[0, 0] for _ in range(n+1)]
dp[1]= [0, 1]
for i in range(2, n+1):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]
    dp[i][1]=dp[i-1][0]
print(sum(dp[n]))
