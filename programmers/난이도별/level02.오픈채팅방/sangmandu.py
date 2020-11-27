'''
https://programmers.co.kr/learn/courses/30/lessons/42888
오픈채팅방
가장 마지막에 Enter 또는 Change 된것이 최종 닉네임
'''

def solution(record):
    uid = {}
    for i in record:
        if i[0] == "L": continue
        b, c = i.split()[1:]
        uid[b] = c

    answer = []
    for i in record:
        if i[0] == "C": continue
        a, b = i.split()[:2]
        answer.append(f"{uid[b]}님이 들어왔습니다." if a == "Enter" else f"{uid[b]}님이 나갔습니다.")
    return answer

'''     
'''