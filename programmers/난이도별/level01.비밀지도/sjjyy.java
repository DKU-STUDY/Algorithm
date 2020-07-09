package 난이도별.level01.비밀지도;

import java.util.Arrays;

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

    public static void main(String[] args)
    {
        int[] arr1 = new int[]{9, 20, 28, 18, 11};
        int[] arr2 = new int[]{30, 1, 21, 17, 28};

        System.out.println(Arrays.toString(solution(5, arr1, arr2)));
        // [#####, # # #, ### #, #  ##, #####]

    }

}
