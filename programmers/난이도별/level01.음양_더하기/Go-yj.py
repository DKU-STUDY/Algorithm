'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/76501
문제 : 음양 더하기
예전에 상민오빠 코드 리뷰할 때 알게된 zip을 활용해보네요
덕분에 두개의 배열을 바로 연산하기 편하더라구요!!!
'''

def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs) :
        if not sign : absolute *= -1
        answer += absolute
    return answer
