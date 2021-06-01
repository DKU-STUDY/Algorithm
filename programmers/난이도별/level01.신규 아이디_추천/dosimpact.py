import sys
import math
from typing import *

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#  규칙에 맞지 않는 아이디를 입력했을 때 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는


# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
#  알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
#  단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습


def solution(new_id: str):
    new_id = list(new_id)
    new_id = list(map(lambda x: (x).lower() if (x).isupper() else x, new_id))
    print(new_id)  # 1

    def ST2(ch: str):
        if ch.isalnum() or ch == '-' or ch == '_' or ch == '.':
            return True
        return False
    new_id = list(filter(ST2, new_id))
    print(new_id)  # 2

    new_id_parsed = [new_id[0]]
    for i in range(1, len(new_id)):
        if new_id_parsed[-1] == '.' and new_id[i] == '.':
            continue
        new_id_parsed += [new_id[i]]
    new_id = new_id_parsed

    print(new_id)  # 3
    if new_id and new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop(len(new_id)-1)
    print(new_id)  # 4
    if len(new_id) == 0:
        new_id += ['a']
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop(len(new_id)-1)

    if len(new_id) == 2:
        new_id += [new_id[-1]]
    if len(new_id) == 1:
        new_id += [new_id[-1]]*2

    return "".join(new_id)
