'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12940
문제 : 최대공약수와 최소공배수
'''

def solution(n, m):
    answer = []
    big_num = max(n,m)
    for i in range (big_num,0,-1) : # 최대공약수 구하기
        if (m%i==0) and (n%i==0) :
            answer.append(i)
            break
    for i in range(big_num,n*m+1) :  # 최소공배수 구하기
        if (i%m==0) and (i%n==0) :
            answer.append(i)
            break
    return answer
