'''
https://programmers.co.kr/learn/courses/30/lessons/17683
방금그곡
replace로 대문자#을 소문자로 변경.
'''

def solution(m, musicinfos):
    m = m.replace('C#', 'c')
        .replace('D#','d')
        .replace('F#','f')
        .replace('G#','g')
        .replace('A#','a')
    answer = []
    for i in musicinfos:
        start, end, title, score = i.split(',')
        time = (int(end[:2])-int(start[:2])) * 60 + int(end[3:])-int(start[3:])
        score = score.replace('C#', 'c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        score = score * (time // len(score)) + score[:time%len(score)]
        if score.find(m) != -1:
            answer.append([title,time])
    return sorted(answer, key=lambda x : -x[1])[0][0] if answer else "(None)"

'''
replace를 계속 쓰는게 맘에 안들었는데, 다른 사람들도 별 방법이 없었나보다.
억지로 re를 쓰거나 함수를 만드는 것보다는 깔끔한 듯 싶다.
'''
