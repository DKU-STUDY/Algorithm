'''
https://programmers.co.kr/learn/courses/30/lessons/12977
소수 만들기
[풀이]
1. 아리스토테네스의 채
'''
from itertools import combinations
def solution(nums):
    nums = sorted([sum(i) for i in combinations(nums, 3)])
    rear = nums[-1]
    sieve = [True] * (rear+1)
    for i in range(2, rear+1):
        if sieve[i] == True:
            for j in range(i+i, rear+1, i):
                sieve[j] = False
    return [sieve[i] for i in nums].count(True)
'''
'''