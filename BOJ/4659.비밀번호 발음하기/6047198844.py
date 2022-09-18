moem = ['a', 'e', 'i', 'o', 'u']
while True:
    line = input()
    moem_cnt = 0
    jaem_cnt = 0
    for i in range(len(line) - 1):
        if line[i] == line[i+1] and (line[i] != 'e' or line[i] != 'o'):
            break
        if line[i] in moem:
            moem_cnt += 1
            jaem_cnt = 0
        else:
            moem_cnt = 1
            jaem_cnt += 0
