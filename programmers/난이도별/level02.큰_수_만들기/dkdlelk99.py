def solution(number, k):
    number = list(map(int, number))  # number = [int(x) for x in number]
    answer=[]
    for i in range(len(number)):
        index_of_max_value = number.index(max(number[:k+1]))
        k -= index_of_max_value
        number = number[index_of_max_value:]
        if index_of_max_value == 0:
            answer.append(number.pop(0))
            continue
        answer.append(number.pop(0))

        if k == 0:
            return "".join(map(str, answer + number))

    return "".join(map(str, answer + number))

print(solution("314161592",5))
