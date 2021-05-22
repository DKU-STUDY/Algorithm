from sys import stdin


def sub_list(input_list):
    if len(input_list) == 0: return 0
    if len(input_list) == 1:
        return input_list[0] * input_list[0]

    mid_idx = len(input_list) // 2
    sub_max = max(sub_list(input_list[:mid_idx]), sub_list(input_list[mid_idx:]))
    start, end = mid_idx, mid_idx
    mid_max = input_list[start] * input_list[start]
    min_val = input_list[start]
    sum_of_list = input_list[start]

    while 0 < start or end < len(input_list) - 1:
        if start > 0:
            if end == len(input_list) - 1 or input_list[start - 1] >= input_list[end + 1]:
                start -= 1
                min_val = min(min_val, input_list[start])
                sum_of_list += input_list[start]
                mid_max = max(mid_max, sum_of_list * min_val)
                continue
        end += 1
        min_val = min(min_val, input_list[end])
        sum_of_list += input_list[end]
        mid_max = max(mid_max, sum_of_list * min_val)

    return max(sub_max, mid_max)


N = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))

print(sub_list(input_list))
