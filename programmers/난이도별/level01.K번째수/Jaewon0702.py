def solution(array, commands):
    return [ sorted(array[v[0]-1 : v[1]])[v[2] - 1] for v in commands ]
#

#점수 : 100점



