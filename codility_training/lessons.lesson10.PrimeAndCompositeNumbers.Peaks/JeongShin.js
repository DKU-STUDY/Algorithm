function solution(A) {
    const len = A.length;
    const peeks = A.reduce((peeks, curr, idx) => {
        const [p, n] = [A[idx - 1], A[idx + 1]] || curr;
        if (curr > p && curr > n) peeks.push(idx);
        return peeks;
    }, []);
    let k = peeks.length;
    while (k > 0) {
        let size = len % k === 0 ? len / k : undefined;
        if (size === undefined) {
            k--;
            continue;
        }
        const result =
            peeks.reduce(([count, from, to], curr) => {
                if (curr < from) return [count, from, to];
                return [
                    count + (from <= curr && curr <= to) * 1,
                    from + size,
                    to + size,
                ];
            }, [0, 0, size - 1])[0];
        if (result === k) return k;
        k--;
    }
    return 0;
}

const r = solution([1, 3, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4])
console.log(r)