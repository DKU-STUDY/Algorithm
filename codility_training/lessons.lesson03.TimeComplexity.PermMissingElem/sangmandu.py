# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    sum = 0
    for a in A:
        sum +=  a
    n = len(A)
    return (n + 2) * ((n + 1) // 2) + (0 if n % 2 == 1 else  (n + 2) // 2) - sum

  '''
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

  return 4
  '''