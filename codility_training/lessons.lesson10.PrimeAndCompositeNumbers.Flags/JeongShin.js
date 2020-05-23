/*
이 문제는 다음에 다시 시도해보겠습니다 어렵네요 ㅠ ㅠ
시간 복잡도 측면에서 해결이 안되네요.
 */

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
    let flags = new Array(peeks.length).fill(1)
    let acc = new Array(peeks.length).fill(0)
    for (const val of peeks)
        acc = acc.map((curr, idx) => (val + curr) / (idx + 1) > 1 ? (flags[idx]++, 0) : (val + curr))
    flags = flags.map((curr, idx) => Math.min(idx + 2, curr))
    return Math.max(...flags);
}

