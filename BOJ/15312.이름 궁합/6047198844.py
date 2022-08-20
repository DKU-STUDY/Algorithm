A = input()
B = input()
score = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name = ''
for i in range(len(A)):
    name += A[i] + B[i]

res = ''
for word in name:
    idx = ord(word) - ord('A')
    res += str(score[idx])

while len(res) != 2:
    tmp = ''
    for i in range(len(res)-1):
        tmp += str((int(res[i]) + int(res[i+1]))%10)
    res = tmp
print(res)