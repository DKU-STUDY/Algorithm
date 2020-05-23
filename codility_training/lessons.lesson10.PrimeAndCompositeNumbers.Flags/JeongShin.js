function solution(A) {
    const [peeks, last] = A.reduce(([peek, last_peek], curr, idx) => {
        const [p, n] = [A[idx - 1], A[idx + 1]] || curr
        if (curr > p && curr > n) {
            last_peek !== undefined ? peek.push(idx - last_peek) : null
            return [peek, idx];
        }
        return [peek, last_peek];
    }, [[], undefined]);
    if (last === undefined)
        return 0
    if (peeks.length === 0)
        return 1
<<<<<<< HEAD
    let flags = new Array(peeks.length).fill(1)
    let acc = new Array(peeks.length).fill(0)

=======

    let flags = new Array(peeks.length).fill(1)
    let acc = new Array(peeks.length).fill(0)
>>>>>>> e7b78c144a7e8b11353b75bb0f559662625c9ed1
    for (const val of peeks)
        acc = acc.map((curr, idx) => (val + curr) / (idx + 1) > 1 ? (flags[idx]++, 0) : (val + curr))
    flags = flags.map((curr, idx) => Math.min(idx + 2, curr))
    return Math.max(...flags);
}


<<<<<<< HEAD
solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2, 4, 5, 2]);
=======
solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2, 4, 5, 2]);
>>>>>>> e7b78c144a7e8b11353b75bb0f559662625c9ed1
