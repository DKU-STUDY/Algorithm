attendance_numbers = set(range(1, 31))
for _ in range(28):
    attendance_numbers.remove(int(input()))
for absent in sorted(attendance_numbers):
    print(absent)