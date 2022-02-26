L = int(input())
line = list(input())
r = 31
M = 1234567891
res = 0
for i in range(L):
    a = ord(line[i]) - ord('a') + 1
    res += (a * r ** i)
res %= M
print(res)