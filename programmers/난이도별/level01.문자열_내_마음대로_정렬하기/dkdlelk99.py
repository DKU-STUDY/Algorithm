def solution(strings, n):
    strings.sort()
    strings = sorted(strings,key= lambda x : x[n])
    return strings

print(solution(	["sun", "bed", "car"],1) == ['car', 'bed', 'sun'])
print(solution(	["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"])
