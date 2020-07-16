function solution(n) {
    const fib = [0, 1, 2]
    for (let i = 3; i <= n; i++) {
        fib[i] = (fib[i - 2] + fib[i - 1])%1000000007
    }
    return fib[n]
}