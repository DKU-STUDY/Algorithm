function solution(A) {
    const len = A.length;
    const arr = new Array(len).fill(-Infinity);
    arr[0] = A[0];
    for (let idx = 0; idx < len; idx++) {
        for (let k = 1; k < 7; k++) {
            const nextIdx = idx + k;
            if (nextIdx > len)
                break;
            const sum = arr[idx] + A[nextIdx];
            if (arr[nextIdx] < sum)
                arr[nextIdx] = sum;
        }
    }
    return arr[len -1];
}

console.log(solution([1, -2, 0, 9, -1, -2]))
