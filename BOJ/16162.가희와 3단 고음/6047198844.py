N, A, D = map(int, input().split())
melodies = list(map(int, input().split()))

res = 0
cur = A

for melody in melodies:
    if cur == melody:
        cur += D
        res += 1

print(res)