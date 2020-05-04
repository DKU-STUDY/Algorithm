function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    var r = 0
    A.sort(function(a,b){return a-b})
    if(A[0] !== 1) return 1;
    else if(A[A.length-1]  !== A.length+1) return A.length+1;
    else {
        for(var i=0;i<A.length-1;i++){
            if(A[i+1]-A[i] !== 1){
                r = A[i]+1
            }
        }
        return r
    }
}

console.log(solution([2,3,1,5])===4)