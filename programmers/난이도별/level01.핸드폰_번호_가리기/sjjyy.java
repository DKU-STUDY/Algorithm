package 난이도별.level01.핸드폰_번호_가리기;

public class sjjyy
{
    public static String solution(String phone_number)
    {
        StringBuilder answer = new StringBuilder();

        for (int i = 0 ; i < phone_number.length(); i++)
        {
            if (i < phone_number.length() - 4)
                answer.append("*");
            else
                answer.append(phone_number.charAt(i));
        }

        return answer.toString();
    }

    public static void main(String [] args)
    {
        System.out.println(solution("01012345678")); // *******5678
        System.out.println(solution("026081128")); // *****1128
    }
}
