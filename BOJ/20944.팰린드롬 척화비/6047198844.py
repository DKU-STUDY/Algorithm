N = int(input())
if N % 2 == 0:
    print('a'*N)
else:
    print('a'*(N//2) + 'b' + 'a'*(N//2))