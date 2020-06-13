function solution(A) {
    let max = 0, min = Infinity, depth = 0;
    A.forEach((curr, idx) => {
        const next = A[idx + 1] || 0;
        if (curr > max) {
            min = curr;
            max = curr;
        }
        depth = Math.max(Math.min(next, max) -  Math.min(curr, min), depth);
    })
    return depth;
}

solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]);