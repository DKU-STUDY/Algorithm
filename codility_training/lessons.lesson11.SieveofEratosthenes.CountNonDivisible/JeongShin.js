function solution(A) {
    const len = A.length
    const max = Math.max(...A)
    const count = {}
    let ones = 0
    for (const val of A) {
        if (val === 1) {
            ones++
            continue
        }
        for (let i = 1; (i * val) <= max; i++)
            count[i * val] = (count[i * val] || 0) + 1
    }
    return A.map(el => len - (count[el] || 0) - ones)
}

// solution([3, 1, 2, 3, 6])

