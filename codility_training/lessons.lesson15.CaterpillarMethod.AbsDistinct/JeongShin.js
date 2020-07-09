function solution(A) {
    return new Set(A.map(v => Math.abs(v))).size;
}

solution([-5, -3, -1, 0, 3, 6]);
