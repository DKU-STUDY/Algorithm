import sys

res = 0
scores = [int(sys.stdin.readline()) for _ in range(5)]
for score in scores:
    res += 40 if score < 40 else score
print(res//5)