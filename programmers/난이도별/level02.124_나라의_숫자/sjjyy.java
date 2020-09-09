public class sjjyy {

    // 3진법 활용, 몫 + 나머지

    public static String solution(int n) {
        String answer = "";

        while (n > 0) {
            int num = n % 3;
            n /= 3;

            if (num == 0) {
                num = 4;
                n--;
            }

            answer = num + answer;
        }
        return answer;
    }

    public static void main(String[] args) {
        int a = 19;
        System.out.println(solution(a)); // 141

        System.out.println(solution(1)); // 1
        System.out.println(solution(2)); // 2
        System.out.println(solution(3)); // 4
        System.out.println(solution(4)); // 11
        System.out.println(solution(5)); // 12
        System.out.println(solution(6)); // 14
        System.out.println(solution(7)); // 21
        System.out.println(solution(8)); // 22
        System.out.println(solution(9)); // 24
        System.out.println(solution(10)); // 41
    }
}

