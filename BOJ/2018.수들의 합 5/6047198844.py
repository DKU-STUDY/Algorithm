import sys

N = int(sys.stdin.readline())
cur = 0
small = 1
res = 0
for i in range(1, N + 1):
    cur += i

    # 현재값이 클 경우. small 값을 빼준다. small 은 1씩 증가한다.
    while cur > N:
        cur -= small
        small += 1

    # 같으면 종류를 추가한다.
    if cur == N:
        res += 1
print(res)