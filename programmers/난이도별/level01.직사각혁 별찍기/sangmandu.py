'''
https://programmers.co.kr/learn/courses/30/lessons/12969
직사각형 별찍기
반복문으로 생성된 list를 join. 이를 중첩
'''

a, b = map(int, input().strip().split(' '))
print(('*'*a +'\n')*b)

'''
이 문제는 이제까지 중 굉장히 멍청하게 푼 문제 중 하나.
처음에는
print(''.join([''.join(["*" for _ in range(a)]+["\n"]) for _ in range(b)]))
처럼 풀음

...???
'''