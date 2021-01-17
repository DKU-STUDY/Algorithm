package LeetCode.Array.Max_Consecutive_Ones;

class HyeonJeong {
    public int findMaxConsecutiveOnes(int[] nums) {
        int length = 0, i, j;
        for (i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                for (j = i+1; j < nums.length; j++) {
                    if (nums[j] != 1) {
                        break;
                    }
                }
                if (j-i > length) {
                    length = j-i;
                }
                i = j;
            }
        }
        return length;
    }
}
