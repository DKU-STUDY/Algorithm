# test case [5, 17, 0, 3], [0, 10, -5, -2, 0], [5, 5, 5] and all negative

def solution(A):
    print(f'A: {A}')
    n = len(A)
    left_sublist = []
    right_sublist = []
    maxsum = A[0]
    for i in range(n - 1):
        if i == 0:
            left_sublist.append(max(0, A[i]))
        else:
            left_sublist.append(max(0, left_sublist[i - 1] + A[i]))
        print(left_sublist)

    for i in range(n - 2, 1, -1):
        if i == 0:
            right_sublist.append(max(0, A[i]))
        else:
            right_sublist.append(max(0, right_sublist[i - 1] + A[i]))
        print(left_sublist)