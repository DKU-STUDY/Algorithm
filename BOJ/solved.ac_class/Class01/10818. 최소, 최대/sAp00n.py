from sys import stdin

N = int(stdin.readline())

input_list = stdin.readline().split()
input_list = [int(ele) for ele in input_list]

print(f'{min(input_list)} {max(input_list)}')
