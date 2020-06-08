const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);

function solution(A, B) {
    let count = 0;
    const len = A.length;
    for (let i = 0; i < len; i++) {
        let [a, b] = [A[i], B[i]]
        const g = gcd(a, b);
        while (true) {
            const r = gcd(a, g)
            if (r === 1)
                break;
            a /= r;
        }
        while (true) {
            const r = gcd(b, g)
            if (r === 1)
                break;
            b /= r;
        }
        count += (b === 1 && a === 1)
    }
    return count
}


// console.log(solution([10], [30]))

