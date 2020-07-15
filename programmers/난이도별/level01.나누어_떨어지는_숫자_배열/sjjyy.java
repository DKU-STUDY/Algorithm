package 난이도별.level01.나누어_떨어지는_숫자_배열;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class sjjyy
{
    public static int[] solution(int[] arr, int divisor) {
        List<Integer> List = new ArrayList<>();

        for (int value : arr) {
            if (value % divisor == 0)
                List.add(value);
        }

        if (List.isEmpty())
            List.add(-1);

        int[] ans = new int[List.size()];

        for (int i = 0 ; i < List.size() ; i++)
            ans[i]= List.get(i);

        Arrays.sort(ans);

        return ans;
    }

    public static int[] solution2(int[] arr, int divisor) {
        int [] answer = Arrays.stream(arr)
                .boxed()
                .filter(v -> v % divisor == 0)
                .sorted((a, b) -> a - b)
                .mapToInt(Integer::valueOf)
                .toArray();

        return  answer.length == 0 ? new int[]{-1} : answer;
    }

    public static void main(String [] args)
    {
        int[] arr = {5, 9, 7, 10};
        int divisor = 5;
        System.out.println(Arrays.toString(solution(arr, divisor))); // [5, 10]
        System.out.println(Arrays.toString(solution2(arr, divisor))); // [5, 10]
    }
}
