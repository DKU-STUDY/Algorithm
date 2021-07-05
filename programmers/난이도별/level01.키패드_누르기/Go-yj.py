'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/67256
문제 : 키패드 누르기
'''

def solution(numbers, hand):
    answer = ''
    left = 10   # 키패드 *:10, 0:11, #:12로 지정
    right = 12
    distance = {    # value : 키패드 숫자 차이, key : 거리
        1 : [1,3],
        2 : [2,4,6],
        3 : [5,7,9],
        4 : [8,10]
    }
    for i in numbers :
        if i in [1,4,7] :   # 누를 키패드가 1,4,7인 경우 왼손 사용
            answer += 'L'
            left = i
        elif i in [3,6,9] : # 누를 키패드가 3,6,9인 경우 오른손 사용
            answer += 'R'
            right = i
        else :
            if i==0 : i = 11
            l_dist = abs(left-i)    # 현재 손위치의 숫자와 누를 키패드 숫자의 차
            r_dist = abs(right-i)
            for key, val in distance.items() :  # distance의 value에 해당하는 key 값(거리) 가져옴
                if l_dist in val :
                    l_dist = key
                if r_dist in val :
                    r_dist = key
            if l_dist == r_dist :   # 왼손, 오른손 거리가 같으면 hand로 결정
                if hand=='right' :
                    answer += 'R'
                    right = i
                else :
                    answer += 'L'
                    left = i
            elif l_dist <= r_dist : # 왼손 거리가 더 짧으면 왼손 사용
                answer += 'L'
                left = i
            else :                  # 오른손 거리가 더 짧으면 오른손 사용
                answer += 'R'
                right = i
    return answer
