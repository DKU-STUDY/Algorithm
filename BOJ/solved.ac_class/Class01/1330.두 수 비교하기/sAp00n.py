import sys
input_list = sys.stdin.readline().split()
A, B = (int(ele) for ele in input_list)

if A > B: print('>')
elif A < B: print('<')
else: print('==')
