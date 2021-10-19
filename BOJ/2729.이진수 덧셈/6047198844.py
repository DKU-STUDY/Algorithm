T = int(input())

for _ in range(T):
    A, B = input()[::-1].split()
    acc = ['0']
    for idx in range(max(len(A), len(B))):
        cur = int(acc[idx])
        if idx < len(A):
            cur += int(A[idx])
        if idx < len(B):
            cur += int(B[idx])
        acc[idx] = str(cur % 2)
        acc.append(str(cur // 2))

    while len(acc) > 1 and acc[-1] == '0':
        acc.pop()
    print(''.join(acc[::-1]))
