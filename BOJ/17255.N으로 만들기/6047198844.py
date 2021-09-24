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
        Q.append(i)
        if i != j:
            Q.append(j)


print(ans)