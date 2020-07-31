from sys import stdin
input_list = [int(stdin.readline()) for _ in range(9)]

max_val = max(input_list)
max_val_idx = input_list.index(max_val)

print(f'{max_val}\n{max_val_idx+1}')
