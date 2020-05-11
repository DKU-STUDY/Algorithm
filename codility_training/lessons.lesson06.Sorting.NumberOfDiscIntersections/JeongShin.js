/*제가 작성한 코드
* */

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

/*
https://jobjava00.github.io/algorithm/codility/lesson6/NumberOfDiscIntersections/
에서 참고하여 작성한 코드
* */

function solution2(A) {
    const len = A.length;
    const lower = [];
    const upper = [];
    for (let i = 0; i < len; i++) {
        lower [i] = i - A[i];
        upper [i] = i + A[i];
    }
    // console.log(lower, upper);

    lower.sort((a, b) => a - b);
    upper.sort((a, b) => a - b)

    // console.log(lower, upper);

    let intersections = 0;
    let j = 0;
    for (let i = 0; i < len; i++) {
        while (j < len && upper[i] >= lower[j]) {
            // console.log(intersections, i,j);
            intersections += j;
            intersections -= i;
            j++;
        }
    }
    return intersections > 10000000 ? -1 : intersections;
}

console.log(solution2([1, 5, 2, 1, 4, 0]));