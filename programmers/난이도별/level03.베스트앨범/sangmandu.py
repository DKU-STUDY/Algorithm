'''
https://programmers.co.kr/learn/courses/30/lessons/42579
베스트앨범
딕셔너리로 해시 기능 이용. 수가 많은 장르와 각 장르별 순위를 매기기 위해 두 가지 딕셔너리 사용
'''

def solution(genres, plays):
    rank, chart = {}, {}
    for idx, val in enumerate(zip(genres, plays)):
        a, b = val[0], val[1]
        rank.setdefault(a, 0)
        rank[a] += b
        chart.setdefault(a, [])
        chart[a].append((idx, b))
    best = sorted(rank.items(), key=lambda x : x[1], reverse=True)
    answer = []
    for i in best:
        answer.extend(sorted(chart[i[0]], key=lambda x : (-x[1], x[0]))[:2])
    return [a[0] for a in answer]


'''
'''