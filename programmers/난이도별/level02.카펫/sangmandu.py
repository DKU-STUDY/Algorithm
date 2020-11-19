'''
https://programmers.co.kr/learn/courses/30/lessons/42842
카펫
'''

def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0 and i + (yellow // i) == (brown - 4) // 2:
            return [yellow // i+2, i+2]

'''
'''