/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
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
const candidates = [10, 1, 2, 7, 6, 1, 5], target = 8;
combinationSum2(candidates, target);
// [
//   [1, 7],
//   [1, 2, 5],
//   [2, 6],
//   [1, 1, 6]
// ]