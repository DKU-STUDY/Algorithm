moem = ['a', 'e', 'i', 'o', 'u']
while True:
    line = input()
    if line == 'end':
        break

    moem_cnt = 0
    jaem_cnt = 0
    for i in range(len(line)):
        if i > 1 and line[i] == line[i-1] and not (line[i] == 'e' or line[i] == 'o'):
            print(f'<{line}> is not acceptable')
            break
        if line[i] in moem:
            moem_cnt += 1
            jaem_cnt = 0
        else:
            moem_cnt = 0
            jaem_cnt += 1

        if moem_cnt == 3 or jaem_cnt == 3:
            print(f'<{line}> is not acceptable')
            break
    else:
        for m in moem:
            if m in line:
                print(f'<{line}> is acceptable')
                break
        else:
            print(f'<{line}> is not acceptable')