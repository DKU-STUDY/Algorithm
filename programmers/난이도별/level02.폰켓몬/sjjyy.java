import java.util.ArrayList;

public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/1845
        @param N마리 폰켓몬의 종류 번호가 담긴 배열 nums
        N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 폰켓몬을 선택하는 방법 찾기
        @return 가장 많은 폰켓몬을 선택할 때, 폰켓몬 종류 번호의 개수
    */

    public static int solution(int[] nums) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int num : nums) { // 중복되는 폰켓몬 번호를 제외하고 리스트에 삽입
            if (!list.contains(num))
                list.add(num);
        }

        return Math.min(list.size(), nums.length / 2);
        // 선택할 수 있는 개수보다 폰켓몬의 종류가 적으면 폰켓몬의 종류를, 아니면 선택할 수 있는 개수를 리턴
    }

    public static void main(String[] args) {
        int[] nums1 = {3, 1, 2, 3};
        int[] nums2 = {3, 3, 3, 2, 2, 4};
        int[] nums3 = {3, 3, 3, 2, 2, 2};

        System.out.println(solution(nums1)); // 2
        System.out.println(solution(nums2)); // 3
        System.out.println(solution(nums3)); // 2
    }
}
