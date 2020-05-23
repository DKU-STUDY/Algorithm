function solution(A) {
    return A.reduce(([max, acc], curr) => {
        max = Math.max(acc + curr, max, curr);
        return [max, curr + !(acc < 0) * acc]
    }, [-Infinity, 0])[0];
}
