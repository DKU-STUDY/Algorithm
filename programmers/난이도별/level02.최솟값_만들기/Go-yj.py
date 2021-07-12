'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12941
문제 : 최솟값 만들기
곱의 최솟값을 구하려면 제일 작은수와 제일 큰 수의 곱의 합으로 이루어져야 합니다.
그래서 하나는 오름차순, 하나는 내림차순으로 정렬하여 곱해주었습니다.
다른 사람들 풀이를 보니 zip을 사용하면 한줄로 간편하게 할 수 있더라구요
zip 진짜 편리하네요
[메모]
sum(a*b for a,b in zip(sorted(A), sorted(B,reverse=True)))
'''

def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)) :
        answer += A[i]*B[i]
    return answer
