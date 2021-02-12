# 출처 https://programmers.co.kr/learn/courses/30/lessons/12949
# input 2차원 행렬 arr1, arr2
# output 행렬 곱셈의 결과

def solution(arr1, arr2):
    answer = []
    for y1 in range(len(arr1)):
        temp_arr = []
        for x2 in range(len(arr2[0])):
            temp = 0
            for y2 in range(len(arr2)):
                temp += arr1[y1][y2] * arr2[y2][x2]
            temp_arr.append(temp)
        answer.append(temp_arr)
    return answer

print(
    solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]],
    solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]),
    solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == \
    [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
    solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
      )
