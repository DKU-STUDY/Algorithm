
/* 90점으로 Correctness Test Case 1 개에 있어서 통과를 못하겠어서 일단 넘어가고 다른 문제 먼저 풀겠습니다. */

function solution(A) {
    const len = A.length;
    if (len < 2)
        return Math.abs(A[len - 1] || 0);
    const absA = A.map(el => Math.abs(el));
    let sum = absA.reduce((acc, curr) => acc + curr);
    absA.sort((a, b) => b - a);
    absA.forEach((val) => {
        const nextsum = sum - val * 2;
        if (nextsum >= 0 && nextsum < sum) {
            sum = nextsum
        }
    });
    return sum;
}

// function solution(A) {
//     const len = A.length;
//     A.sort((a, b) => Math.abs(b) - Math.abs(a))
//     if (len < 2)
//         return Math.abs(A[len - 1] || 0);
//     let parent = new Set().add(0);
//     A.forEach((x, idx) => {
//         const child = new Set();
//         for (const y of parent) {
//             const left = len - idx;
//             if (y < left * Math.abs(x))
//                 child.add(Math.abs(x + y));
//             child.add(Math.abs(x - y))
//         }
//         console.log(child)
//         parent = child;
//     });
//     return Math.min(...parent)
// }


/* Second Solution */
// function solution(A) {
//     const cache = {};
//     const len = A.length;
//     let min = Infinity;
//     A.sort((a, b) => Math.abs(b) - Math.abs(a))
//     const dp = (val, idx) => {
//         if (cache[[val, idx]] === true) {
//             return 0;
//         } else if (idx === len) {
//             min = Math.min(min, Math.abs(val));
//             return 0;
//         } else if (val > Math.abs(A[idx]) * (len - idx)) {
//             return 0;
//         }
//         cache[[val, idx]] = true;
//         dp(val - A[idx], idx + 1);
//         dp(val + A[idx], idx + 1);
//         return 0;
//     };
//     dp(0, 0);
//     return min;
// }

