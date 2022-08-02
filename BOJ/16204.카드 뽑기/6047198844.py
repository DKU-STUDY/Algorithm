# M개 O가 1개
# N-M X가 1개
import sys

N, M, K = map(int, sys.stdin.readline().split())

o_num = M
x_num = N - M

o_write = K
x_write = N - K
print(min(o_num, o_write) + min(x_num, x_write))
