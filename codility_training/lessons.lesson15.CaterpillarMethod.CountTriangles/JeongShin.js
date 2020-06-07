function solution(A) {
    const len = A.length;
    let result = 0;
    A.sort((a, b) => a - b);
    for (let x = 0; x < len; x++) {
        let z = x + 2;
        for (let y = x + 1; y < len; y++) {
            while (z < len && (A[x] + A[y]) > A[z]) {
                z += 1
            }
            result += (z - y - 1)
        }
    }
    return result;
}

solution([10, 2, 5, 1, 8, 12])