N, M = map(int, input().split())

A = set()
B = set()

for _ in range(N):
    A.add(input())
for _ in range(N):
    B.add(input())

print(len(A & B))
for name in sorted(A & B):
    print(name)