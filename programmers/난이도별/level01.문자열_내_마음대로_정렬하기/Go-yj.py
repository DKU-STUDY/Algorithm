'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12915
문제 : 문자열 내 마음대로 정렬하기
처음에는 dictionary의 key에 문자열 넣고, value에 n자리 값 넣어서
value 정렬하려고 혼자 이것저것 뻘짓하고 value 정렬법 찾다가
sorted에 lambda사용해서 너무 간단하게 정렬하는 방법을 알게 됐다.
헤멘건 나뿐인가봐,, 똑똑한 사람들 ⚆_⚆;;
'''

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])
