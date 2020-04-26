function solution(A, K) {
    return A.slice(A.length-K).concat(ActiveXObject.slice(0,A.length-K));
}
