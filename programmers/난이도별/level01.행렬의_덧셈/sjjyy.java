package 난이도별.level01.행렬의_덧셈;

import java.util.Arrays;

public class sjjyy
{
    public static int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];

        for (int i = 0 ; i < arr1.length ; i++)
        {
            for (int j = 0 ; j < arr1[0].length ; j++)
                answer[i][j] = arr1[i][j] + arr2[i][j];
        }
        return answer;
    }

    public static void main(String [] args)
    {
        int[][] arr1 = { { 1, 2 }, { 2, 3 } };
        int[][] arr2 = { { 3, 4 }, { 5, 6 } };
        System.out.println(Arrays.deepToString(solution(arr1, arr2))); // [[4, 6], [7, 9]]
    }
}
