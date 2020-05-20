function solution(N) {
    if(N===1) return 1
    let result = 0;
    /*
    for(let i = 1; i*i<=N;i++){
        if(N%i===0){
            if(i*i === N)
                result += 1;
            else {
                result += 2;
            }    
        }
    }
    */
    let i = 1;
    while(i ** 2 < 0){
        result += !(N % i++) * 2
    }
    return result + !(N%i)
}

console.log(solution(24)===8)
