function solution(A) {
    const o = {}
    const mx = Math.max(...A)
    if(m<1) return 1
    A.forEach((a) => {
        if(a>0) o[a] = true;
    })
    var m = mx
    for(var j=1;j<m;j++){
        if(!o[j]) return j
    }
    return m+1
}

console.log(solution([1,3,6,4,1,2]) === 5)
console.log(solution([1,2,3]) === 4)
