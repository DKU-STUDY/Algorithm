/*
* 아직 풀고 있습니다 ㅠ ㅠ
* */

function solution(A) {
    const len = A.length;
    if (len < 4)
        return 0;
    A[0] = 0;
    A[len - 1] = 0;
    let max = -Infinity;

    A.reduce(([acc, min], curr, index) => {
        const next = A[index + 1];
        if (index !== 0 && index !== len - 1) // 처음과 마지막은 최소값으로 포함될 수 없음.
            min = Math.min(min, curr);
        if (next === undefined)
            max = Math.max(acc - min, max);
        acc += curr;
        // console.log(curr, next, acc, min, max);
        if (curr <= 0 && next >= 0) {
            max = Math.max(acc - min, max);
            if (acc - min < 0)
                return [0, Infinity];
        }
        if (curr >= 0 && next < 0) {
            max = Math.max( acc,acc - min, max);
        }

        return [acc, min];
    }, [0, Infinity]);
    // console.log(max);
    return max;
}