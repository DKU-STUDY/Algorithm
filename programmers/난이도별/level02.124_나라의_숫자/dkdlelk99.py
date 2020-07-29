def solution(n):
    rule = '124'
    cnt = 1
    while 3**cnt <= n:
        n -= 3**cnt
        cnt += 1
    if n == 0:
        return '4' * (cnt -1)
    answer = '1' * cnt
    for i in range(n - 1):
        check_4 = 0
        if answer[-1:] == '1':
            answer = answer[:-1] + '2'
        elif answer[-1:] == '2':
            answer = answer[:-1] + '4'
        elif answer[-1:] == '4':
            for ans in range(1, cnt + 1):# cnt == len(answer)
                check_4 += 1
                if answer[-ans] != '4':
                    break
            answer = answer[:-(check_4 - 1)] # 여기서 잘못됨 0부터 뒤에서 체크4까지
            if answer[-1:] == '1':
                answer = answer[:-1] + '2'
            elif answer[-1:] == '2':
                answer = answer[:-1] + '4'
            answer += '1' * (check_4 - 1)

    return answer
    
print(solution(1), solution(1) == '1')
print(solution(2), solution(2) == '2')
print(solution(3), solution(1) == '4')
print(solution(4), solution(1) == '11')
