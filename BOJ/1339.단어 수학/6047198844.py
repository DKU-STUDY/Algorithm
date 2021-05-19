#00GCF
#ACDEB
#자릿수가 클수록 높은 번호를 가져야함.
#그러면 만약에
#ACDEB CAGCF 의 경우는 ?
import collections
import sys

N = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(N)]
dict = collections.defaultdict(int)

for word in words:
    for idx, w in enumerate(word[::-1]):
        dict[w] = dict[w] + 10 ** idx

nums = sorted(dict.values(), reverse=True)
res = 0

for idx, num in enumerate(nums):
    res += num * (9-idx)

print(res)
#dict.update()
#string배열을 set으로 하는 방법
#dict key를 기준으로 정렬
#dict update
#가중치