'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12909
문제 : 올바른 괄호
'(' 개수와 ')' 개수를 세서 비교하였습니다.
다른 사람 풀이를 보니 0에서부터 시작해서 '('면 +1, ')'면 -1을 해서
-가 될 때와 최종 결과가 0이 아닐 때 FALSE를 return 하면
변수를 한 개만 만들어도 되고 '('와 ')'의 개수가 같은지도 추가로 비교하지 않아도 되더라구요
'''

def solution(s):
    answer = True
    if s.count('(') != s.count(')') : return False
    s = list(s)
    open_count, close_count = 0,0
    for i in s :
        if close_count > open_count : return False
        if i == '(' : open_count += 1
        else : close_count += 1
    return True
