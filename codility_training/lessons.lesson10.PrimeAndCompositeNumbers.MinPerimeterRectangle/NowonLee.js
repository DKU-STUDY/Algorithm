function solution(N) {
    let l = []
    for(let i = 1;i*i<=N;i++){
        if(N%i == 0) l.push(i)
    }
    /*
    const nums = l.map(el => {
        return 2*(el + (N/el))
    })
    return Math.min(...nums)
    */
    return l.reduce((min, el) => {
        return Math.min(min, 2 * (el + N/el))
     }, Infinity)
}

console.log(solution(36)===24)
