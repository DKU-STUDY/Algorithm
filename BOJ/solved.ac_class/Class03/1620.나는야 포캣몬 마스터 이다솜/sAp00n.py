from sys import stdin


i, j = map(int, stdin.readline().split())
name2_num = {}
num2_name = {}
for num in range(1, i+1):
    number = str(num)
    name = stdin.readline().strip('\n')
    name2_num[name] = number
    num2_name[number] = name

#print(name2_num)
#print(num2_name)
for case in range(j):
    input_str = stdin.readline().strip('\n')
    if input_str in num2_name:
        print(num2_name[input_str])
    else:
        print(name2_num[input_str])
