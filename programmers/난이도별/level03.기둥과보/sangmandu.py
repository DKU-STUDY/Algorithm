'''
https://programmers.co.kr/learn/courses/30/lessons/60061
기둥과 보 설치
구조물 상태를 매번 갱신
삽입 삭제시에 구조물 규칙 검사
'''

def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:  # 기둥일 때
            if y != 0 and (x, y - 1, COL) not in result and \
                    (x - 1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else:  # 보일 때
            if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and \
                    not ((x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

'''
https://velog.io/@tjdud0123/기둥과-보-설치-2020-카카오-공채-python 참고
너무 많은 if문과 30점 이하의 정확성 때문에 현타.
이렇게 푸는 것이 아니라 확신했는데, 멋지게 푸는 사람 발견.
보통 이런 문제를 풀면 전체적인 board를 만들기 마련인데,
이렇게 풀 수도 있다는 것을 알았다
'''