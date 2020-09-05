from sys import stdin

T = int(stdin.readline())

for case in range(T):
    input_list = stdin.readline().split()
    input_list = [int(ele) for ele in input_list]
    print(input_list[0]+input_list[1])
