function solution(A) {
    const len = A.length;
    const peeks = A.reduce((peeks, curr, idx) => {
        if (curr > A[idx - 1] && curr > A[idx + 1])
            peeks.push(idx);
        return peeks;
    }, []);
    let k = peeks.length;
    while (k > 0) {
        if (len % k) {
            k--
            continue
        }
        const size = len / k
        const result =
            peeks.reduce(([count, from, to], curr) =>
                    curr < from ?
                        [count, from, to] :
                        [count + (from <= curr && curr <= to), from + size, to + size]
                , [0, 0, size - 1])[0];
        if (result === k) return k;
        k--;
    }
    return 0;
}
