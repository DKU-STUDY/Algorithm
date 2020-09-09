def solution(prices):
    answer = []
    len_prices = len(prices)
    for i in range(len_prices):
        up_price = 0
        for j in range(i + 1, len_prices):
            up_price += 1
            if prices[i] > prices[j]:
                answer.append(up_price)
                break
            if j == len_prices - 1:
                answer.append(up_price)
        if i == len_prices - 1:
            answer.append(0)
    return answer
    

print(solution([1,2,3,2,3]), solution([1,2,3,2,3]) == [4,3,1,1,0])
print(solution([2,1,3,42,31,4,5,1,3,6,9,11,2]), solution([2,1,3,42,31,4,5,1,3,6,9,11,2])\
      == [1, 11, 5, 1, 1, 2, 1, 5, 4, 3, 2, 1, 0]) #셀프 테스트
