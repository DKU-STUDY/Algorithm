function solution(n) {
    const p = [2]
    for (let i = 3; i <= n; i+=2) {
        let bool = true
        for (let j = 1; p[j] <= Math.pow(i, 1/2); j++) {
            if (i % p[j] === 0) {
                bool = false
                break
            }
        }
        if (bool) p.push(i)
    }
    return p.length
}