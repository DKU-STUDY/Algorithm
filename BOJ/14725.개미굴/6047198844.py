import sys

N = int(sys.stdin.readline())
foods = [sys.stdin.readline().rstrip().split() for _ in range(N)]
ant = {}
for i in range(N):
    node = ant
    for food in foods[i][1:]:
        # 노드가 없으면 생성하고 있으면 생성하지 않는다.
        if food not in node:
            node[food] = {}
        # 다음노드로 파고든다.
        node = node[food]


def func(ant, i):
    keys = sorted(ant.keys())
    for key in keys:
        print('--' * i + key)
        func(ant[key], i + 1)


func(ant, 0)
