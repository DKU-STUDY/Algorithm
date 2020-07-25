a, b = map(int, input().strip().split(' '))
for x in range(b):
    for y in range(a):
        print('*', end = '')
    print('', end = "\n")