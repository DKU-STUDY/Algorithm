import math
import sys
from collections import Counter, defaultdict


def arr_sum(acc, arr, dictionary, limit):
    for i in range(limit):
        for j in range(i, limit):
            if i == j:
                acc[i][j] = arr[i]
            else:
                acc[i][j] = acc[i][j - 1] + arr[j]
            dictionary[acc[i][j]] += 1


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B_arr = list(map(int, sys.stdin.readline().split()))

A_acc = [[math.inf for _ in range(n)] for _ in range(n)]
B_acc = [[math.inf for _ in range(m)] for _ in range(m)]
A_dict = defaultdict(int)
B_dict = defaultdict(int)

arr_sum(A_acc, A_arr, A_dict, n)
arr_sum(B_acc, B_arr, B_dict, m)

res = 0
for i in A_dict:
    if T - i in B_dict:
        res += A_dict.get(i) * B_dict.get(T - i)

print(res)
