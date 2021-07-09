'''
https://programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어
[풀이]
1. list의 index와 실제 영어 단어를 매칭
2. replace 함수는 한번만이 아니라 해당하는 모든 문자열을 바꾼다.
=> find 함수는 하나만 찾기 때문에 이런 문자열 함수들을 자세히 알아둬야함
'''
def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for idx, n in enumerate(number):
        s = s.replace(n, str(idx))
    return int(s)
'''
'''