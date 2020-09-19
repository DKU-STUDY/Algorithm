function solution(array, commands) {
    let sort;
    let answer=[];
    const commands_length= commands.length;
    for(let i=0;i<commands_length;i++)
    {
        sort=array.slice(commands[i][0]-1,commands[i][1]);
        sort.sort((A,B)=>(A-B))
        answer.push(sort[commands[i][2]-1]);
    }
    return answer;
}
