import sys

N = int(sys.stdin.readline())

max_num_list = [0, 0, 0]
min_num_list = [0, 0, 0]

for _ in range(N):
    i, j, k = map(int, sys.stdin.readline().split())

    max_num_list[0], max_num_list[1], max_num_list[2] = max(max_num_list[0] + i, max_num_list[1] + i), max(
        max_num_list[0] + j, max_num_list[1] + j, max_num_list[2] + j), max(max_num_list[1] + k, max_num_list[2] + k)

    min_num_list[0], min_num_list[1], min_num_list[2] = min(min_num_list[0] + i, min_num_list[1] + i), min(
        min_num_list[0] + j, min_num_list[1] + j, min_num_list[2] + j), min(min_num_list[1] + k, min_num_list[2] + k)

print(max(max_num_list), min(min_num_list))
