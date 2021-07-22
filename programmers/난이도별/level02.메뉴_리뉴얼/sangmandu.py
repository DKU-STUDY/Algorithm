'''
https://programmers.co.kr/learn/courses/30/lessons/72411
메뉴 리뉴얼
[풀이]
1. dictionary와 combinations 사용
'''
from itertools import combinations
def solution(orders, course):
    result = []
    for c in course:
        count = {}
        for order in orders:
            for o in combinations(order , c):
                key = ''.join(sorted(o))
                count.setdefault(key, 0)
                count[key] += 1
        if len(count.keys()) == 0:
            break
        max_count = count[max(count, key=count.get)]
        if max_count > 1:
            for key in count.keys():
                if count[key] == max_count:
                    result.append(key)
    return sorted(result)
'''
`get` 을 사용해 Key로 Value를 얻을 수 있다
또, 아래 코드와 같이 collections.Counter(param).most_common() 을 사용해서 가장 많이 나온 원소를 셀 수 있다

import collections
for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

'''