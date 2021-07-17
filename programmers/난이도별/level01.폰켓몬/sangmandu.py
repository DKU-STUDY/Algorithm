'''
https://programmers.co.kr/learn/courses/30/lessons/1845
폰켓몬
[풀이]
1. set 사용
'''
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
'''
'''