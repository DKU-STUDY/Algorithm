N = int(input())

milks = list()
for _ in range(N):
    milks.append(int(input()))

milks.sort(reverse=True)

print(sum([milk for idx, milk in enumerate(milks) if idx % 3 != 2]))