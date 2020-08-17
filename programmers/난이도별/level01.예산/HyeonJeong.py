def solution(d, budget):
    tries = 0
    for n in sorted(d):
        if budget < n:
            break #break는 for문에서 빠져나오게 함.
        budget -= n
        tries += 1
    return tries

print(
    solution([1,3,2,5,4], 9) == 3,
    solution([2,2,3,3], 10) == 4
     )