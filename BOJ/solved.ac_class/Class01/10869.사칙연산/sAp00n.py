import sys

input_list = sys.stdin.readline().split()
A, B = (int(ele) for ele in input_list)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
