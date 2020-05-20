function solution(A) {
    return A.reduce(([max, acc], curr) => {
        max = Math.max(acc + curr, max, curr);
        return acc < 0 ? [max, curr] : [max, acc + curr]
    }, [-Infinity, 0])[0];
}

