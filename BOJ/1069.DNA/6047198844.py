from collections import Counter

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
res_dna = ''
for i in list(zip(*arr)):
    k = Counter(i).items()
    res_dna += sorted(k, key=lambda i:(-i[1], i[0]))[0][0]

res_diff = 0
for i in arr:
    for j in range(M):
        if i[j] != res_dna[j]:
            res_diff += 1
print(res_dna)
print(res_diff)