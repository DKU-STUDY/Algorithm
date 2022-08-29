import sys

N, W, H, L = map(int, sys.stdin.readline().split())
print(min(N, (W // L) * (H // L)))
