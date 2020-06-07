function solution(N, M) {
    const gcd = (a, b) => {
        if (a % b === 0)
            return b;
        else
            return gcd(b, a % b)
    }
    return ((N * M / gcd(N, M)) / M)
}

solution(10, 4)