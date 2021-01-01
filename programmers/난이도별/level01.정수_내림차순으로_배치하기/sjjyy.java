package 난이도별.level01.정수_내림차순으로_배치하기;

import java.util.Arrays;

import static java.util.stream.Collectors.collectingAndThen;
import static java.util.stream.Collectors.joining;

public class sjjyy
{
    public static long solution(long n)
    {
        char[] arr = Long.toString(n).toCharArray();

        Arrays.sort(arr);

        StringBuilder stringBuilder = new StringBuilder();

        for (char i : arr)
        {
            stringBuilder.append(i);
        }

        stringBuilder.reverse();

        return Long.parseLong(stringBuilder.toString());
    }

    public static long solution2(long n)
    {
        return Arrays.stream(Long.toString(n).split(""))
                .map(Integer::parseInt)
                .sorted((a, b) -> b - a)
                .map(String::valueOf)
                .collect(collectingAndThen(joining(""), Long::parseLong));
    }

    public static void main(String[] args)
    {
        System.out.println(solution(98023214)); // 98432210
        System.out.println(solution2(98023214)); // 98432210
    }
}
