/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 * 모든 조합 중복 X
 */
const combinationSum = function (candidates, target) {
    const len = candidates.length;
    const answer = [];
    candidates.sort((a, b) => b - a);
    const combination = (array, sum, idx) => {
        if (target <= sum)
            return target === sum ? answer.push(array) : null;
        for (let i = idx; i < len; i++) {
            const v = candidates[i];
            if (v < array[0] || 0)
                continue;
            combination([v, ...array], sum + v, idx);
        }
    };

    combination([], 0, 0);
    return answer;
};

/* LeetCode 에서 참고한 풀이 */

const combinationSum_2 = (candidates, target) => {
    const answer = [];
    candidates.sort((a, b) => a - b);
    backtrack(candidates, [], 0, target, answer);
    return answer;
};

function backtrack(candidates, arr, idx, remain, answer, len = candidates.length) {
    if (remain <= 0)
        return remain === 0 ? answer.push(arr) : null;
    for (let i = idx; i < len; i++) {
        const curr = candidates[i];
        arr.push(curr);
        backtrack(candidates, [...arr], i, remain - curr, answer, len);
        arr.pop();
    }
}

combinationSum2([2, 3, 6, 7], 7);