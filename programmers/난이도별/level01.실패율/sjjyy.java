package 난이도별.level01.실패율;

import java.util.Arrays;

public class sjjyy
{
    public static int[] solution(int N, int[] stages) {
        int[] answer = {};
        return answer;
    }

    public static void main(String[] args)
    {
        int[] s1 = {2, 1, 2, 6, 2, 4, 3, 3};
        int[] s2 = {4, 4, 4, 4, 4};
        int[] s3 = {1, 2, 3, 4, 5, 6, 7};
        System.out.println(Arrays.toString(solution(5, s1))); // [3, 4, 2, 1, 5]
        System.out.println(Arrays.toString(solution(4, s2))); // [4, 1, 2, 3]
        System.out.println(Arrays.toString(solution(8, s3)));
    }
}
