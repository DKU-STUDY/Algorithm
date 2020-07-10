def solution(a, b):
    answer = ''
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    i = b % 7

    if ( a == 1 or a == 4 or a == 7):
        if(4 <=i <= 6):
            answer = day_list [i-4]
        else:
            answer = day_list [i+3]

    elif (a == 2 or a == 8):
        if(i == 0):
            answer = day_list [6]
        else:
            answer = day_list [i-1]

    elif (a == 3 or a == 11):
            answer = day_list [i]

    elif (a == 5):
        if(0 <= i <= 1):
            answer = day_list [i+5]
        else:
            answer = day_list [i-2]

    elif (a == 6):
        if(i ==  6):
            answer = day_list [0]
        else:
            answer = day_list [i+1]

    elif (a == 9 or a == 12):
        if(5 <= i <= 6):
            answer = day_list [i-5]
        else:
            answer = day_list [i+2]
    elif (a == 10):
        if(0 <= i <= 2):
            answer = day_list [i+4]
        else:
            answer = day_list [i-3]

    return answer