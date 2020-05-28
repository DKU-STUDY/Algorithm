def find_peaks(A):
    peak_logical_list = [0 for i in range(len(A))]  # Peak Node == 1 else == 0
    past_element = A[0]
    current_element = A[1]
    next_element = A[2]
    peak_num = 0
    if past_element < current_element > next_element:
        peak_logical_list[1] = 1
        peak_num += 1

    for idx in range(1, len(A) - 1):
        past_element = A[idx - 1]
        current_element = A[idx]
        next_element = A[idx + 1]
        if past_element < current_element > next_element:
            peak_logical_list[idx] = 1
            peak_num += 1
    #print(peak_logical_list)
    if peak_num == 0:
        return False
    return peak_logical_list


def find_Max_subunit_number(logical_list):
    list_length = len(logical_list)
    forward_candidate = logical_list.index(1) + 1
    logical_list.reverse()
    backward_candidate = logical_list.index(1) + 1
    # print(f'for:{forward_candidate}     back: {backward_candidate}')
    return_val = min(forward_candidate, backward_candidate)
    return_val = int(list_length / return_val)
    # print(f'Max_subunit_num:{return_val}')
    return return_val


def check_function(logical_list, number_of_subunit):
    if len(logical_list) % number_of_subunit != 0:
        return False

    subunit_len = int(len(logical_list) / number_of_subunit)
    start_slice = 0
    end_slice = subunit_len
    if number_of_subunit == 1:
        subunit = logical_list
        for ele in subunit:
            if ele == 1:
                checker = True
                break
            checker = False
        # print(f'checker :{checker}')
    else:
        for i in range(0, number_of_subunit):
            subunit = logical_list[start_slice:end_slice]
            #print(f'subunit = {subunit}')
            for ele in subunit:
                if ele == 1:
                    checker = True
                    break
                checker = False
            #print(f'checker :{checker}')
            if checker == False:
                break
            start_slice += subunit_len
            end_slice += subunit_len
    #print(f'check result: {checker}')
    return checker


def solution(A):
    if len(A) < 3:
        return 0
    logical_list = find_peaks(A)
    if logical_list == False:
        return 0

    Max_subunit_number = find_Max_subunit_number(logical_list)
    subunit_number = Max_subunit_number
    while subunit_number >= 1:
        #print(f'subunit_num = {subunit_number}')
        temp = check_function(logical_list, subunit_number)
        if temp == True:
            return subunit_number
        subunit_number -= 1
    return 0


#A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
A= [1, 2, 3, 4, 5, 6, 5, 5, 5, 6, 5, 6]
print(solution(A))
