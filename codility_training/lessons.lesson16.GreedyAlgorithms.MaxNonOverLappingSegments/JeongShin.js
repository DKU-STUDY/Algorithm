function solution(A, B) {
    const len = A.length;
    if (len < 2)
        return len;
    let count = 1;
    let end = B[0];
    for (let idx = 1; idx < len; idx++) {
        while (idx < len && A[idx] <= end) {
            idx++;
        }
        if (idx === len)
            break;
        count++;
        end = B[idx]
    }
    return count;
}

solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]);
