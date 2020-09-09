package 난이도별.level01.평균_구하기;

import java.util.Arrays;

public class sjjyy {
    public static double solution(int[] arr)
    {
        double answer = 0;

        for (int i : arr) {
            answer += i;
        }

        answer /= arr.length;
        return answer;
    }

    public static double solution2(int[] arr)
    {
        return Arrays.stream(arr).average().getAsDouble();
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int[] arr2 = {5, 5};
        System.out.println(solution(arr)); // 2.5
        System.out.println(solution(arr2)); // 5

        System.out.println(solution2(arr)); // 2.5
        System.out.println(solution2(arr2)); // 5
    }
}
