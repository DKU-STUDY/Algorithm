N = int(input())

tips = list()
for _ in range(N):
    tips.append(int(input()))
tips.sort(reverse=True)

res = 0
i = 0
for nth in range(N):
    if tips[nth] - nth > 0:
        res += tips[nth] - nth
    else:
        break
print(res)
