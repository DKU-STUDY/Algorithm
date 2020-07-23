package 난이도별.level01.비밀지도;

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class sjjyy
{
    public static String[] solution(int n, int[] arr1, int[] arr2)
    {
        String [] arr = new String[n];

        for(int i = 0 ; i < n ; i++)
        {
            arr[i] = Integer.toBinaryString(arr1[i] | arr2[i])
                    .replace("1", "#")
                    .replace("0", " ");
        }
        return arr;
    }

    public static String solution2(int n, int[] arr1, int[] arr2)
    {
        return IntStream.range(0, n).mapToObj(i -> Integer.toBinaryString(arr1[i] | arr2[i])
                .replace("1", "#")
        .replace("0", " ")).collect(Collectors.joining(", "));
    }

    public static void main(String[] args)
    {
        int[] arr1 = new int[]{9, 20, 28, 18, 11};
        int[] arr2 = new int[]{30, 1, 21, 17, 28};

        System.out.println(Arrays.toString(solution(5, arr1, arr2)));
        // [#####, # # #, ### #, #  ##, #####]
        System.out.println(solution2(5, arr1, arr2));
        // [#####, # # #, ### #, #  ##, #####]

    }

}
