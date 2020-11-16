function solution(participant, completion) {
    const obj = {}
    completion.forEach((el)=> {
        obj[el]=(obj[el]||0) + 1;
    })
    for (const p of participant) {
        if ((obj[p]||0)< 1)
            return p
        obj[p]--
    }
}