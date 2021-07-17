'''
https://programmers.co.kr/learn/courses/30/lessons/12969
직사각형 별찍기
[풀이]
1. 반복문으로 생성된 list를 join. 이를 중첩
'''
a, b = map(int, input().strip().split(' '))
print(('*'*a +'\n')*b)
'''
'''