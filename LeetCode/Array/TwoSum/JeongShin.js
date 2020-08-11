/* Brute Force Method */
const twoSum = function (nums, target) {
    const len = nums.length;
    for (let i = 0; i < len; i++) {
        for (let j = i + 1; j < len; j++) {
            if (nums[i] + nums[j] === target && i !== j)
                return [i, j]
        }
    }
};

/* 다른 사람 풀이 */
const twoSum2 = function (nums, target) {
    const cache = {};
    for (let i = 0; i < nums.length; i++) {
        const curr = nums[i];
        if (cache[curr] >= 0) {
            return [cache[curr], i]
        }
        cache[target - curr] = i
    }
};

