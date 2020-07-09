
def solution(array, commands):

    result=[]
    for i in range (len(commands)):
        cut=array[commands[i][0]-1:commands[i][1]]
        cut=sorted(cut)
        result.append(cut[commands[i][2]-1])
    return result

if __name__=="__main__":
    array=[1,5,2,6,3,7,4]
    commands=[[2,5,3],[4,4,1],[1,7,3]]

    solution(array, commands)