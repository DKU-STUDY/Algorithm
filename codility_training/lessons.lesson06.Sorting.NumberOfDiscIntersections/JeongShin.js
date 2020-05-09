function solution(A) {
    const len = A.length;
    let count = 0;
    A.forEach((el, idx) => {
        for (let j = idx + 1; j < len; j++) {
            if (count > 10000000)
                return -1;
            count = (idx - A[idx] >= j + A[j] || idx + A[idx] >= j - A[j]) ? count + 1 : count;
        }
    });
    return count;
}

console.log(solution2([1, 5, 2, 1, 4, 0]));