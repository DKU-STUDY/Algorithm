'''
https://programmers.co.kr/learn/courses/30/lessons/77884
약수의 개수와 덧셈

'''

def solution(left, right):
    return sum([-num if num ** 0.5 == int(num ** 0.5) else num for num in range(left, right+1)])

'''
'''