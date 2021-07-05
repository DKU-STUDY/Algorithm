def solution(costs, budget):
    answer = 0
    costs.sort()
    for cost in costs:
        if cost <= budget:
            budget -= cost
            answer += 1
    return answer