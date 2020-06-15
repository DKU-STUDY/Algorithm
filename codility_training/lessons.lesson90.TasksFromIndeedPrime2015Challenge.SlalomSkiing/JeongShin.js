/*
너무 어려워서 커밋 해두고 나중에 다시 풀어보겠습니다.
* */
function solution(A) {
    const getLongestSequence = arr => {
        const len = arr.length;
        const temp = new Array(len+1);
        temp[0] = -1;
        let result = 0;
        for (const val of arr) {
            let lower = 0;
            let upper = len - 1;
            while (lower <= upper) {
                let mid = ~~((upper + lower) / 2)
                if (val < temp[mid])
                    upper = mid - 1;
                else
                    lower = mid + 1;
            }
            if (temp[lower]===undefined) {
                temp[lower] = val;
                result++;
            } else
                temp[lower] = Math.min(temp[lower], val);
        }
        return result;
    }

    const len = A.length;
    const map = new Array(len * 3);
    const max = Math.max(...A);

    for (let i = 0; i < len; i++) {
        map[i * 3] = max * 2 + A[i] + 1;
        map[i * 3 + 1] = max * 2 - A[i] + 1;
        map[i * 3 + 2] = A[i];
    }

    return getLongestSequence(map);
}


// const A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
// console.log(solution(A))

