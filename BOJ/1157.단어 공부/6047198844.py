frequency = [0]*26
s = input().upper()
res = []
for _ in range(26):
    res.append(s.count(chr(_+ord('A'))))
print(chr(res.index(max(res))+ord('A'))) if res.count(max(res)) == 1 else print('?')