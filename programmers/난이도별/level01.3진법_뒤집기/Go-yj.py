'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/68935
문제 : 3진법 뒤집기
'''

def solution(n):
    answer = 0
    tri = ''
    # 3진수로 만든 후 앞에 0 제거
    while n>0 :
        tri += str(n%3)
        n //= 3
    tri = str(int(tri))
    
    # 역순으로 변환 후 list로 쪼갬
    dec = list(map(int,tri[::-1]))
    # 10진수로 변환
    for i in range(len(dec)) :
        answer += dec[i] * pow(3,i)
    return answer
