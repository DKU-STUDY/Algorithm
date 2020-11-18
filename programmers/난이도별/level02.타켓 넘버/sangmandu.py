'''
https://programmers.co.kr/learn/courses/30/lessons/12905
타켓넘버
숫자의 개수가 20개 이고, 모든 숫자는 양 또는 음의 수를 가지므로 최대 2의 20승, 대략 백만정도의 크기.
따라서 각각의 경우의 수를 모두 구하고 모든 경우의 수가 target과 매칭되는 경우를 카운트
'''

import numpy
def pm(numbers, target):
    if not numbers: return target
    num = numbers.pop()
    return [pm(numbers[:], target-num), pm(numbers[:], target+num)]
def solution(numbers, target):
    return numpy.array(pm(numbers, target)).flatten().tolist().count(0)

'''
좀 더 효과적인 재귀
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
        
고인물 시리즈 product를 저렇게 이용하다니 대단하다.
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
'''
