import sys

S = int(sys.stdin.readline())

cnt = 0
acc = 0
i = 1
while acc <= S:
    acc += i
    i += 1
    cnt += 1
print(cnt-1)