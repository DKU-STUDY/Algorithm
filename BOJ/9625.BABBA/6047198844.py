commands = 'A'

K = int(input())
for _ in range(K):
    tmp = ''
    for command in commands:
        if command == 'A':
            tmp += 'B'
        else:
            tmp += 'BA'
    commands = tmp

a_cnt = commands.count('A')
print(a_cnt, len(commands) - a_cnt)