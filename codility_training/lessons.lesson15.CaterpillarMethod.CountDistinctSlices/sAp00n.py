def solution(M, A):
    slice_count = 0
    counter = {}
    for value in range(0, M + 1): counter[value] = 0
    print(counter)
    for i in range(len(A)):
        for j in range(i, len(A)):
            condition = True
            temp = counter.copy()
            print(f'range: A[{i}]:A[{j}]')
            for k in range(i, j + 1):
                temp[A[k]] += 1
                if temp[A[k]] >= 2:
                    condition = False
                    break
            if condition:
                slice_count += 1
            print(f'counter: {temp}\n')

    return slice_count


M = 6
A = [0]
print(solution(M, A))
