'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/12951#
문제 : JadenCase 문자열 만들기
처음에는 s = [x[0].upper()+x[1:] for x in s]로 풀었는데
공백이 여러개일 때 에러가 발생해서 try, except 문을 사용해줬습니다.
예전에 level01에서도 공백 때문에 성가신 문제가 있었는데
여러 케이스를 잘 고려해야 되겠네요
'''

def solution(s):
    s = s.lower().split(' ')
    for i in range(len(s)) :
        try :
            s[i] = s[i][0].upper()+s[i][1:]
        except :
            continue
    return ' '.join(s)
