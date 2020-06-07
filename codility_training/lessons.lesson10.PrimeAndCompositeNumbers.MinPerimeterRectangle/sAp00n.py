from random import randint

def solution(N):
    couple_list = find_couple(N)
    return_val = find_min_perimeter(couple_list)
    return return_val

def find_couple(A):
    i = 1
    list_of_couple = []
    while i * i <= A:
        if A % i == 0:
            val01 = i
            val02 = int(A / i)
            couple = (min(val01, val02), max(val01, val02))
            if couple not in list_of_couple:
                list_of_couple.append(couple)
        i += 1
    if A == i:
        list_of_couple.append((1, 1))
    return list_of_couple


def find_min_perimeter(list_of_couple):
    min_perimeter = 2 * (list_of_couple[0][0] + list_of_couple[0][1])
    list_length = len(list_of_couple)
    if list_length == 2:
        min_perimeter = min(min_perimeter, 2 * (list_of_couple[1][0] + list_of_couple[1][1]))
    else:
        for idx in range(2, len(list_of_couple)):
            min_perimeter = min(min_perimeter, 2 * (list_of_couple[idx][0] + list_of_couple[idx][1]))
    return min_perimeter

