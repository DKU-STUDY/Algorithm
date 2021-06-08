'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12935
문제 : 제일 작은 수 제거하
제일 작은수(min(arr))을 제거(remove())함.
'''

def solution(arr):
    answer = []
    if len(arr) == 0 or len(arr) == 1 :
        answer.append(-1)
        return answer
    arr.remove(min(arr))
    return arr
