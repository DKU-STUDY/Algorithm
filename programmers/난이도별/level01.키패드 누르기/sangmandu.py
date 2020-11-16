'''
https://programmers.co.kr/learn/courses/30/lessons/67256
키패드 누르기
키패드를 1을 중심으로 (0,0)~(3,2)로 설정, 해당 좌표로부터의 거리를 기준으로 조건문
'''


def solution(numbers, hand):
    answer = ''
    l, r = (3, 0), (3, 2)
    for i in numbers:
        if i and i % 3 == 1:
            answer += "L"
            l = (i // 3, 0)
        elif i and i % 3 == 0:
            answer += "R"
            r = (i // 4, 2)
        else:
            n = (i // 4, 1) if i else (3, 1)
            which = abs(n[1] - l[1]) + abs(n[0] - l[0]) - abs(n[1] - r[1]) - abs(n[0] - r[0])
            if which < 0:
                l = n
                answer += "L"
            elif which > 0:
                r = n
                answer += "R"
            else:
                if hand == "left":
                    l = n
                    answer += "L"
                else:
                    r = n
                    answer += "R"

    return answer

'''
'''