from sys import stdin


def compute_sum(location):
    global triang_list
    global memo

    line, number = location

    if line == len(triang_list) - 1:
        if location in memo:
            return memo[location]
        return_val = triang_list[line][number]
        memo[location] = return_val
        # print(f'return: {return_val}')
        return return_val

    if number == len(triang_list[line]):
        if (line + 1, number) in memo:
            return triang_list[line][number] + memo[(line + 1, number)]
        return_val = compute_sum((line + 1, number))
        memo[line + 1, number] = return_val
        # print(f'return: {return_val}')
        return triang_list[line][number] + return_val

    if (line + 1, number) in memo:
        left_sum = memo[(line + 1, number)]
    else:
        left_sum = compute_sum((line + 1, number))
        memo[(line + 1, number)] = left_sum
    if (line + 1, number + 1) in memo:
        right_sum = memo[(line + 1, number + 1)]
    else:
        right_sum = compute_sum((line + 1, number + 1))
        memo[(line + 1, number + 1)] = right_sum
    return_val = triang_list[line][number] + max(left_sum, right_sum)
    # print(f'return: {return_val}')
    return return_val


def sol():
    C = int(stdin.readline())
    for _ in range(C):
        n = int(stdin.readline())
        global triang_list
        global memo
        triang_list = []
        memo = {}
        for __ in range(n):
            triang_list.append(list(map(int, stdin.readline().split())))
        print(compute_sum((0, 0)))
        # print(memo)


sol()
