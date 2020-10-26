from sys import stdin
import heapq


def sol(k):
    check = [False] * k
    min_heap = []
    max_heap = []
    for i in range(k):
        commend = stdin.readline().split()
        commend[1] = int(commend[1])
        # print(commend)
        if commend[0] == 'I':
            # print(f'commend : {commend}')
            check[i] = True
            node = (commend[1], i)
            heapq.heappush(min_heap, node)
            node = (-commend[1], i)
            heapq.heappush(max_heap, node)
        if commend[0] == 'D':
            if len(min_heap) > 0:
                if commend[1] == 1:
                    while max_heap:
                        if not check[max_heap[0][1]]:
                            heapq.heappop(max_heap)
                        else:
                            check[max_heap[0][1]] = False
                            heapq.heappop(max_heap)
                            break

                else:
                    while min_heap:
                        if not check[min_heap[0][1]]:
                            heapq.heappop(min_heap)
                        else:
                            check[min_heap[0][1]] = False
                            heapq.heappop(min_heap)
                            break
            # print(f'commend : {commend}     que : min => {min_heap} max => {max_heap}     check: {check}')
    # print(f'loop end    que:{deb_que}')
    # print(check)
    # print(f'{min_heap}      {max_heap}')
    while min_heap and not check[min_heap[0][1]]: heapq.heappop(min_heap)
    while max_heap and not check[max_heap[0][1]]: heapq.heappop(max_heap)
    # print(f'{min_heap}      {max_heap}')
    if len(min_heap) == 0:
        print('EMPTY')
    else:
        result = []
        result.append(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else 'EMPTY')
        print('\n'.join(result))


T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    sol(k)
