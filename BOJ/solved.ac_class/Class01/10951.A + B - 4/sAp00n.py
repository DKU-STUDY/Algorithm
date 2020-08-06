from sys import stdin

input_str = stdin.readlines()
input_str = [string.rstrip('\n') for string in input_str]

input_num_couple = [couples.split() for couples in input_str]
for idx in range(len(input_num_couple)): input_num_couple[idx] = [int(numbers) for numbers in input_num_couple[idx]]

for i in input_num_couple:
    print(i[0] + i[1])