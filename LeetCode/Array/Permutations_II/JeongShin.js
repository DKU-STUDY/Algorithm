/**
 * @param {number[]} nums
 * @return {number[][]}
 * 모든 순열 단, 중복된 후보가 있음
 */

/* 나의 풀이 */

const permuteUnique = function (nums) {
    const answer = [];
    const possible = {};
    nums.sort((a, b) => a - b);

    for (const num of nums)
        possible[num] = (possible[num] || 0) + 1;

    backtrack(answer, [], nums, {}, possible);

    return answer;
};

function backtrack(answer, arr, nums, visited, possible, len = nums.length) {
    if (arr.length === len)
        return answer.push(arr);
    for (let i = 0; i < len; i++) {
        const curr = nums[i];
        if (visited[curr] === possible[curr])
            continue;
        arr.push(curr);
        visited[curr] = (visited[curr] || 0) + 1;
        backtrack(answer, [...arr], nums, {...visited}, possible, len);
        arr.pop();
        visited[curr] = visited[curr] - 1;
        while (nums[i] === nums[i + 1])
            i++;
    }
}

permuteUnique([1, 1, 2]);

/* LeetCode 를 참고한 풀이 */

const permuteUnique2 = (nums) => {
    const answer = [];
    const visited = [];
    nums.sort((a, b) => a - b);
    backtrack2(nums, visited, [], answer);
    return answer;
};

function backtrack2(nums, visited, arr, answer, len = nums.length) {
    if (arr.length === len)
        return answer.push(arr);
    for (let i = 0; i < len; i++) {
        if (visited[i] || (i > 0 && nums[i - 1] === nums[i] && !visited[i - 1]))
            continue;
        arr.push(nums[i]);
        visited[i] = true;
        backtrack2(nums, visited, [...arr], answer, len);
        visited[i] = false;
        arr.pop();
    }
}