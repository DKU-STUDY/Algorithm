#col : x
'''
0123
0123
0123
0123
'''

#row : y
'''
0000
1111
2222
3333
'''
#ldiag : y + x
'''
0123
1234
2345
3456
'''
#rdiag : y + (n-x-1)
'''
3210
4321
5432
6543
'''
N = int(input())
col = set()
#row = set()
ldiag = set()
rdiag = set()

def dfs(y:int)->int:
    if y == N:
        return 1

    res = 0
    for x in range(0, N):
        if x not in col and y + x not in ldiag and y + (N-x-1) not in rdiag:
            col.add(x)
            ldiag.add(y + x)
            rdiag.add(y + N - x - 1)
            res += dfs(y+1)
            col.remove(x)
            ldiag.remove(y + x)
            rdiag.remove(y + N - x - 1)
    return res

print(dfs(0))