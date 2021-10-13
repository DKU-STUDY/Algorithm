N = int(input())
M = int(input())
shields = map(int, input().split())
table = dict()
res = 0
for shield in shields:
    if shield in table:
        res += 1
    elif shield < M:
        table[M - shield] = True
print(res)