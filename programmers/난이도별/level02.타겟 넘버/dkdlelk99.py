def solution(numbers, target):
    result = [0]
    for num in numbers:
        temp = []
        for i in result:
            temp.append(i + num)
            temp.append(i - num)
        result = temp
    return result.count(target)

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target), solution(numbers, target) == 5)
