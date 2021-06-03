'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12954
문제 : x만큼 간격이 있는 n개의 숫자
x를 리스트에 넣고 x만큼 더하는 과정을 n번 반복하였습니다.
'''

def solution(x, n):
    answer = []
    num = x
    for i in range(0,n) :
        answer.append(num)
        num += x
    return answer
