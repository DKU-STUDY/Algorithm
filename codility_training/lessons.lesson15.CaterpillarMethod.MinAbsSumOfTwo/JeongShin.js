function solution(A) {
    const len = A.length;
    const abs = (x, y) => Math.abs(x + y);
    if (len < 2)
        return abs(A[0], A[0]);
    A.sort((a, b) => b - a);
    let min = Infinity;
    let x = 0, y = len - 1;
    while (x <= y) {
        const curr = abs(A[y], A[x]);
        const next = abs(A[y - 1], A[x]);
        [x, y] = curr < next ? [x + 1, y] : [x, y - 1];
        min = Math.min(min, curr);
    }
    return min;
}

solution([-1, -4, -3, -5]);