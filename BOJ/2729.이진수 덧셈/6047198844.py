T = int(input())
res = '0'
for _ in range(T):
    A, B = input().split()
    A, B = A[::-1], B[::-1]
    acc = '0'
    for idx in range(max(len(A), len(B))):
        tmp = int(res[idx])
        if idx < len(A):
            tmp += int(A[idx])
        if idx < len(B):
            tmp += int(B[idx])
        res[idx] = str(tmp % 2)
        res += str(tmp // 2)

    print(res)