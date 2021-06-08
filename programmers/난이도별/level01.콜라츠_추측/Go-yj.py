'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12943
문제 : 콜라츠 추측
1이 되지 않으면 계속 반복하는 while문을 사용하여 짝수일때와 홀수일때
사용해야 하는 식을 적었습니다. answer 값이 500이 되면 return 하도록 했습니다.
'''

def solution(num):
    answer = 0
    while num != 1 :
        if num %2 == 0 :
            num /= 2
        else :
            num = num*3+1
        if answer == 500 :
            return -1
        answer += 1
    return answer
