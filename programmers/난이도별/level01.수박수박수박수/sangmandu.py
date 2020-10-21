'''
https://programmers.co.kr/learn/courses/30/lessons/12922
수박수박수박수박수박수? : n만큼 "수", "박" 출력
join, slice
'''

def solution(n):
    answer = "수박" * (n // 2 + 1)
    return answer[:n]

'''

'''