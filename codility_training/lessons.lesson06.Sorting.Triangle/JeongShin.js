function solution(A) {
    const len = A.length;
    if (len < 3)
        return 0;
    const sorted = A.sort((a, b) => b - a);
    const isTraingle = (a, b, c) => a < b + c && b < a + c && c < a + b;
    for (let i = 0; i < len - 2; i++) {
        if (isTraingle(sorted[i], sorted[i + 1], sorted[i + 2]))
            return 1;
    }
    return 0;
}

console.log(solution([10, 2, 5, 1, 8, 20]));
