import math
import sys

K = int(input())

for i in range(1, K + 1):
    N, *scores = map(int, sys.stdin.readline().split())
    scores.sort(reverse=True)
    largest_gap = 0
    for j in range(len(scores) - 1):
        largest_gap = max(largest_gap, scores[j] - scores[j+1])

    print(f'Class {i}')
    print(f'Max {max(scores)}, Min {min(scores)}, Largest gap {largest_gap}')
