function solution(N) {
    const n = Math.sqrt(N);
    let min = Infinity
    for (let x = 1; x <= n; x++) {
        const [y, r] = [N / x, N % x]
        min = r === 0 ? Math.min(2 * (x + y), min) : min
    }
    return min;
}

solution(1)