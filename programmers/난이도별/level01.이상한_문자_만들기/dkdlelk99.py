def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
        else:
            count += 1
            answer += s[i].upper() if count % 2 == 0 else s[i].lower()
    return answer

print(solution('Try hard') == 'TrY HaRd')
print(solution('This is difficult') == 'ThIs Is DiFfIcUlT')
