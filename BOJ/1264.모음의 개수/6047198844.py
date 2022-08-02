while True:
    s = input()
    if s == '#':
        break

    cnt = 0
    for i in 'a','A','e','E','i','I','o','O','u','U':
        cnt += s.count(i)
    print(cnt)