
n, k= map(int, input().split())
coin= []
cnt= 0
for i in range(n):
    coin.append(int(input()))
coin.reverse()

for i in coin:
    if k<i: continue
    tmp= k//i
    cnt+=tmp
    k-=tmp*i
print(cnt)
