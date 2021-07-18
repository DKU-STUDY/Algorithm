'''
https://programmers.co.kr/learn/courses/30/lessons/12932
자연수 뒤집어 배열로 만들기
[풀이]
1. map 사용
'''
def solution(n):
    return list(map(int, str(n)))[::-1]
'''
'''