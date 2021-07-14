'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/17687#
문제 : [3차] n진수 게임
'''

def solution(n, t, m, p):
    num = [x for x in range(1,t*m)]     # n진수 만들 개수(그냥 for문에서 범위 지정해도 됐었네요)
    over = ['A','B','C','D','E','F']    # 10 이상일 때 알파벳으로 바꿔주기
    rule = '0'
    for i in num :
        temp = ''
        while i>0 :                     # n진수로 만들기
            if i%n >= 10 : temp += over[(i%n)%10]   # 나머지가 10 이상일 때는 over 리스트 이용해서 알파벳으로 변환
            else : temp += str(i%n)     # 나머지가 10 미만일 때는 그대로 +=
            i //= n
        rule += temp[::-1]              # 반대로 뒤집어서 합쳐줍니다
    return rule[p-1:t*m:m]              # 다른 사람들 풀이 : rule[p-1::m][:t]
