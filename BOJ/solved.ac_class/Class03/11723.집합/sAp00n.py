from sys import stdin

M = int(stdin.readline())

set = bin(1048576)
#print(set)

commend_list = ['add', 'remove', 'check', 'toggle', 'all', 'empty']

for _ in range(M):
    commend = stdin.readline().split()
    commend_idx = commend_list.index(commend[0])
    if commend_idx == 0:
        set = bin(int(set,2) | (1 << int(commend[1])))
    elif commend_idx == 1:
        set = bin(int(set,2) & ~(1 << int(commend[1])))
    elif commend_idx == 2:
        temp = int(bin(int(set,2) & (1 << int(commend[1]))), 2)
        if temp > 0:
            print(1)
        else:
            print(0)
    elif commend_idx == 3:
        set = bin(int(set,2) ^ (1 << int(commend[1])))
    elif commend_idx == 4:
        set = bin(2097151)
    else:
        set = bin(1048576)

