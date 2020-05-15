# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# [1, 2, 1, 1, 2, 1]
def solution(A):
    # write your code in Python 3.6
    leader = search_leader(A)
    # print(f'leader = {leader}')
    if leader == -1:
        return 0

    else:
        eq_leadernum = 0
        n = len(A)
        logical_list = [0 for i in range(n)]
        temp = 0
        for value in range(n):
            if A[value] == leader:
                temp += 1
            logical_list[value] = temp
        # print(logical_list)
        for i in range(len(A) - 1):
            left_ele_num = len(A[:i + 1])
            right_ele_num = len(A[i + 1:])
            left_condition = logical_list[i] / left_ele_num
            if left_condition > 1 / 2:
                right_condition = (logical_list[-1] - logical_list[i]) / right_ele_num
                if right_condition > 1 / 2:
                    '''print(
                        f'left = {A[:i + 1]}len({left_ele_num})\nleft_logical = {logical_list[i]}\nright = {A[i + 1:]}len({right_ele_num})\nright_logical = {logical_list[-1] - logical_list[i]}')
                    print(i + 1)
                    print('\n')'''
                    eq_leadernum += 1

        return eq_leadernum


def search_leader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        elif value != A[k]:
            size -= 1
        else:
            size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0

    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader