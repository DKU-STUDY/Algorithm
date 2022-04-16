import sys

sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())

line1 = {}
idx = 1
for num in sys.stdin.readline().split():
    line1[num] = idx
    idx += 1

tree = [0] * (N + 1)


def update(index, value):
    while index < len(tree):
        tree[index] += value
        index += (index & -index)

    return tree


def query(index):
    res = 0
    while index > 0:
        res += tree[index]
        index -= (index & -index)

    return res


res = 0
for node in sys.stdin.readline().split():
    res += query(N) - query(line1[node])
    update(line1[node], 1)
print(res)