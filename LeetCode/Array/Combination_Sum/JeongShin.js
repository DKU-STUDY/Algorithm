/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
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
            combination([v,...array], sum + v, idx);
        }
    };

    combination([], 0, 0);
    return answer;
};

