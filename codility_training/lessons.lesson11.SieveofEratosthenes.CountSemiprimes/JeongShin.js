function solution(N, P, Q) {
    const semi_primes = new Array(N + 1).fill(0)
    for (let i = 2; i <= N; i++) {
        if (semi_primes[i] === 0) {
            for (let j = i * i; j <= N; j += i)
                if (semi_primes[j] === 0)
                    semi_primes[j] = i;
        }
    }
    semi_primes[0] = 1;     // 1 is not prime num
    const semi_primes_count = semi_primes.reduce(([arr, acc], curr, idx) => {
        if (curr !== 0)
            acc += (semi_primes[idx / curr] === 0) * 1
        arr.push(acc);
        return [arr, acc];
    }, [[], 0])[0]
    return P.map((P, idx) => (semi_primes_count[Q[idx]] - (semi_primes_count[P - 1] || 0))) // P 자기자신 포함,직전 ~ Q 까지 차이
}



