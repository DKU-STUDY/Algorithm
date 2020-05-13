# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    leader = search_leader(A)
    # print(f'leader = {leader}')
    if leader == -1:
        return 0

    else:
        eq_leadernum = 0
        ind_list = []
        for ind in range(len(A)):
            if A[ind] == leader:
                ind_list.append(ind + 1)

        for i in ind_list:
            left = A[:i]
            right = A[i:]
            left_leader = search_leader(left)
            right_leader = search_leader(right)
            if left_leader == right_leader:
                eq_leadernum += 1
                # print(f'num++ i={ind_list[i]}')
        return eq_leadernum


def search_leader(A):
    condition = len(A) // 2
    leader = -1
    dic = {}
    if len(A) == 1:
        leader = A[0]
        return leader

    for i in A:
        if i in dic:
            dic[i] += 1
            if dic[i] > condition:
                leader = i
                # print(dic)
                return leader
        else:
            dic[i] = 1
    return leader