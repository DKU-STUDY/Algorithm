from sys import stdin


def sub_list(input_list):
    if len(input_list) == 1:
        return input_list[0]
    mid_idx = len(input_list) // 2
    sub_max = max(sub_list(input_list[:mid_idx]), sub_list(input_list[mid_idx:]))
    start, end = mid_idx - 1, mid_idx
    min_val = min(input_list[start], input_list[end])
    mid_max = min_val * 2
    # print(f'in : {input_list}')
    while 0 < start or end < len(input_list) - 1:
        # print(f'start:{start}  end: {end}   mid_max:{mid_max}')
        if start > 0:
            if end == len(input_list) - 1 or input_list[start - 1] >= input_list[end + 1]:
                start -= 1
                min_val = min(min_val, input_list[start])
                mid_max = max(mid_max, min_val * (end - (start - 1)))
                continue
        end += 1
        min_val = min(min_val, input_list[end])
        mid_max = max(mid_max, min_val * (end - (start - 1)))
    # print(f'sub_max:{sub_max}   mid_max:{mid_idx}')
    return max(sub_max, mid_max)


N = int(stdin.readline())
input_list = []
for _ in range(N):
    input_list.append(int(stdin.readline()))

print(sub_list(input_list))
