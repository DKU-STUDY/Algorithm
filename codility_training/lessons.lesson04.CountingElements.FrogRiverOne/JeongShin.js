function solution(X, A) {
    if (X === 0 || !A) return;
    const set = Array.from(new Set(A));
    const len = set.length;
    if (len!==X)
        return -1;
    else{
        return A.indexOf(set[len-1]);
    }
}

console.log(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]));
