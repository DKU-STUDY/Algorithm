function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    var r = 0
    const l = A.length;
    A.sort((a,b) => a-b)
    if(A[0] !== 1) return 1;

    else if(A[l-1]  !== l+1) return l+1;
    for(var i=0;i<l-1;i++){
        if(A[i+1]-A[i] !== 1){
            r = A[i]+1
        }
    }
    return r
}

console.log(solution([2,3,1,5])===4)
