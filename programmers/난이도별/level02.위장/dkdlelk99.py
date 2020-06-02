def solution(clothes):
    category = {}
    for i in clothes:
        if i[1] in category:
            category[i[1]] += 1
        else:
            category[i[1]] = 1

    multiply_of_list = 1
    for i in category.values():
        multiply_of_list *= (i+1)
    
    return multiply_of_list-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
 ["green_turban", "headgear"]]) == 5)
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], 
 ["smoky_makeup", "face"]]) == 3)
