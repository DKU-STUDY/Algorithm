def solution(scoville, K):
    answer = 0
    # for i in range(len(n for n in scoville if n < K)):
    while K > min(scoville):
        # scoville[1] = scoville[0] + (2 * scoville[1])
        mix = scoville.pop(scoville.index(min(scoville))) + 2*scoville.pop(scoville.index(min(scoville)))
        scoville.append(mix)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7), solution([1, 2, 3, 9, 10, 12], 7) == 2)
#1st try fail
#1, 3, 8, 14 런타임 에러, 효율성 0점
