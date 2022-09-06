import sys
from collections import Counter

while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        cnt = 0
        for i in range(N, M + 1):
            cnt += Counter(str(i)).most_common()[0][1] == 1
        print(cnt)
    except:
        break
