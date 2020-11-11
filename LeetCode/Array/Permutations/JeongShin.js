/**
 * @param {number[]} nums
 * @return {number[][]}
 * 모든 순열 (경우의 수) 중복 X
 */
const permute = function (nums) {
    const answer = [];
    permutation(nums, [], answer);
    return answer;
};

function permutation(nums, arr, answer, len = nums.length) {
    if (arr.length === len)
        return answer.push(arr);
    nums.forEach((v) => {
        if (!~arr.indexOf(v))
            permutation(nums, [...arr, v], answer, len);
    })
}

permute([1, 2, 3]);

/* LeetCode 를 참고한 풀이 */
const permute = function (nums) {
    const answer = [];
    backtrack(answer, [], nums);
    return answer;
};

function backtrack(answer, arr, nums, len = nums.length) {
    if (arr.length === len)
        return answer.push(arr);
    for (let i = 0; i < len; i++) {
        const curr = (nums[i]);
        if (arr.includes(curr))
            continue;
        arr.push(curr);
        backtrack(answer, [...arr], nums, len);
        arr.pop();
    }
}




