/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const sortColors = function (nums) {
  if (nums[1] === undefined)
    return;
  let [pointer, left, right] = [0, 0, nums.length - 1];
  while (left <= right) {
    let temp = nums[left];
    if (temp === 2) {
      nums[left] = nums[right];
      nums[right] = temp;
      right--;
      continue;
    }
    if (temp === 0) {
      nums[left] = nums[pointer];
      nums[pointer] = temp;
      pointer++;
    }
    left++;
  }
};


sortColors([2, 0, 2, 1, 1, 0]);