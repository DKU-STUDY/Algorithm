n = int(input())
res = n % 8
if res == 1:
    print(1)
elif res == 2 or res == 0:
    print(2)
elif res == 3 or res == 7:
    print(3)
elif res == 4 or res == 6:
    print(4)
else:
    print(5)