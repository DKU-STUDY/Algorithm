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
        ind_list = []
        n = len(A)
        for ind in range(n):
            if A[ind] == leader:
                ind_list.append(ind)
        # print(ind_list)
        group_dic = {}
        for i in range(len(ind_list) - 1):
            # print(f'left ={A[:ind_list[i]+1]},{ind_list[:i+1]}   right = {A[ind_list[i]+1:]}, {ind_list[i+1:]}')

            # case 01
            # -->
            left_A = A[:ind_list[i] + 1]
            left_leader_ind_list = ind_list[:i + 1]
            right_A = A[ind_list[i] + 1:]
            right_leader_ind_list = ind_list[i + 1:]

            '''print(f'\ncase 01 -->\n left: {left_A}  right: {right_A}')
            print(f'indl_left:{left_leader_ind_list}  indl_right:{right_leader_ind_list}')'''
            dic_key = (str(left_A), str(right_A))
            if dic_key not in group_dic:
                group_dic[dic_key] = 0
                left_condition = len(left_leader_ind_list) / (len(left_A))
                right_condition = len(right_leader_ind_list) / len(right_A)
                '''print(f'left_c = {len(ind_list[:i+1])}/{(ind_list[i]+1)} = {left_condition}  right_c = {len(ind_list[i+1:])}/{len(A[ind_list[i]+1:])} = {right_condition}')'''
                if left_condition and right_condition > 1 / 2:
                    eq_leadernum += 1
                    # print('     eq +1')
            '''else:
                #print('redundant')'''
        for i in range(len(ind_list) - 1, 0, -1):
            # case 02
            # <--
            left_A = A[:ind_list[i]]
            left_leader_ind_list = ind_list[:i]
            right_A = A[ind_list[i]:]
            right_leader_ind_list = ind_list[i:]

            '''print(f'\ncase 02 <--\n left: {left_A}  right: {right_A}')
            print(f'indl_left:{left_leader_ind_list}  indl_right:{right_leader_ind_list}')'''
            dic_key = (str(left_A), str(right_A))
            if dic_key not in group_dic:
                group_dic[dic_key] = 0
                left_condition = len(left_leader_ind_list) / (len(left_A))
                right_condition = len(right_leader_ind_list) / len(right_A)
                '''print(f'left_c = {len(left_leader_ind_list)}/{(len(left_A))} = {left_condition}  right_c = {len(right_leader_ind_list)}/{len(right_A)} = {right_condition}')'''
                if left_condition > 0.5:
                    if right_condition > 0.5:
                        eq_leadernum += 1
                        # print('     eq +1')
            '''else:
                #print('     redundant')'''
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
