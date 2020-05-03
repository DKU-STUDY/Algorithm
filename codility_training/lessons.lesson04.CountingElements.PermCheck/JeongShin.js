/*
1,2,3,4 -> 순열 O -> return 1
1, 3, 4 -> 순열 X -> return 0

고려: 중복, missing
 */
function solution(A) {
    const len = A.length;
    let arr = [];
    let count = 0;
    for (let i = 0; i < len; i++) {
        const val = A[i] - 1;
        if (val < 0)
            continue;
        else if (!arr[val]) {
            arr[val] = true;
            count++;
        } else
            return 0;
    }

    for (const val of arr) {
        if (val === undefined)
            return 0
    }
    return 1;
}

console.log(solution([1, 2, 3]));