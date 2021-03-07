package LeetCode.Array.Squares_of_a_Sorted_Array;

import java.util.Arrays;

class HyeonJeong {
    public int[] sortedSquares(int[] nums) {
        int []result = nums;
        for (int i = 0; i < nums.length; i++) {
            result[i] *= result[i];
        }
        Arrays.sort(result);
        return result;
    }
}
