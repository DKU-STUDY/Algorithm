def solution(a, b):

    total = b
    day_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    months_29 = [2]

    for i in range (1, a):
        if i in months_31:
            total += 31
        elif i in months_30:
            total += 30
        elif i in months_29:
            total += 29


    rest = total % 7
    answer = day_list [rest]

    return answer