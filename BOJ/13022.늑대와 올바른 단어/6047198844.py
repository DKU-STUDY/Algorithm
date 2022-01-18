from itertools import permutations

wolfs = ['w' * i + 'o' * i + 'l' * i + 'f' * i for i in range(1, 12 + 1)]
table = dict()
for idx, wolf in enumerate(wolfs):
    table[idx+1] = wolf

word = input()
start_idx = 0

while start_idx < len(word):
    for wolf in wolfs:
        if word[start_idx:].startswith(wolf):
            start_idx += len(wolf)
            break
    else:
        print(0)
        exit()
print(1)
