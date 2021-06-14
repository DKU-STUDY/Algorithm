'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12930
문제 : 이상한 문자 만들기
원래 s.split(" ")을 이용하여 공백을 기준으로 나눈 후,
아래와 같은 방법으로 대소문자를 구분하여 (" ").join을 사용하여 합쳐주었는데
계속 오류가 발생했습니다. 질문을 보니 공백 갯수만큼 공백을 유지해 줘야 한다 해서
아래와 같이 split으로 나누지 않고 if를 통해 공백일 경우, 아닐 경우를
판별하여 추가해주게 되었습니다.
'''

def solution(s):
    answer = ''
    num = 0
    for i in range(len(s)) :
        if s[i] == ' ' : 
            answer += ' '
            num = 0
        else :
            if num%2 == 0 :
                answer += s[i].upper()
                num += 1
            else :
                answer += s[i].lower()
                num += 1
    return answer
