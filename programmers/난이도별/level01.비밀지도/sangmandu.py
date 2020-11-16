'''
https://programmers.co.kr/learn/courses/30/lessons/17681
비밀지도 : array의 원소는 어떤 이진수의 십진수. 이 이진수는 n*n에 대한 암호이며
두 개의 array를 합한 array는 최종 암호이다. 1은 #으로 0은 공백으로 표현
bin으로 이진수 치환. zip으로 바로 리스트화. re.sub으로 1과 0 대체
'''

import re
def solution(n, arr1, arr2):
    cipher = [bin(i | j)[-n:] for i, j in zip(arr1, arr2)]
    for i in range(len(cipher)):
        cipher[i] = re.sub('1','#',cipher[i])
        cipher[i] = re.sub('[0b]',' ',cipher[i])
    return cipher

'''
배울만한 풀이.
1) rjust 함수 => 오른쪽 정렬 후 해당 크기 만큼 문자열 생성, 빈 공간을 해당 문자로 치환
2) re.sub 대신 간단하게 replace 사용 가능
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''

'''
한줄 풀이
1) 문자열 포맷터를 이용 => int: {0:d}, bin: {0:b}, oct: {0:o}, hex: {0:x}".format(num)
2) 위 rjust와는 0으로만 채울 수 있는 점을 제외하고는 비슷.
=> str.zfill(n) : 해당 자리수가 되도록 앞에 0을 채움
return [''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))]
'''