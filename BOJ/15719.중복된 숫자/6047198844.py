import sys

N = int(sys.stdin.readline())
numbers = sys.stdin.readline()
sum = 0
temp = ""
for num in numbers:
    if num.isdigit():
        temp += num
    elif num == " ":
        sum += int(temp)
        temp = ""
sum += int(temp)
print(sum - N * (N - 1) // 2)