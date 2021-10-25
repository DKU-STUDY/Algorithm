import sys
from itertools import combinations

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

stickers = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = 0

for sticker in combinations(stickers, 2):
    A, B = sticker
    RA, CA = A
    RB, CB = B
    # A , B
    if (RA + RB <= H and CA <= W and CB <= W) or (CA + CB <= W and RA <= H and RB <= H):
        res = max(res, RA * CA + RB * CB)
    # A(90), B
    elif (CA + RB <= H and RA <= W and CB <= W) or (RA + CB <= W and CA <= H and RB <= H):
        res = max(res, RA * CA + RB * CB)
    # A, B(90)
    elif (RA + CB <= H and CA <= W and RB <= W) or (CA + RB <= W and RA <= H and CB <= H):
        res = max(res, RA * CA + RB * CB)
    # A(90), B(90)
    elif (CA + CB <= H and RA <= W and RB <= W) or (RA + RB <= W and CA <= H and CB <= H):
        res = max(res, RA * CA + RB * CB)

print(res)