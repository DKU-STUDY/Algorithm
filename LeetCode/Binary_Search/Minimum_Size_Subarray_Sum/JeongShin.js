/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
const minSubArrayLen = function (s, nums) {
    let sum = 0, start = 0;
    const answer = nums.reduce((minLen, num, end) => {
        sum += num;
        // 만약 sum 이 기준치를 넘게 되면 최소 길이를 구하기 위해 minLen 을 구합니다.
        // 앞에서 숫자를 하나씩 빼면서 최소 길이를 유지 합니다.
        while (sum >= s) {
            minLen = Math.min(minLen, end - start + 1);
            sum -= nums[start++];
        }
        return minLen;
    }, Infinity);
    return answer === Infinity ? 0 : answer;
};

console.log(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]));

