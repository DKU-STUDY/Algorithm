package LeetCode.Array.Array_Partition_I;

import java.util.Arrays;

class HyeonJeong {
    public int arrayPairSum(int[] nums) {
        /*
        정수 배열의 2 요소씩 만들어진 그룹이 둘 중의 작은 수 값을 가질 때, 그룹들의 합계가 최대가 되는 합계 반환하는 문제
        풀이 : 정렬한 배열에서 순서대로 두개씩 그룹을 만들면 그룹의 합계를 최대로 만들 수 있음
        */
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}
