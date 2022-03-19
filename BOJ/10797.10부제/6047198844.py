from collections import Counter

N = int(input())
res = Counter(map(int, input().split())).get(N)
print(res) if res else print(0)