/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// var search = function(nums, target) {
//     return nums.indexOf(target);
// };

const search = function(nums, target) {
    let start = 0;
    let end = nums.length - 1;
    while (start <= end){
        const mid = ~~((start + end) / 2);
        if (nums[mid] === target)
            return mid;

        if (nums[start] <= nums[mid]){
            if (target < nums[mid] && target >= nums[start])
                end = mid - 1;
            else
                start = mid + 1;
        }

        if (nums[mid] <= nums[end]){
            if (target > nums[mid] && target <= nums[end])
                start = mid + 1;
            else
                end = mid - 1;
        }
    }
    return -1;
}