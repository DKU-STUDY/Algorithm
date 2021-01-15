'''
https://programmers.co.kr/learn/courses/18/lessons/43164
여행 경로
dictionary로 사용. dfs 방식 stack 사용.
'''

def solution(tickets):
    dic = {}
    for st, ed in tickets:
        dic.setdefault(st, [])
        dic[st].append(ed)
    for i in dic.keys():
        dic[i].sort(reverse=True)

    stack = ["ICN"]
    save = []
    while stack:
        start = stack[-1]
        if start not in dic or not dic[start]:
            save.append(stack.pop())
            continue
        stack.append(dic[start].pop())

    return save[::-1]

'''
채점 케이스 1번이 너무 안풀려서 한참 골아팠음.
이유는 잘 모르겠다. 나같은 사람들도 많던데,
다만 while문 돌릴 때 ticket의 갯수와 관련없이
stack으로 푸니까 풀렸음
'''