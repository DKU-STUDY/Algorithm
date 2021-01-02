package LeetCode.Math.Maximum_Product_of_Three_Numbers;

import java.util.Arrays;

class HyeonJeong {
    public int maximumProduct(int[] nums) {
        int result = 1;
        Arrays.sort(nums);
        for (int i = nums.length-3; i<nums.length; i++) {
            result *= nums[i];
        }
        if (nums[1] < 0) {
            int n = nums[0]*nums[1]*nums[nums.length-1];
            if (result < n)
                result = n;
        }
        return result;
    }
}
