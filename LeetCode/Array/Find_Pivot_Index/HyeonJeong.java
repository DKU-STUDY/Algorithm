package LeetCode.Array.Find_Pivot_Index;

class HyeonJeong {
    public int pivotIndex(int[] nums) {
        int len = nums.length;
        for (int i = 0; i < len; i++) {
            int left = 0, right = 0;
            for (int j = 0; j < len; j++) { // 배열에서 기준 요소(nums[j])에 따라 양쪽 요소들의 합을 구함
                if (j < i)
                    left += nums[j];
                else if (j > i)
                    right += nums[j];
            }
            if (left == right)
                return i;
        }
        return -1;
    }
}
