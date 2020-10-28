'''
https://programmers.co.kr/learn/courses/30/lessons/12926
시저암호 : 문자열 밀기
알파벳 리스트를 사전에 구성
'''
def solution(s, n):
    U = [chr(i) for i in range(65, 91)]
    L = [chr(i) for i in range(97, 123)]
    answer = ''
    for i in s:
        if i in U : answer += U[(U.index(i)+n)%26]
        elif i in L : answer += L[(L.index(i)+n)%26]
        else : answer += i
    return answer

'''
문자열에는 isupper와 islower가 있음
if s[i].isupper():
    s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
elif s[i].islower():
    s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
'''