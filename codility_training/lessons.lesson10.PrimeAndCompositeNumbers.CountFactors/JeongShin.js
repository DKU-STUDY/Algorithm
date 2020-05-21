function solution(N) {
    if (N === 1)
        return 1
    const n = ~~Math.sqrt(N)
    let count = 0
    for (let i = 1; i <= n; i++)
        count += (N % i === 0) * 1
    return count * 2 - (N / n === n) * 1
}

console.log(solution(4))