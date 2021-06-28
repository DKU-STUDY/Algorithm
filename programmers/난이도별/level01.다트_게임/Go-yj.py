'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/17682
문제 : 다트 게임
10점짜리를 list로 쪼갰을 때 1,0으로 구분하지 않도록
십으로 바꿔준 후 한글자씩 쪼갰습니다.
그 후 score에 점수 넣고 조건별로 계산하도록 했습니다.
다른 사람 풀이 보고 덕분에 정규식 공부하긴 했는데
다른 문제 풀 때 정규식을 적용시킬 수 있을런지 ￣▽￣;;
'''

def solution(dartResult):
    score = []
    pow_score = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    if '10' in dartResult : 
        dartResult = dartResult.replace('10','십')
    answer = list(dartResult)
    for i in answer :
        if i.isdigit() : 
            score.append(int(i))
        elif i == '십' :
            score.append(10)
        elif i in pow_score :
            score[-1] = pow(score[-1],pow_score[i])
        elif i == '*' :
            score[-1] *= 2
            if len(score) >= 2 :
                score[-2] *= 2
        else :
            score[-1] *= -1
    return sum(score)
