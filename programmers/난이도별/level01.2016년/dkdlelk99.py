import datetime

def solution(a, b):
    time_1 = datetime.datetime(2016,1,1)
    time_2 = datetime.datetime(2016,a,b)
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return week[(((time_2 - time_1).days))%7]
    
print(solution(5,24) == 'TUE')
print(solution(7,30) == 'SAT')
