'''
https://programmers.co.kr/learn/courses/30/lessons/17684
압축 : 주어진 문자열 압죽
가장 긴 문자열부터 확인한다. dict 사용.
'''

def solution(msg):
    dic = {chr(i + 65): i + 1 for i in range(26)}
    length = len(msg)
    num = 27
    answer = []
    idx = 0
    while idx < length:
        for i in range(length, idx, -1):
            if msg[idx:i] in dic.keys():
                answer.append(dic[msg[idx:i]])
                dic[msg[idx:i + 1]] = num
                num += 1
                idx = i
                break
    return answer

'''
'''