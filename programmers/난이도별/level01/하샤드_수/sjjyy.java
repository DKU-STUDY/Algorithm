package 난이도별.level01.하샤드_수;

import java.util.Arrays;

public class sjjyy
{
    public static boolean solution(int x)
    {
        String str = Integer.toString(x);
        String [] arr = str.split("");

        /*
        int sum = 0;
        for(String i : arr)
            sum += Integer.parseInt(i);
        */

        int sum = Arrays.stream(arr).map(Integer::parseInt).reduce(0, Integer::sum);

        return x % sum == 0;
    }

    public static void main(String[] args)
    {
        int x = 10;
        int z = 11;
        System.out.println(solution(x));
        System.out.println(solution(z));
    }
}
