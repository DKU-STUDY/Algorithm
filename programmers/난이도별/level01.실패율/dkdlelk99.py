def solution(N, stages):
    user = len(stages)
    failure = {}
    fail_sum = 0
    for stage in range(1, N+1):
        if user != fail_sum:
            failure[stage] = (stages.count(stage) / (user - fail_sum))
            fail_sum += stages.count(stage)
        else:
            failure[stage] = 0
    return [ x[0] for x in sorted(failure.items(), key = lambda x: x[1], reverse=True) ]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5])
print(solution(4, [4,4,4,4,4]) == [4,1,2,3])
