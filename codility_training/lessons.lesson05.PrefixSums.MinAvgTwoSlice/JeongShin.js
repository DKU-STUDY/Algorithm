function solution(A) {
    const len = A.length;
    let i = 0;
    let min = [];
    let glob_min = Infinity;
    while (i < len - 1) {
        let sum = A[i];
        let min_avg = Infinity;
        for (let j = i + 1; j < i + 3; j++) {
            sum += A[j];
            min_avg = min_avg > sum / (j - i + 1) ? sum / (j - i + 1) : min_avg;
        }
        glob_min = glob_min > min_avg ? min_avg : glob_min;
        min[i] = min_avg;
        i++;
    }
    return min.indexOf(glob_min);
}

solution([4, 2, 2, 5, 1, 5, 8]);