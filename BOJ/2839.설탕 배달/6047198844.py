N = int(input())
three = 0
five = 0
while N % 5 and N >= 0:
    N -= 3
    three += 1
five = N // 5
print(-1) if N < 0 else print(three + five)