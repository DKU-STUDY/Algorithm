import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    F = int(input())
    names = dict()
    names_cnt = 0
    # 이름 > 번호로 변경
    parent = [i for i in range(F*2+1)]
    childNum = [1 for i in range(F*2+1)]

    def getNumber(name: str):
        global names_cnt
        if name in names:
            return names[name]
        else:
            names[name] = names_cnt
            names_cnt += 1
            return names[name]

    def getP(x: int):
        if parent[x] == x:
            return x
        parent[x] = getP(parent[x])
        return parent[x]

    def union(x: int, y: int):
        px, py = getP(x), getP(y)
        if px == py:
            return
        if px > py:
            parent[px] = py
            childNum[py] += childNum[px]
        else:
            parent[py] = px
            childNum[px] += childNum[py]

    for _ in range(F):
        u, v = input().strip().split()
        un, vn = getNumber(u), getNumber(v)
        union(un, vn)
        pn = getP(un)
        print(childNum[pn])
        # print(f"childNum : {childNum} u,v ={u} {v} , un vn = {un} {vn} ")

"""
1
6
Fred Barney
Betty Wilma
Barney Betty
Fred Barney
Barney Betty
Betty Wilma
"""
