function solution(A, K) {
    return A.slice(A.length-K).concat(A.slice(0,A.length-K));
}
