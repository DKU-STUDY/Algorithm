def solution (arr):
    f([], arr, len(arr))

def f (stack, arr, last):
    if len(stack) == last:
        print(stack)
        return

    for v in arr:
        if not v in stack:
            f(stack[:] + [v], arr, last)

solution([ 1, 2, 3 ])
# answer
# [ 1, 2, 3 ]
# [ 1, 3, 2 ]
# [ 2, 1, 3 ]
# [ 2, 3, 1 ]
# [ 3, 1, 2 ]
# [ 3, 2, 1 ]