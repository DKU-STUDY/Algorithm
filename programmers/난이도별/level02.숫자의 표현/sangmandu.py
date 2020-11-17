'''
https://programmers.co.kr/learn/courses/30/lessons/12924
숫자의 표현
'''

def solution(n):
    cnt = 0
    for i in range(1, n):
        sumN = 0
        while sumN < n:
            sumN += i
            i += 1
        if sumN == n:
            cnt += 1
    return cnt + 1

'''
말도 안되는 등차 수열 공식..
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

'''