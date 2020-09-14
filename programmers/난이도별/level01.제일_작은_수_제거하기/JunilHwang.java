package programmers.난이도별.level01.제일_작은_수_제거하기;

import java.util.ArrayList;
import java.util.Arrays;

public class JunilHwang
{
    public static int[] solution(int[] arr) {
        if (arr.length < 2) return new int[]{-1};

        int min = Arrays.stream(arr).reduce(Integer.MAX_VALUE, Math::min);

        return Arrays.stream(arr)
                     .boxed()
                     .filter(v -> v != min)
                     .mapToInt(v -> v).toArray();
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int[] arr2 = {10};
        System.out.println(Arrays.toString(solution(arr))); // [2, 3, 4]
        System.out.println(Arrays.toString(solution(arr2))); // [-1]
    }
}
