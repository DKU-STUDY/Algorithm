numbers = map(int, input().split())
cnt = 0
for number in numbers:
    cnt += number**2
print(cnt % 10)