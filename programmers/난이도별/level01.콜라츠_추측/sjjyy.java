package 난이도별.level01.콜라츠_추측;

public class sjjyy
{
    public static int solution(long num)
    {
        int answer = 0;

        while (num != 1)
        {
            if (num % 2 == 0)
                num /= 2;
            else
                num = num * 3 + 1;

            answer++;

            if (answer == 500)
            {
                answer = -1;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args)
    {
        System.out.println(solution(6)); // 8
        System.out.println(solution(16)); // 4
        System.out.println(solution(626331)); // -1
    }
}
