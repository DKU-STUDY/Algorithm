'''
https://programmers.co.kr/learn/courses/30/lessons/12915
문자열 내 마음대로 정렬하기 : 원하는 인덱스를 키로 문자 정렬하기
해당 인덱스의 문자를 문자열 맨 앞으로 추가해서 정렬
'''

def solution(strings, n):
    return [i[1:] for i in sorted([i[n] + i for i in strings])]

'''
sorted는 key를 가지고 정렬할 수 있다는 점 알기
return sorted(strings, key=lambda x: x[n])
'''