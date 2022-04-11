import sys

sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())

line1 = {}
idx = 1
for num in sys.stdin.readline().split():
    line1[num] = idx
    idx += 1

segment_tree = [0 for _ in range(N + 1)]


# init 필요없음
# sum 현재구간 / 구하고자 하는구간
def sum(sgi):
    res = 0
    while sgi > 0:
        res = res + segment_tree[sgi]
        res = res - (res & -res)
    return res


def update(sgi):
    while sgi < N + 1:
        segment_tree[sgi] = segment_tree[sgi] + 1
        sgi = sgi + (sgi & -sgi)


res = 0
for node in sys.stdin.readline().split():
    res += sum(line1[node] + 1)
    update(1, 1, N, line1[node])
print(res)
