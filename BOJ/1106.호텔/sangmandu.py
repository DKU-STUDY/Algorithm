'''
https://www.acmicpc.net/problem/1106
호텔
DP : Knapsack 풀이방법 이용
'''

from sys import stdin
def solution(target, cities):
    graph = [[0] + [100000] * target  for i in range(len(cities)+1)]
    for idx, b in enumerate(cities):
        for i in range(1, target+1):
                graph[idx+1][i] = min(graph[idx][i], graph[idx+1][i-b[1] if i-b[1] >=0 else 0]+b[0])
    print(graph[len(cities)][target])

target, city = map(int, stdin.readline().split())
cities = [list(map(int, stdin.readline().split())) for _ in range(city)]
solution(target, cities)

'''
'''