'''
https://programmers.co.kr/learn/courses/30/lessons/67258
보석 쇼핑
[풀이]
1. 난이도가 좀 있는 문제. 투 포인터를 사용할 것이라 예상까지는 했는데 풀이에 시간이 꽤 걸렸다.
=> 코드 자체가 어려운 편은 아니고, 방법을 생각하는 것이 어려움
2. 투 포인터 st, ed를 0으로 선언. 답으로 제출할 ast(answer st)와 aed(answer ed)는 전체 크기로 설정
3. dictionary cnt를 선언. => 첫번째 보석을 담고 있다. (st,가 0이기 때문)
4. 기본적인 작동원리 : 전체 보석 개수가 필요한 보석 개수보다
많으면 => st += 1
적으면 => ed += 1
5. ed - st값에 따라 ast와 aed를 갱신한다.
=> 이 때, ed - st < aed - ast 에서 부등호가 <= 가 아니라 < 여야 한다.
=> "만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다." 조건을 만족하기 위해서
6. 최종으로 구한 ast, aed에 +1 을 해서 반환
'''
def solution(gems):
    st = ed = 0
    ast, aed = 0, len(gems) - 1
    cnt = {gems[0]: 1}
    kinds = len(set(gems))

    while st < len(gems) and ed < len(gems):
        if len(cnt) == kinds:
            if ed - st < aed - ast:
                ast, aed = st, ed
            cnt[gems[st]] -= 1
            if cnt[gems[st]] == 0:
                del cnt[gems[st]]
            st += 1
        else:
            ed += 1
            if ed == len(gems):
                break
            cnt[gems[ed]] = cnt.get(gems[ed], 0) + 1

    return [ast + 1, aed + 1]
'''
보통 dictionary를 선언하는 이유는 특정 key에 대한 value를 찾을 때 O(1)의 시간이 들기 때문.
이 value값의 유무를 조사하기 위해 처음에는 list(cnt.values()).count() 를 사용했다.
이 부분이 시간이 많이 걸렸는데. del을 사용해서 값의 유무를 판단했고 시간을 줄였다.
왜냐하면 보석이 몇 개 인지가 중요한 것이 아니라 1개 이상인지 0개인지가 판단 근거이기 때문.
'''