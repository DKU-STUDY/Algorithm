from sys import stdin

T = int(stdin.readline())

for cases in range(T):
    result = stdin.readline()
    score = 0
    temp = 0
    for idx in range(len(result)):
        if result[idx] == 'O':
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
