import sys

ul = list(map(int, sys.stdin.readline().split()))
st = list(map(int, sys.stdin.readline().split()))

ul_res = 0
st_res = 0
for i in range(9):
    ul_res += ul[i]
    if ul_res > st_res:
        print('Yes')
        exit()
    st_res += st[i]
print('No')
