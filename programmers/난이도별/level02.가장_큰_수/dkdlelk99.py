def solution(numbers):
    answer = ""
    sorted_num = []
    for num in numbers:
        sorted_num.append(str(num)*3)
    sorted_num = sorted(sorted_num, reverse=True)
    for num in sorted_num:
        answer += num[:int(len(num)/3)]
    return answer

print(solution([6,10,2]) == '6210')
print(solution([21,212]) == '21221')
print(solution([999,9,998]) == '9999998')
