'''
https://programmers.co.kr/learn/courses/30/lessons/12943
콜라츠 추측
[풀이]
1. 주어진 알고리즘 그대로 풀이
'''
def solution(num):
    for i in range(500):
        if num == 1: return i
        num = num * 3 + 1 if num & 1 else num // 2
    return -1

'''
'''