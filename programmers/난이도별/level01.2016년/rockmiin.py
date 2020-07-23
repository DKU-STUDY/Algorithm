def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    mon_31 = [1, 3, 5, 7, 8, 10, 12]
    mon_30 = [4, 6, 9, 11]
    sum = 0

    for i in range(1, a):
        if i in mon_31:
            sum += 31
        elif i in mon_30:
            sum += 30
        else:
            sum += 29
    sum += b

    if (sum % 7 == 0):
        return day[0]
    elif (sum % 7 == 1):
        return day[1]
    elif (sum % 7 == 2):
        return day[2]
    elif (sum % 7 == 3):
        return day[3]
    elif (sum % 7 == 4):
        return day[4]
    elif (sum % 7 == 5):
        return day[5]
    elif (sum % 7 == 6):
        return day[6]


if __name__ == "__main__":
    a = 5;
    b = 24;
    print(solution(a, b))