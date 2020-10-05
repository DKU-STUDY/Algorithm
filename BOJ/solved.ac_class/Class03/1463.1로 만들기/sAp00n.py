from sys import stdin
from collections import deque


def sol():
    input_num = int(stdin.readline())
    if input_num == 1:
        print(0)
        return
    que = deque()
    n = 0
    que.append([input_num])

    while True:
        list_to_compute = que.pop()
        # print(f'list to compute : {list_to_compute}')
        result = []
        temp = []
        for ele in list_to_compute:
            temp += [ele // 2 if ele % 2 == 0 else None, ele // 3 if ele % 3 == 0 else None, ele - 1]
        for i in temp:
            if i is None:
                continue
            result.append(i)
        # print(f'temp : {temp}   result : {result}')
        n += 1
        if 1 in result:
            return print(n)
        que += [result]


sol()
