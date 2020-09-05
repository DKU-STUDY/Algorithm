from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().strip('\n').split()))
A_dict = {}
for ele in A:
    A_dict[ele] = True
M = int(stdin.readline().strip('\n'))
B = list(map(int, stdin.readline().strip('\n').split()))

for ele in B:
    if ele in A_dict:
        print('1')
    else:
        print('0')
