def solution(array, commands):
    result = []
    for v in commands:
        i, j, k = v
        temp = array[i-1:j]
        temp.sort()
        result.append(temp[k-1])
    return result


a = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
b =	[1, 5, 2, 6, 3, 7, 4]

print(solution(b,a))