/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 * 모든 조합 중복 O
 */

const combinationSum2 = function (candidates, target) {
    candidates.sort((a, b) => a - b);
    let answer = [];
    const len = candidates.length;

    let dfs = function (idx, num, arr) {
        if (num === 0)
            return answer.push(arr);

        for (let i = idx; i < len; i++) {
            const curr = candidates[i];
            if (curr <= num) {
                dfs(i + 1, num - curr, [...arr, curr]);
            }
            while (candidates[i + 1] === candidates[i]) i++;
        }
        return answer;
    };

    dfs(0, target, []);

    return answer;
};

/* LeetCode 참고한 코드 */
const combinationSum2_2 = (candidates, target) => {
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
        backtrack(candidates, [...arr], i + 1, remain - curr, answer, len);
        arr.pop();
        while (candidates[i + 1] === candidates[i]) i++;
    }
}

const candidates = [10, 1, 2, 7, 6, 1, 5], target = 8;
combinationSum2_2(candidates, target);
// [
//   [1, 7],
//   [1, 2, 5],
//   [2, 6],
//   [1, 1, 6]
// ]

