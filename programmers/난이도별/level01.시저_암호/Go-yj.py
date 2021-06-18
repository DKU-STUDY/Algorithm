'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12926
문제 : 시저 암호
아스키 코드로 변경하여 n만큼 수를 더해주는 방법을 사용하였습니다.
저는 대문자, 소문자를 확인할 때도 아스키 코드를 사용하였는데
isupper(), islower()를 사용하여 더 간단하게 대소문자를 구분할 수 있었습니다.
또한 n만큼 더했을 때 알파벳 범위를 벗어나는 경우를 저는 따로 if를 사용하여 판별하였는데
이 또한 26으로 나눈 나머지를 이용하여 한 번에 구할 수 있었습니다.
[메모]
대문자의 경우 : chr((ord(i)-ord('A')+n)%26+ord('A'))
소문자의 경우 : chr((ord(i)-ord('a')+n)%26+ord('a'))
'''

def solution(s, n):
    answer = ''
    s = list(s)
    for i in s :
        if ord(i) == ord(' ') :
            answer += ' '
        elif ord(i) <= ord('Z') :
            if n+ord(i) > ord('Z') :
                answer += chr(ord(i)+n-26)
            else :
                answer += chr(ord(i)+n)
        else :
            if n+ord(i) > ord('z') :
                answer += chr(ord(i)+n-26)
            else :
                answer += chr(ord(i)+n)
    return answer
