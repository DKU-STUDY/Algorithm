table = dict()
table['0'] = 'zero'
table['1'] = 'one'
table['2'] = 'two'
table['3'] = 'three'
table['4'] = 'four'
table['5'] = 'five'
table['6'] = 'six'
table['7'] = 'seven'
table['8'] = 'eight'
table['9'] = 'nine'

table['zero'] = '0'
table['one'] = '1'
table['two'] = '2'
table['three'] = '3'
table['four'] = '4'
table['five'] = '5'
table['six'] = '6'
table['seven'] = '7'
table['eight'] = '8'
table['nine'] = '9'

M, N = map(int, input().split())
alphanum_list = list()
for i in range(M, N + 1):
    alphanum = ' '.join(map(table.get, list(str(i))))
    alphanum_list.append(alphanum)
alphanum_list.sort()
numeric_list = list()
for alphanum in alphanum_list:
    numeric = ''.join(map(table.get, alphanum.split(' ')))
    numeric_list.append(numeric)

for start_idx in range(0, len(numeric_list), 10):
    for numeric in numeric_list[start_idx:start_idx+10]:
        print(numeric, end=' ')
    print()
