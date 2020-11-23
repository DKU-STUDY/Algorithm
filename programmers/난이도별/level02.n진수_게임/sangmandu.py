'''
https://programmers.co.kr/learn/courses/30/lessons/17687
N진수 게임: 수학벌레들의 미친게임
미리 진수를 모두 구해놓은 뒤 해당 리스트에서 적절한 인덱스만 고른다.
'''

from itertools import product
def solution(n, t, m, p):
    size = 2
    txt = [i for i in range(n)]
    while len(txt) < t * m:
        tmp = [i for i in product(range(n), repeat = size)][n**(size-1):]
        txt.extend([j for i in tmp for j in i])
        size += 1
    order = 0
    dic = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'][:n]
    answer = ''.join(map(str, [dic[txt[i*m+p-1]%n] for i in range(t)]))
    return answer

'''
나도 이 함수 쓰고 싶었는데, 시간 초과 났다.
def convert(n, base):
    T = "0123456789ABCDEF"

    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
다른 사람들은 다 쓰네. 억울하다!
아마도 모든 수에대해 사용하는 것이 아니라, 자릿수가 바뀌기 전까지 사용해야 됐던 것 같다.
또는 내가 풀었듯이 미리 구해 놓는게 하나의 방법이었던 것 같다.
다음은 convert를 사용해서 미리 구해놓고 풀이

def convert(m,n):
    total = "0123456789ABCDEF"
    i,j = divmod(m,n)
    if i ==0:
        return total[j]
    else : 
        return convert(i,n)+total[j]

def solution(n, t, m, p):
    total = ''
    answer=''
    for i in range(t*m):
        total+=convert(i,n)
    for i in range(t):
        idx = p-1 + i*m
        answer +=total[idx]
    return answer
    
'''