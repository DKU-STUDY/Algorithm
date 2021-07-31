'''
https://programmers.co.kr/learn/courses/30/lessons/67257
수식 최대화
[풀이]
1. +-*의 순열에 따라 모든 반복문 진행. 이후 피연산자 연산자 피연산자를 피연산자의 꼴로 바꿈.
'''
from itertools import permutations
def solution(expression):
    operator = ['+', '-', '*']

    exp = ''
    for i in expression:
        exp += f" {i} " if i in operator else i
    exp = exp.split()

    num = 0
    for i in list(permutations(operator, 3)):
        copy = exp[:]
        for j in i:
            while j in copy:
                idx = copy.index(j)
                copy[idx] = str(eval(copy[idx - 1] + j + copy[idx + 1]))
                copy.pop(idx + 1)
                copy.pop(idx - 1)
        num = max(num, abs(int(copy[0])))
    return num
'''
'''