def solution(answers):
    student = [0, 0, 0]
    check = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i, n in enumerate(answers):
        for m in range(len(student)):
            if check[m][i % len(check[m])] == n:
                student[m] += 1

    return [s + 1 for s in range(len(student)) if student[s] == max(student)]

print(solution([1,2,3,4,5]) == [1])
print(solution([1,3,2,4,2]) == [1,2,3])