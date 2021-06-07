'''
https://programmers.co.kr/learn/courses/30/lessons/43105
정수 삼각형
[풀이]
1. 왼쪽과 오른쪽은 각각 삼각형의 테두리선의 합으로 정의
2. 나머지 원소는 왼쪽 위와 왼쪽 오른 쪽중 더 큰 값을 더하기
3. 최종 층에서는 모든 경우의 수가 더해진 것 중에 큰 것들만 모인 것. 이중에 최대를 반환.
'''
def solution(triangle):
    tri = triangle
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][0] += tri[i - 1][0]
            elif j == len(tri[i]) - 1:
                tri[i][-1] += tri[i - 1][-1]
            else:
                tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

    return max(tri[-1])


'''
[한줄코드 분석]
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
1. solution은 t와 l로 이루어진 함수
=> t는 triangle, l은 빈 리스트임
2. t가 존재하지 않으면 max(l)을 반환
3. t가 존재하면 t = t[1:], l = [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])] 를 다시 호출
=> 재귀적 함수를 구현했다.
t = t[1:] => 삼각형의 다음 층에대해 조사 => 언젠가는 다음 층이 없으므로 이 때 max(l)을 반환
4. l = [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])]
=> l은 처음 층에서 빈 리스트이기 때문에 [max(x,y)+z for x,y,z in zip([0], [0], t[0])] 가 계산됨
=> 다음층으로 건네주는 l은 t[0]가 된다.
=> 그 다음층으로 건네주는 l은 t[0]가 더해진 t[1]이 된다
5. 두번째 층 [3,8]을 기준으로 zip을 보면 다음과 같이 된다.
=> zip([0, 7], [7, 0], [3,8])
6. 따라서 x, y, z는 다음과 같은 순서쌍을 가진다
(0, 7, 3) => max(0, 3) + 7
(7, 0, 8) => max(7, 0) + 8
=> 이 부분이 가장 핵심적인 부분. 한줄로 구현할 때 제일 많이 고민해야 하는 부분이다.
=> 전 층에서 다음층으로 넘어갈 때 더 큰 쪽을 넘겨줘야 하는 부분을 구현하면서,
양 끝에 있는 부분도 if조건없이 한번에 할 수 있도록 [0] 리스트를 더해주는 스킬
'''