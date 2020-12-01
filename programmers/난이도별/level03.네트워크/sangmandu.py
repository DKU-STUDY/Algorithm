'''
https://programmers.co.kr/learn/courses/30/lessons/43162
네트워크
기본적인 그래프 문제이다. 방문 처리를 해놓는것이 포인트
'''

def solution(n, computers):
    visited = [0] * n

    def cal(visited, idx):
        if visited[idx]:
            return 0
        visited[idx] = 1

        for i in range(n):
            if idx == i:
                continue
            if computers[idx][i]:
                cal(visited, i)
        return 1

    return sum([cal(visited, i) for i in range(n)])

'''
'''