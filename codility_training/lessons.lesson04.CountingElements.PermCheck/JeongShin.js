function solution(A) {
    const len = A.length;
    const arr = [];
    for (let i = 0; i < len; i++) {
        arr[A[i] - 1] = true
    }

    for (const val of arr) {
        if (val === undefined)
            return 0
    }
    return 1;
}

console.log(solution([1, 2, 3]));
