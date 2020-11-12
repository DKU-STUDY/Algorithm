'''
https://programmers.co.kr/learn/courses/30/lessons/70128
조이스틱: 게임 기록 세웠을 때 자신의 이름을 등록하기 위해 레버를 움직여야 하는 횟수
진짜 어려웠던 문제. 구현하고 나니 쉬운 감이 있다.
풀이 방법
1) 각 자리에서 알파벳을 변경할 때의 횟수는 cnt에 한번에 생성
2) index 0에서 오른쪽과 왼쪽을 선택했을 때의 최소 횟수는 idx[-1], len(name) - idx[1]
3) idx 0에서 idx -1로만 이동이 가능한데, idx가 len(name) // 2 전에서 역행을 해야 최소 횟수 확보 가능
4) idx가 len(name) // 2 보다 작으면서 'A'가 아닐 때 idx 0 과의 거리 * 2 + 남은 거리를 통해 최종 비교
'''

def solution(name):
    cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']
    idx = [i for i, v in enumerate(name) if v != 'A']

    graph = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [len(name) - idx[-1]]
    if name[0] == 'A':
        idx = [0] + idx
        graph = [idx[1]] + graph

    answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + [
        idx[-1], len(name) - idx[1]]
    return sum(cnt) + min(answer)


'''
참고로 이 문제는 현재 잘못되었다.
"BABAAAAB" 와 같은 예제에 대해서 결과 8을 출력해야 하는데 9를 출력한다.
이 문제의 채점 코드에서는 역행하는 경우의 수를 고려하지 않았다.
따라서 현재 인덱스에서 최단 거리만 방문해서 풀 수 있도록 설계해놓았다.

실제로는, 다익스트라 알고리즘이 적용되지 않는다.
따라서, 최단 거리만 방문해서는 문제를 풀 수 없다.

하지만 풀리는 이상한 문제...
'''