from collections import deque

res = deque('UCPC')
str = input()
for char in str:
    if not res:
        break
    if char == res[0]:
        res.popleft()

if res:
    print("I hate UCPC")
else:
    print("I love UCPC")
