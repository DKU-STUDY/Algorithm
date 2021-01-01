class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> list = new ArrayList<String>();
        if (nums.length == 0)
            return list;
        int i = 0, num = nums[0];

        while (i < nums.length) {
            if (i+1 == nums.length || nums[i]+1 != nums[i+1]) {
                if (num == nums[i])
                    list.add(Integer.toString(num));
                else
                    list.add(num + "->" + nums[i]);

                if (i+1 < nums.length)
                    num = nums[i+1];
            }
            i++;
        }
        return list;
    }
}