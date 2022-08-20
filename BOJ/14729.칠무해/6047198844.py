import sys

N = int(sys.stdin.readline())
students = [float(sys.stdin.readline()) for _ in range(N)]
students.sort()
for i in range(7):
    print(format(students[i], ".3f"))