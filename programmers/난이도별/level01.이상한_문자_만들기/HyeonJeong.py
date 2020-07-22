def solution(s):
    answer = ""
    list = s.split(" ")
    for n in list:
        for m in range(len(list[n])): #s를 빈칸단위로 분리해서  list에 담았더니 이러한 방식으로는 작동이 불가능하다고 뜹니다.
            str = list[n][m]
            if "a" <= str <= "z" and c % 2 == 0:
                answer += str.upper()
            elif "A" <= str <= "Z" and c % 2 == 1:
                answer += str.lower()
            else:
                answer += str
        answer += " "
    return answer

'''
정답 예시
try hello world는 세 단어 try, hello, world로 구성되어 있습니다.
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다.
따라서 TrY HeLlO WoRlD 를 리턴합니다.
'''

'''
처음에는 제가 문제를 빈칸 포함한 전체 단어라고 잘못 이해하였습니다.
이 생각대로 하면 답은 아래처럼 완성하였습니다.

def solution(s):
    answer = ""
    for i in range(len(s)):
        c = s[i]
        if c == " " :
            answer += " "
        else:
            if "a" <= c <= "z" and i % 2 == 0:
                answer += c.upper()
            elif "A" <= c <= "Z" and i % 2 == 1:
                answer += c.lower()
            else:
                answer += c
    return answer
'''