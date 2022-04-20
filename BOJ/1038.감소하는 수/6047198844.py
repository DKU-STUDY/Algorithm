import sys
from itertools import combinations

N = int(sys.stdin.readline())

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = []

for i in range(1, 10 + 1):
    for j in combinations(arr, i):
        numbers.append(int(''.join(list(map(str,j)))[::-1]))
numbers.sort()
if N >= len(numbers):
    print(-1)
else:
    print(numbers[N])