function solution(N) {
    if(N===1) return 1
    var result = 0;
    for(let i = 1; i*i<=N;i++){
        if(N%i===0){
            if(i*i === N)
                result += 1;
            else {
                result += 2;
            }    
        }
    }
    return result
}

console.log(solution(24)===8)
