'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/17684
문제 : [3차] 압축
문자열이라서 신난다고 re로 풀었는데 re.match 안에 dictionary 값을 넣을 수는 없어서 포기했다.
나만 또 이상하게 풀고 있는건 아닌가 했는데 다행히 많은 사람들이 dictionary의 key를 이용해서 풀었다.
key에 알파벳을 넣고, value에 값을 넣어 key에 없으면 새로운 값을 추가하는 방식으로 문제를 풀었다.
dictionary는 한 줄로 초기화가 안 될 줄 알았는데 다른 사람들 풀이를 보니 :로 할 수 있었다.
[메모]
dic_alpha = {chr(e+64): e for e in range(1,27)}
'''

def solution(msg):
    answer = []
    start = 0       # 사전에 값 추가 후 인덱스 슬라이싱 시작 부분 변경
    end = 26        # 사전의 마지막 숫자 기억
    dic_match = ''
    
    # 알파벳 대문자 사전
    dic_alpha = {}
    for i in range(26) :
        dic_alpha[chr(i+65)] = i+1
    
    for i in range(1,len(msg)+2) :
        dic_match = msg[start:i]
        if (dic_match not in dic_alpha.keys()) :        # 현재 입력과 일치하는 가장 긴 문자열 찾기
            answer.append(dic_alpha[msg[start:i-1]])
            end += 1
            dic_alpha[dic_match] = end
            start = i-1
    answer.append(dic_alpha[dic_match])
    return answer
