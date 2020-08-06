function solution(A) {
    const len = A.length;
    const score = new Array(len).fill(-Infinity);
    score[0] = A[0];
    for (let curr = 0; curr < len; curr++) {
        for (let k = 1; k < 7; k++) {
            const next = curr + k;
            if (next > len)
                break;
            const sum = score[curr] + A[next];
            score[next] = Math.max(sum, score[next]);
        }
    }
    return score[len -1];
}

console.log(solution([1, -2, 0, 9, -1, -2]))
