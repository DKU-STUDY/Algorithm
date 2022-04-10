n = int(input())

res = -1
five = 0
while five * 5 <= n:
    if (n - five * 5) % 2 == 0:
        res = five + (n - five * 5) // 2
    five += 1
print(res)