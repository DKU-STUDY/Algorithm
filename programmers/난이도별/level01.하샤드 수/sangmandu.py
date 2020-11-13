'''
https://programmers.co.kr/learn/courses/30/lessons/12947
하샤드 수
list화 하여 sum
'''

def solution(x):
    return not x % sum(list(map(int, str(x))))

'''
'''