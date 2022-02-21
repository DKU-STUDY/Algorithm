import sys

visited = set()
N = int(input())
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    visited.add(line)
    if line[::-1] in visited:
        print(len(line), line[len(line)//2])