def solution(A):
    element_dict = {}
    for element in A:
        element_dict[element] = 0
    Max_element = max(A)

    for element in A:
        i = 1
        temp = element * i
        while temp <= Max_element:
            if temp in element_dict:
                element_dict[temp] += 1
            i += 1
            temp = element * i
    A_len = len(A)
    for idx in range(A_len):
        A[idx] = A_len - element_dict[A[idx]]
    return A


A = [3, 1, 1, 2, 2, 3, 6]
print(solution(A))
