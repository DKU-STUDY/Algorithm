/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 * nums 가 주어졌을때 각 요소 별로 +, - 값을 가질때 합이 target 과 같아지는 방법의 개수를 구하는 문제
 */
const findTargetSumWays = function (nums, target) {
    return dfs(nums, 0, 0, target, nums.length);
};

const dfs = function (nums, idx ,sum, target, len) {
    if (idx === len)
        return sum === target;

    const num = nums[idx];

    let result = 0;

    result += dfs(nums, idx + 1, sum + num, target, len);
    result += dfs(nums, idx + 1, sum - num, target, len);

    return result;
};


console.log(findTargetSumWays([1, 1, 1, 1, 1], 3))