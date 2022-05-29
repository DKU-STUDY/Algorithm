from _curses import endwin

arr = sorted(list(map(int, input().split())))
for i in arr:
    print(i, end=' ')