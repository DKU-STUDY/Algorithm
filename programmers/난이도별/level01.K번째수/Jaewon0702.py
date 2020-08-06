def solution(array, commands)
    return [ sorted(array[v[0]-1 : v[1]])[v[2] - 1] for v in commands ]
#return [ sorted(array[x-1 : y])[z - 1] for x, y, z in commands 
    

#점수 : 100점



