def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
        elif count%2 == 0:
            count += 1
            answer += s[i].upper()
        elif count%2 == 1:
            count += 1
            answer += s[i].lower()
    return answer

print(solution('Try hard') == 'TrY HaRd')
print(solution('This is difficult') == 'ThIs Is DiFfIcUlT')
