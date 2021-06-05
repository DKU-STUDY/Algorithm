'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12969
문제 : 직사각형 별찍기
중첩 for문을 이용하여 *을 찍었습니다.
다른 사람들의 코드를 참고하니 한 줄로도 가능하더라구요
메모메모 : print(("*"*a + "\n")*b)
'''

a, b = map(int, input().strip().split(' '))
for i in range(0,b) :
    for j in range(0,a) :
        print('*', end='')
    print()
