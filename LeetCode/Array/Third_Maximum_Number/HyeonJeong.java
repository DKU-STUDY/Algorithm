package LeetCode.Array.Third_Maximum_Number;

import java.util.Arrays;

class HyeonJeong {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int tmp = 1, n = nums[nums.length-1];
        for (int i = nums.length-2; i >= 0; i--) {
            if (n > nums[i]) {
                tmp += 1;
                n = nums[i];
            }
            if (tmp == 3) // 3번째 큰 값 반환
                return n;
        }
        return nums[nums.length-1];
        // 값이 2개 이하로 사용된 배열이 주어진 경우는 가장 큰 값 반환
    }
}