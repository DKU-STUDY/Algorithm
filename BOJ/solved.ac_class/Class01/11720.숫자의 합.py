from sys import stdin

N = int(stdin.readline())
input_str = stdin.readline()
input_list = map(int, [input_str[idx] for idx in range(N)])

print(sum(input_list))
