'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12922
문제 : 수박수박수박수박수박수?
저는 리스트를 만들어 n 수만큼 반복해서 넣어줬는데
다른 사람들 풀이를 보니 굳이 리스트를 만들지 않고
문자열 그대로 n 수만큼 곱해서 넣어주면 되더라구요
[메모]
"".join(["수박"[i%2] for i in range(n)])
'''

def solution(n):
    answer = ''
    s = ['수','박']
    for i in range (n) :
        answer += s[i%2]
    return answer
