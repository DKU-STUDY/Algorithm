package LeetCode.Array.Summary_Ranges;

import java.util.ArrayList;
import java.util.List;

class HyeonJeong {
    public List<String> summaryRanges(int[] nums) {
        List<String> list = new ArrayList<>();
        if (nums.length == 0)
            return list;
        int i = 0, num = nums[0];

        while (i < nums.length) {
            if (i+1 == nums.length || nums[i]+1 != nums[i+1]) {
                if (num == nums[i]) // 1개의 값이 범위가 되는 경우
                    list.add(Integer.toString(num));
                else // 2개이상의 값이 범위가 되는 경우
                    list.add(num + "->" + nums[i]);

                if (i+1 < nums.length)
                    num = nums[i+1];
            }
            i++;
        }
        return list;
    }
}