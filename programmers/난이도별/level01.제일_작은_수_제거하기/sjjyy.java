package 난이도별.level01.제일_작은_수_제거하기;

import java.util.ArrayList;
import java.util.Arrays;

public class sjjyy
{
    public static int[] solution(int[] arr)
    {
        int[] answer = new int[arr.length-1];

        if (arr.length < 2)
            return new int[]{-1};

        ArrayList<Integer> arr2 = new ArrayList<>();

        for (int i : arr) arr2.add(i);

        int min = arr[0];
        for (int i = 1; i < arr.length; i++)
            min = Math.min(arr[i], min);

        arr2.remove((Integer) min);

        for (int i = 0 ; i < arr2.size() ; i++)
            answer[i] = arr2.get(i);

        return answer;

    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int[] arr2 = {10};
        System.out.println(Arrays.toString(solution(arr))); // [2, 3, 4]
        System.out.println(Arrays.toString(solution(arr2))); // [-1]
    }
}
