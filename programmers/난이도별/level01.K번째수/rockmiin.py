
def solution(array, commands):

    result=[]
    for i in range (len(commands)):
        cut=array[commands[i][0]-1:commands[i][1]]
        cut=sorted(cut)
        result.append(cut[commands[i][2]-1])
    return result
