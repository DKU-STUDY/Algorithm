def solution(N, stages):
    answer = []
    failure_list = []
    failure = {}
    fail_sum = 0
    for stage in range(1, N+1):
        failure[stage] = (stages.count(stage) / (len(stages) - fail_sum))
        fail_sum += stages.count(stage)
    failure_list = sorted(failure.items(), key = lambda x: x[1], reverse=True)
    for key, val in failure_list:
        answer.append(key)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5])
print(solution(4, [4,4,4,4,4]) == [4,1,2,3])

# 런타임 에러로 실패
