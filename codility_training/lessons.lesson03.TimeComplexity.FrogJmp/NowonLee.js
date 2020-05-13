
function solution(X, Y, D){
    return Math.ceil((Y-X)/D)
}

console.log(solution(10,85,30)===3)
/*
function solution(X, A) {
    var s = new Set();
    for(var i =0;i<A.length;i++){
        s.add(A[i]);
        if(s.size === X && Math.max(...s)===X)
            return i
    }
    return -1
}

console.log(solution(5,[1,3,1,4,2,3,5,4])===6)
*/
