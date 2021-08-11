'''
https://www.acmicpc.net/problem/9081
단어 맞추기
[풀이]
1. 각 단어가 구성할 수 있는 경우의 수를 구하기 위해 permutations import
2. 이 때 단어의 알파벳이 중복될수도 있으므로 set을 적용해준다
3. 입력받은 단어 뒤의 단어를 알기위해 정렬을 한다
=> 문자열의 순서는 문자열을 숫자로 바꾸더라도 동일하다
4. idx를 찾는다. 마지막 원소라면 그대로 유지. 이후 반환
'''
from itertools import permutations
n = int(input())
for _ in range(n):
    word = list(input())
    num = [ord(w) for w in word]
    nums = sorted([n for n in tuple(set(permutations(num, len(num))))])
    idx = nums.index(tuple(num))
    idx = idx if idx+1 == len(nums) else idx+1
    print(''.join([chr(n) for n in nums[idx]]))
