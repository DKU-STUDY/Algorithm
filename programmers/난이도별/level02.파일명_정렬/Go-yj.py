'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/17686#
문제 : [3차] 파일명 정렬
dictonary의 value에 HEAD와 NUMBER를 분리해서 리스트로 넣고 value를 기준으로 정렬해 주었습니다.
정렬 후 key의 순서에 따라 files 값을 return 하였습니다.
정규식 사용할 생각은 전혀 하지 못했는데 다들 정규식을 사용하더라구요
문자가 나오면 무조건 re 사용하는게 편하다는 말을 또 잊어버리고 있었어요
정규식 계속 까먹어서 정규식 문제 나올때마다 링크 다시 가서 보고 중...
[메모]
import re
a = sorted(files, key=lambda x:int(re.findall('\d+',x)[0]))
b = sorted(a, key=lambda x:re.split('\d+',x.lower())[0])
'''

def solution(files):
    answer = []
    dic = {}
    for i in range(len(files)) :
        temp = list(files[i])
        ishead = True
        HEAD, NUMBER = '',''
        for j in temp :
            if not j.isdigit() and ishead :
                HEAD += j
            elif j.isdigit() :
                ishead = False
                NUMBER += j
            else : break
        dic[i] = [HEAD.lower()]
        dic[i].append(int(NUMBER))
    
    dic = sorted(dic.items(), key=lambda x:x[1])
    
    for i in range(len(dic)) :
        answer.append(files[dic[i][0]])
    return answer
