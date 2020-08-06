import sys
mush_list = []
temp = 0

for _ in range(10): mush_list += [int(sys.stdin.readline())]
'''from random import randint
mush_list = []
temp = 0
for _ in range(10): mush_list += [randint(0,100)]
print(f'mush_list = {mush_list}')'''
score = 0
i = 0

for idx in range(10):
    if score + mush_list[idx] > 100:
        break
    score += mush_list[idx]
    i += 1
if i < 10:
    temp = score + mush_list[idx]
#print(f'i : {i}')
#print(f'score = {score} diff form 100 = {abs(100 - score)} \ntemp = {temp} diff from 100 = {abs(100 - temp)}')
if abs(100 - score) == abs(100 -temp):
    print(temp)

elif abs(100 - score) > abs(100 - temp):
    print(temp)
else:
    print(score)
