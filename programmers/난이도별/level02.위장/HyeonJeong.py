def solution(clothes):
    answer = 1
    num = 0
    length = len(clothes)
    list = set([clothes[i][1] for i in range(length)])
    for n in list:
        for m in clothes:
            if n == m[1]:
                num += 1
        answer *= num + 1 # 그 옷을 입지 않는 경우로 + 1
        num = 0
    return answer - 1 # 전부 입지 않는 경우로 -1

print(
    solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]) == 5,
    solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]) == 3
)
