'''
링크 : https://programmers.co.kr/learn/courses/30/lessons/64061
문제 : 크레인 인형뽑기 게임
마침 어제 코드리뷰하면서 본 defaultdict와 deque를 이용할 수 있겠다 싶어서 바로 적용해본 문제
근데 만들고나니 popleft() 쓸 일이 없어 불필요해 보이긴 하네요 :|
'''

from collections import defaultdict, deque

def solution(board, moves):
    answer = 0
    dolls = defaultdict(list)
    
    # board의 인형을 위치별로 리스트로 묶었습니다.
    for i in board[::-1] :
        for j in range(len(board)) :
            if i[j] != 0 :
                dolls[j].append(i[j])
    
    # 바구니에 인형을 넣고, dolls에서 없애는 과정
    bucket = deque([-1])
    for i in moves :
        if dolls[i-1] :
            if bucket[-1] == dolls[i-1][-1] :
                bucket.pop()
                dolls[i-1].pop()
                answer += 2
            else :
                bucket.append(dolls[i-1].pop())
    return answer
