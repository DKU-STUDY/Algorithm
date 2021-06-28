import math
from itertools import permutations


def solution(n, k):
    answer = []
    people = list(range(1, n + 1))

    def dfs(people, nth):
        N = len(people)
        if N == 1:
            return people
        group, nth = nth // math.factorial(N - 1), nth % math.factorial(N - 1)
        M = people.pop(group)
        return [M] + dfs(people, nth)

    answer = dfs(people, k - 1)

    return answer