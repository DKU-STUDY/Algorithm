word = input()
res = list()
for i in range(1, len(word) - 1):
    for j in range(1, len(word) - i):
        k = len(word) - i - j
        res.append(word[:i][::-1] + word[i:i+j][::-1] + word[i+j:i+j+k][::-1])
res.sort()
print(res[0])