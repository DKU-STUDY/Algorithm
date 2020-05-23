/*
* 이틀정도 해매다가 84%에서 어디가 틀렸는지 모르겠어서 인터넷 검색해서 풀이 공부했습니다 ㅜ ㅜ.
* 일단 merge 해둔뒤 나중에 수정하겠습니다 .
* */



function solution(A) {
    const N = A.length;

    if (N === 3) return 0;

    let headSum = A.map(i => 0);
    let tailSum = A.map(i => 0);

    for (let i = 1; i < N - 1; i++) {
        headSum[i] = Math.max(0, headSum[i - 1] + A[i]);
    }

    for (let i = N - 2; i >= 1; i--) {
        tailSum[i] = Math.max(0, tailSum[i + 1] + A[i]);
    }

    let maxSum = 0;

    for (let i = 1; i < N - 1; i++) {
        maxSum = Math.max(maxSum, headSum[i - 1] + tailSum[i + 1]);
    }

    return maxSum;
}
//출처 : https://sustainable-dev.tistory.com/25
solution([1, 1, 0, 10, -100, 10, 0]);

// function solution(A) {
//     const len = A.length;
//     if (len < 4)
//         return 0;
//     A[0] = 0;
//     A[len - 1] = 0;
//     let max = -Infinity;
//     const result = A.reduce(([acc, min, flag], curr, index) => {
//         const prev = index > 1 ? A[index - 1] : 0;
//         if (index !== 0 && index !== len - 1) { // 처음과 마지막은 최소값으로 포함될 수 없음.
//             min = Math.min(min, curr);
//         }
//         if (prev > 0 && curr < 0) {
//             max = Math.max(flag === 1 ? acc - min : acc, max);
//         }
//         if (prev < 0 && curr >= 0)
//             if (acc - min < 0)
//                 return [curr, curr, 0];
//             else
//                 return [acc + curr, min, 1];
//         return [curr + acc, min, flag]
//     }, [0, Infinity, 0]);
//     max = Math.max(max, result[0] - result[1]);
//     return max < 0 ? 0 : max;
// }