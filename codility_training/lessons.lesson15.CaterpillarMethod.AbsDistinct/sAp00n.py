def solution(A):
    distnct_num = 0
    ele_dict = {}
    for ele in A:
        if ele < 0:
            abs_ele = abs(ele)
        else:
            abs_ele = ele
        if abs_ele not in ele_dict:
            ele_dict[abs_ele] = True
            distnct_num += 1
    return distnct_num


A = [-5, -3, -1, 0, 3, 6]
print(solution(A))
