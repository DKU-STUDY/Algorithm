package LeetCode.Array.Maximum_Subarray;

import java.util.Arrays;

class HyeonJeong {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i=0; i+1<nums.length; i+=2) {
            if (nums[i] != nums[i+1])
                return nums[i];
        }
        return nums[nums.length-1];
    }
}
