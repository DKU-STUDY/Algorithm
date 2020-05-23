def solution(A, B):
    # write your code in Python 3.6
    print(f'A: {A}      B:{B}')
    fish_stack = []
    n = len(B)
    for i in range(n):
        if len(fish_stack) == 0:
            fish_stack.append((B[i], A[i]))

        else:
            if fish_stack[-1][0] == 0:
                fish_stack.append((B[i], A[i]))
            else:
                if B[i] == 1:
                    fish_stack.append((B[i], A[i]))
                elif A[i] > fish_stack[-1][-1]:
                    fish_eat_func(fish_stack,B[i], A[i])
        print(fish_stack)
    return len(fish_stack)


def fish_eat_func(fish_stack, Bi, Ai):
    if len(fish_stack) == 0:
        fish_stack.append((Bi, Ai))
        return
    while fish_stack[-1][0] != Bi and Ai > fish_stack[-1][-1]:
        fish_stack.pop()
        if len(fish_stack) == 0:
            fish_stack.append((Bi, Ai))
            return

    if fish_stack[-1][0] == Bi:
        fish_stack.append((Bi, Ai))
        return
    else:
        return