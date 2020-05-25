# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# [1, 2, 1, 1, 2, 1]
def solution(A):
    # write your code in Python 3.6
    leader = search_leader(A)
    #print(f'leader = {leader}')
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
        #print(logical_list)
        left_ele_num = 1
        right_ele_num = len(A)-1
        for i in range(len(A) - 1):
            left_condition = logical_list[i] / left_ele_num
            if left_condition > 1 / 2:
                right_condition = (logical_list[-1] - logical_list[i]) / right_ele_num
                if right_condition > 1 / 2:
                    eq_leadernum += 1
            left_ele_num += 1
            right_ele_num -= 1

        return eq_leadernum


def search_leader(A):
    # write your code in Python 3.6
    len_a = len(A)
    condition = len_a // 2
    dic = {}
    for i in A:
        dic[i] = dic.get(i, 0)+1
        if dic[i] > condition:
            return i
    return -1