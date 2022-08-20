import sys
from collections import defaultdict

N = int(sys.stdin.readline())
for _ in range(N):
    table = defaultdict(int)
    s = sys.stdin.readline().rstrip()
    i = 0
    while i < len(s):
        table[s[i]] += 1
        if table[s[i]] % 3 == 0:
            if i + 1 >= len(s) or table[s[i + 1]] != table[s[i]]:
                print('FAKE')
                break
            else:
                i += 1
        i += 1
    else:
        print('OK')