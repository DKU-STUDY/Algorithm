'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12903
문제 : 가운데 글자 가져오기
'''

def solution(s):
    n = len(s)//2
    return s[n-1:n+1] if len(s)%2==0 else s[n]
