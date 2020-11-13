'''
https://programmers.co.kr/learn/courses/30/lessons/12903
가운데 글자 출력, 길이가 짝수면 2개의 char 출력
if else 사용, 더 잘하는 사람은 if문 안쓰고 풀음
'''

def solution(s):
    size = len(s)
    return (s[size//2-1] if size % 2 == 0 else "") + s[size//2]