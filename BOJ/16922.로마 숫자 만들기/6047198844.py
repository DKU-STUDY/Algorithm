from itertools import combinations_with_replacement

N = int(input())
res = set()
arr = [1, 5, 10, 50]

for i in combinations_with_replacement(arr, N):
    res.add(sum(i))
print(len(res))
