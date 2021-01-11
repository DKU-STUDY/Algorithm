package LeetCode.Divide_and_Conquer.Kth_Largest_Element_in_an_Array;

import java.util.Arrays;

class HyeonJeong {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length-k]; // k 번째 큰 요소
    }
}
