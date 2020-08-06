package 난이도별.level01.소수찾기;

import java.util.Arrays;

public class sjjyy {
    public static int solution(int n) // 75/100
    {
        int ans = 0;

        for (int i = 2; i <= n; i++) {
            boolean isPrime = true;

            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                ans++;
        }

        return ans;
    }

    public static int solution2(int n) // 100/100
    {
        int ans = 0;
        int[] num = new int[n + 1];

        for (int i = 2; i <= n; i++) // 2~n까지 배열에 추가
            num[i] = i;

        for (int i = 2; i <= n; i++)
        {
            if(num[i] == 0)
                continue;

            for (int j = 2*i ; j <= n ; j+=i) // 값이 0이 아닌 수의 배수는 모두 0ㅇ로 처리
                num[j]= 0;
        }

//        for (int i = 2 ; i <= n ; i++) // 값이 0이 아닌 수 (= 소수)의 개수 측정
//        {
//            if (num[i] != 0)
//                ans++;
//        }
//
//        return ans;

        return (int) Arrays.stream(num).filter(v -> v > 0).count();
    }

    public static void main(String[] args) {
        System.out.println(solution(10));
        System.out.println(solution2(10)); // 4

        System.out.println(solution(5));
        System.out.println(solution2(5)); // 3

    }
}