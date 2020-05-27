def find_peaks(A):
    peak_logical_list = [0 for i in range(len(A))]  # Peak Node == 1 else == 0
    past_element = A[0]
    current_element = A[1]
    next_element = A[2]

    if past_element < current_element > next_element:
        peak_logical_list[1] = 1

    for idx in range(1, len(A) - 1):
        past_element = A[idx - 1]
        current_element = A[idx]
        next_element = A[idx + 1]
        if past_element < current_element > next_element:
            peak_logical_list[idx] = 1
    return peak_logical_list

def find_min_subunit_length(logical_list):
    list_length = len(logical_list)
    idx = 1
    forward_ele = logical_list[0]
    while not(forward_ele != 1 or idx <= list_length-1):
        forward_ele = logical_list[idx]
        idx += 1
    forward_candidate = logical_list.index(forward_ele) + 1

    idx = -2
    backward_ele = logical_list[-1]
    while not(backward_ele != 1 or (idx * -1) <= list_length):
        backward_ele = logical_list[idx]
        idx -= 1
    backward_candidate = list_length - logical_list.index(backward_ele)+1
    return_val = min(forward_candidate, backward_candidate)
    return return_val

def check_function(logical_list, subunit_len):

    if len(logical_list)%subunit_len != 0:
        return False

    number_of_subunit = int(len(logical_list)/subunit_len)
    start_slice = 0
    end_slice = subunit_len
    for i in range(1, number_of_subunit):
        subunit = logical_list[start_slice:end_slice]
        for ele in subunit:
            if ele == 1:
                checker = True
                break
            checker = False
        if checker == False:
            break
        start_slice += subunit_len
        end_slice += subunit_len
    return checker
def solution(A):
    logical_list = find_peaks(A)
    Max_subunit_len = len(A)/2

    min_subunit_len = find_min_subunit_length(logical_list)
    subunit_len = min_subunit_len
    while subunit_len <= Max_subunit_len :
        temp = check_function(logical_list, subunit_len)
        if temp == True:
            return  int(len(A)/subunit_len)
        subunit_len += 1

A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
print(solution(A))