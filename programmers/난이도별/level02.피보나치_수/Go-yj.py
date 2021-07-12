'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12945
문제 : 피보나치 수
예전에 문제 리뷰하다가 본 멀리뛰기 문제랑 굉장히 유사했으나
며칠 지났다고 어떻게 했었는지 잊어버렸더라구요 ㅋㅋㅋㅋㅋ
리스트 없이 푸는 방법 다시 메모!
[메모메모]
a,b = 0,1
for i in range(2,n+1) :
    a,b = b,a+b
return b
'''

def solution(n):
    F = [0,1]
    for i in range(2,n+1) :
        F.append(F[i-1]+F[i-2])
    return F[-1]%1234567
