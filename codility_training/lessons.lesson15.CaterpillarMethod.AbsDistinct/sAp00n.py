def solution(A):
    distnct_num = 0
    ele_dict = {}
    for ele in A:
        abs_ele = abs(ele)
        ele_dict[abs_ele] = ele_dict.get(abs_ele,True)
    return len(ele_dict)


A = [-5, -3, -1, 0, 3, 6]
print(solution(A))
