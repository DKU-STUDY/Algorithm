from sys import stdin
from collections import deque


def sol():
    N, K = map(int, stdin.readline().split())

    size_of_space = max(N, K)
    size_of_space = size_of_space + (size_of_space // 2) + 2
    #print(f'size_of space : {size_of_space}')
    if N == K:
        print(0)
        return
    space = [0 for i in range(1, size_of_space)]
    que = deque([[N]])
    #print(que)
    times = 0
    while True:
        times += 1
        current = que.pop()
        #print(current)
        travable = []
        for node in current:
            if node - 1 == K or node + 1 == K or node * 2 == K:
                print(times)
                return
            if node - 1 >= 0:
                if space[node - 2] == 0 or space[node - 2] > times:
                    space[node - 2] = times
                    travable.append(node - 1)
            if node + 1 < size_of_space:
                if space[node] == 0 or space[node] > times:
                    space[node] = times
                    travable.append(node + 1)
            if node * 2 < size_of_space:
                if space[(node * 2) - 1] == 0 or space[(node * 2) - 1] > times:
                    space[(node * 2) - 1] = times
                    travable.append(node * 2)
        que.append(travable)


sol()
