'''
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
Group the People Given the Group Size They Belong To
dictionary 사용
'''
class Solution(object):
    def groupThePeople(self, groupSizes):
        dic = {}
        for idx, val in enumerate(groupSizes):
            dic.setdefault(val, [])
            dic[val].append(idx)
        answer = []
        for key in dic.keys():
            size = len(dic[key])
            for idx in range(0, size, key):
                answer.append(dic[key][idx:idx + key])
        return answer
'''
dict.setdefault 보다 더 좋은 방법이 있는 것을 알았다.
collections.defaultdict(param)
param에 int를 넘기면 0으로 초기화가 되며
list를 넘기면 []]로 초기화가 된다
'''