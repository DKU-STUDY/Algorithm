from sys import stdin


def gdc(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
    while b > 0:
        c = b
        b = a % b
        a = c
    return a


a, b = list(map(int, stdin.readline().split()))
gdc_num = gdc(a, b)
print(gdc_num)
print(int((a * b)/gdc_num))

