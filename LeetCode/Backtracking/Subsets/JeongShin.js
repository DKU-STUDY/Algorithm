/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsets = function (nums) {
    const answer = [];
    backtracking(nums, [], 0, nums.length, answer);
    console.log(answer)
    return answer;
};

function backtracking(nums, subset, start, target, answer) {
    for (let i = start; i < target; i++) {
        subset.push(nums[i]);
        backtracking(nums, [...subset], i + 1, target, answer);
        subset.pop();
    }
    answer.push([...subset]);
}

subsets([1, 2, 2]);

