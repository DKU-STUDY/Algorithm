'''
https://programmers.co.kr/learn/courses/30/lessons/12982
예산 : 최적의 해 찾기 문제
부서를 정렬 후, 앞 부서가 할당받지 못하면 뒷 부서 역시 할당받지 못한다고 간주.
'''

def solution(d, budget):
    for i, v in enumerate(sorted(d)):
        if budget < v:
            return i
        budget -= v
    return len(d)

'''
'''