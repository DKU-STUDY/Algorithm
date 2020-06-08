function solution(A, B) {
    const [max_a, max_b] = [Math.max(...A), Math.max(...B)]
    const fibonacci = n => {
        const fib = [0, 1];
        for (let i = 2; i < n + 2; i++)
            fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << max_b) - 1)
        return fib
    }
    const fib = fibonacci(max_a);
    return A.map((el, idx) => fib[el + 1] & ((1 << B[idx]) - 1))
}
