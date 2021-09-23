N = input()
ans = 0
Q = [N]

while Q:
    num = Q.pop()
    if len(num) == 1:
        ans += 1
    else:
        i = num[1:]
        j = num[:-1]
        if i == j:
            Q.append(i)
        else:
            Q.append(i)
            Q.append(j)

print(ans)