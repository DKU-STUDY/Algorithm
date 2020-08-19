from sys import stdin


def gdc(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a


a, b = list(map(int, stdin.readline().split()))
gdc_num = gdc(a, b)
print(gdc_num)
print(int((a * b)/gdc_num))

