'''
https://programmers.co.kr/learn/courses/30/lessons/70129
이진 변환 반복하기
0의 개수와 반복문 돈 횟수 카운트.
'''

def solution(s):
    cnt = num = 0
    while s != "1":
        zero = s.count('0')
        s = format(len(s)-zero,'b')
        num += zero
        cnt += 1
    return [cnt, num]

'''
'''