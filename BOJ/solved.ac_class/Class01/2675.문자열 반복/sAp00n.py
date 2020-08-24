from sys import stdin

T = int(stdin.readline())

for i in range(T):
    input_list = stdin.readline().split()
    input_list[0] = int(input_list[0])
    return_str = ''
    for j in range(len(input_list[1])):
        return_str += input_list[1][j] * input_list[0]
    print(return_str)
