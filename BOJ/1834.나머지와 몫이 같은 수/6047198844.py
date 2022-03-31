N = int(input())
res = 0
# 나머지이자 몫
for i in range(1, N):
    res += i * N + i
print(res)