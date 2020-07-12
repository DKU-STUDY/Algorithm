from random import randint

def solution(n):
    binary = []
    while(n // 2 != 0):
        if(n % 2 == 1):
            binary.append(1)
        else:
            binary.append(0)
        n = n // 2
    binary.append(1)
    
    index = []
    for x, y in enumerate(binary):
        if(y == 1):
            index.append(x)

    max = 0
    for i in range(len(index)-1):
        temp = index[i+1] - index[i] - 1
        if(max < temp):
            max = temp

    return max

n = randint(1, 2147483647)
solution(n)























