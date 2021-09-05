'''
https://www.acmicpc.net/problem/14719
빗물
[풀이]
1. 20칸인 기차 생성
2. 각 액션들을 인덱스 번호로 실행할 수 있도록 선언
=> exec 사용 => lambda 에서는 할당이 안되므로
3. 열차칸을 문자열로 만들고 set()으로 중복 조사.
'''
import sys
input = sys.stdin.readline
input()
blocks = [i for i in map(int, input().strip().split())]
left_block = rain = stagnant_rain = 0
for idx, block in enumerate(blocks):
    left_block = max(block, left_block)
    rain = left_block - block
    if rain > 0:
        right_block = block
        for next_b in blocks[idx+1:]:
            right_block = max(right_block, next_b)
            if right_block >= left_block:
                break
        stagnant_rain += min(left_block, right_block) - block
print(stagnant_rain)