/**
 * 출처 : https://leetcode.com/problems/jump-game/
 *
 * 문제:
 * 양의 정수로 주어진 배열이 있을때, 가장 첫번째 요소는 최초 위치를 나타낸다.
 * 그 다음부터 요소들 마다 점프할 수 있는 최대 범위를 나타낸다.
 * 마지막 인덱스에 도달 할 수 있는지 여부에 대해 반환 하여라.
 *
 * @param {number[]} nums
 * @return {boolean}
 */

// Sol 1. Runtime : 2496 ms Memory : 42.3 MB
// 👉 Greedy X

const canJump = function (nums) {
    const target = nums.length - 1;
    const possible = [true];

    for (const [idx, num] of nums.entries()) {
        if (possible[target])
            return true;
        if (!possible[idx])
            continue;
        const end = idx + num;
        for (let i = idx; i <= end; i++) {
            possible[i] = true;
        }
    }
    return false;
};

// Sol2. Runtime : 76ms, Memory : 42.3 MB

const canJump2 = function (nums) {
    let distance = 0;
    const target = nums.length - 1;
    for (let i = 0; i <= distance; i++) {
        distance = Math.max(distance, i + nums[i]);
        if (distance >= target)
            return true
    }
    return false;
};


console.log(canJump([2, 3, 1, 1, 4])) // true
console.log(canJump([3, 2, 1, 0, 4])) // false