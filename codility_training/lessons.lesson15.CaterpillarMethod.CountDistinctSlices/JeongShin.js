// function solution(M, A) {
//     let appeared = [];
//     const result = A.reduce(([acc, count], curr) => {
//         if (!appeared[curr]) {
//             count++;
//         } else {
//             count = 1;
//             appeared = [];
//         }
//         appeared[curr] = true;
//         return [acc + count, count];
//     }, [0, 0])[0]
//     return Math.min(result, 1000000000)
// }

function solution(M, A) {
    const len = A.length
    let sum = 0, front = 0, back = 0
    const appeared = []
    while (front < len && back < len) {
        while (front < len && appeared[A[front]] === undefined) {
            sum += (front - back + 1)
            appeared[A[front]] = true
            front += 1
        }
        while (A[back] !== A[front]) {
            appeared[A[back]] = undefined
            back += 1
        }
        appeared[A[back]] = undefined
        back += 1
    }
    return Math.min(sum, 1000000000)
}

solution(6, [3, 4, 5, 5, 2])