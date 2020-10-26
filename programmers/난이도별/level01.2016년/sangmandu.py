#https://programmers.co.kr/learn/courses/30/lessons/12901
# 2016년 a월 b일의 요일 구하기
# datetime 사용

import datetime
def solution(a, b):
    answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return answer[datetime.datetime(2016, a, b).weekday()]

'''
library 사용이 안되었다면 다음과 같이 푸는게 best인 듯
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
'''