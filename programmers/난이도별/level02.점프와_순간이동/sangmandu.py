'''
https://programmers.co.kr/learn/courses/30/lessons/12980
점프와 순간이동
//2와 -1을 해서 0을 만듬. 이 때 -1할때 카운트
'''

def solution(n):
    cnt = 0
    while n:
        if n % 2:
            cnt += 1
            n = n-1
        n = n // 2
    return cnt

'''
def solution(n):
    return bin(n).count('1')
'''