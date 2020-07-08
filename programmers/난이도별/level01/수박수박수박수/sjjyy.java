package 난이도별.level01.수박수박수박수;

public class sjjyy
{
    public static String solution(int n)
    {
        StringBuilder answer = new StringBuilder();

        for(int i = 1 ; i <= n ; i++)
        {
            if(i % 2 == 1)
                answer.append("수");
            else
                answer.append("박");
        }
        return answer.toString();
    }

    public static void main(String [] args)
    {
        int n = 3;
        System.out.println(solution(n));
    }
}
