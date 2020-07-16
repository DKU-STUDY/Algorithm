# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    pass
    return (0 if (Y-X)%D == 0 else 1) + ((Y-X)//D if X < Y else 0)

'''
 X = 10
 Y = 85
 D = 30

 return 3
 '''