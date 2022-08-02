from collections import Counter

for _ in range(3):
    s = input().split()
    zero_cnt = Counter(s).get('0')

    if zero_cnt == 1:
        print('A')
    elif zero_cnt == 2:
        print('B')
    elif zero_cnt == 3:
        print('C')
    elif zero_cnt == 4:
        print('D')
    elif zero_cnt == None:
        print('E')
