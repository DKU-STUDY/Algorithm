package 난이도별.level02.가장_큰_수

import java.util.Arrays;
import java.util.Comparator;

public class sjjyy {
    public static String solution(int[] numbers) {
        String answer = "";
        int len = numbers.length;

        // int [] -> String []
        String [] arr = new String[len];
        for (int i = 0 ; i < len ; i++)
            arr[i] = String.valueOf(numbers[i]);

        // 내림차순 정렬
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s, String t1) {
                return (t1+s).compareTo(s+t1);
            }
        });
        
        // 람다식
        // Arrays.sort(arr, (s, t1) -> (t1+s).compareTo(s+t1));

        // 예외처리
        if (arr[0].equals("0"))
            return "0";

        // 이어붙이기
        for (String s : arr)
            answer += s;

        return answer;
    }

    public static void main(String [] args) {
        int[] num1 = {6, 10, 2};
        int[] num2 = {3, 30, 34, 5, 9};

        System.out.println(solution(num1)); // 6210
        System.out.println(solution(num2)); // 9534330
    }
}
