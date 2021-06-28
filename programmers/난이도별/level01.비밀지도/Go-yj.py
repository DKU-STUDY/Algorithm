'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/17681
문제 : [1차] 비밀지도
비트 연산자를 사용해서 arr1과 arr2를 or연산한 후 2진수로 바꿔줬습니다.
zfill 함수를 사용해서 앞의 여백을 0으로 채워 5글자로 만들고
1을 #으로 0을 ' '로 바꿔주었습니다.
'''

def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        binary = bin(arr1[i]|arr2[i])[2:].zfill(n)
        cipher = binary.replace('1','#')
        cipher = cipher.replace('0',' ')
        answer.append(cipher)
    return answer
