'''
https://programmers.co.kr/learn/courses/30/lessons/64604
불량 사용자
[풀이]
1. 문자열 문제는 항상 re가 최고다. 시간 단축과 구현 편의에 필수
=> 정규 표현식으로 불량 사용자에 해당아는 유저 아이디를 검출한다
2. 각 불량사용자마다 얻은 유저들의 아이디를 result에 모은다
3. result에있는 아이디로 구성할 수 있는 조합을 만든다.
=> 이 때 중복순열인 product를 사용한다.
=> 이를 사용하지 않으려면 while문과 리스트 연산을 해야하는데 이게 피곤하다
4. 만들어진 조합을 가지고 조건을 추려서 결과를 얻는다
=> 이 조건은 코드 아래에 다시 명시하겠음
'''
import re
from itertools import product
def solution(user_id, banned_id):
    result = []
    for ban in banned_id:
        ban = ban.replace('*', '.')
        banned = [user for user in user_id if re.fullmatch(ban, user)]
        result.append(banned)

    answer = set([tuple(sorted(set(i))) for i in product(*result) if len(set(i)) == len(banned_id)])
    return len(answer)
'''
다음은 prodcut(*result)가 변환하는 과정.

입력값 〉	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
기댓값 〉	2
    # 모든 경우의 수를 구한다
    print([i for i in product(*result)])
    	[('frodo', 'frodo', 'abc123'), ('frodo', 'frodo', 'frodoc'), ('frodo', 'crodo', 'abc123'), ('frodo', 'crodo', 'frodoc'), ('crodo', 'frodo', 'abc123'), ('crodo', 'frodo', 'frodoc'), ('crodo', 'crodo', 'abc123'), ('crodo', 'crodo', 'frodoc')]
    
    # 중복되는 경우의 수를 제거한다
    print([set(i) for i in product(*result)])
        [{'abc123', 'frodo'}, {'frodo', 'frodoc'}, {'abc123', 'crodo', 'frodo'}, {'crodo', 'frodo', 'frodoc'}, {'abc123', 'crodo', 'frodo'}, {'crodo', 'frodo', 'frodoc'}, {'abc123', 'crodo'}, {'crodo', 'frodoc'}]
    
    # 문제 조건에 "불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다." 라는 조건이 있다.
    # 따라서, 불량 아이디는 무조건 하나의 아이디와 대응되기 때문에 불량 아이디의 개수와 경우의 수의 개수가 동일해야 한다.
    # 그리고 여기서 이 if문을 미리 해야한다. 다음에 나오는 sorted() 이후에 조건이 달리면 시간초과가 뜬다. => 테스트케이스 5
    print([set(i) for i in product(*result) if len(set(i)) == len(banned_id)])
        [{'abc123', 'crodo', 'frodo'}, {'crodo', 'frodo', 'frodoc'}, {'abc123', 'crodo', 'frodo'}, {'crodo', 'frodo', 'frodoc'}]
    
    # [a, b, c] 와 [b, a, c] 를 중복으로 판단하기 위해 정렬을 한다
    print([sorted(set(i)) for i in product(*result) if len(set(i)) == len(banned_id)])
        [['abc123', 'crodo', 'frodo'], ['crodo', 'frodo', 'frodoc'], ['abc123', 'crodo', 'frodo'], ['crodo', 'frodo', 'frodoc']]
    
    # set이 중복을 제거할 수 있는 타입은 '문자', '숫자' 그리고 '튜플' 뿐이다.
    # sorted() 된 대상은 리스트이다.
    # 따라서, tuple 형태로 변환한다.
    print([tuple(sorted(set(i)) for i in product(*result) if len(set(i)) == len(banned_id))])
        [(['abc123', 'crodo', 'frodo'], ['crodo', 'frodo', 'frodoc'], ['abc123', 'crodo', 'frodo'], ['crodo', 'frodo', 'frodoc'])]
    
    # 이후 set()을 이용해 중복을 제거한다.
    print(set([tuple(sorted(set(i))) for i in product(*result) if len(set(i)) == len(banned_id)]))
        {('crodo', 'frodo', 'frodoc'), ('abc123', 'crodo', 'frodo')}
'''