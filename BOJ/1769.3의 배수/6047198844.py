X = input()
cnt = 0
while len(X) > 1:
    X = str(sum(map(int, X)))
    cnt += 1
print(cnt)
if X == '3' or X == '6' or X == '9':
    print('YES')
else:
    print('NO')
