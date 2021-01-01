'''
https://programmers.co.kr/learn/courses/30/lessons/17682
다트 게임 : 숫자, 보너스, 옵션에 대한 점수 계산
정규식 사용
'''

import re

def solution(dartResult):
    record = re.findall('[0-9]{1,2}[SDT][*#]|[0-9]{1,2}[SDT]', dartResult)
    scores = []
    for i in record:
        a = int(''.join(re.findall('[0-9]', i)))
        b = ''.join(re.findall('[SDT]', i))
        c = ''.join(re.findall('[*#]', i))

        if b == 'S':
            score = a
        elif b == 'D':
            score = a ** 2
        else:
            score = a ** 3

        if c == "*":
            score *= 2
            if scores:
                scores[-1] *= 2
        elif c == "#":
            score = -score
        scores.append(score)

    return sum(scores)


'''
if문으로 해당 index의 값을 비교하기 보다는, 미리 딕셔너리화 해서 key값으로 바로 참조하기
정규식을 좀 더 깔끔하게 쓸 것
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
'''