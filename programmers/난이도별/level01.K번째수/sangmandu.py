'''
https://programmers.co.kr/learn/courses/30/lessons/42748
K번째수
1. 주어진 배열의 i~j 인덱스의 부분 배열을 정렬 후 k번째 값 찾기
2. 문제 그대로 풀이
'''
def solution(array, commands):
    return [ sorted(array[ a - 1 : b ])[ c - 1 ] for (a, b, c) in commands ]
'''
'''