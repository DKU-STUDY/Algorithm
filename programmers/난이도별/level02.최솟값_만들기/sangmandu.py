'''
https://programmers.co.kr/learn/courses/30/lessons/12941
최솟값 만들기
각 리스트를 오름차순, 내림차순으로 곱셈
'''

def solution(A,B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B)[::-1])])

'''
'''