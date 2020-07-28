package 난이도별.level01.다트_게임;

public class sjjyy
{
    public static int solution(String dartResult)
    {
        char[] darts = dartResult.toCharArray();
        int[] score = new int[3];
        int index = -1;

        for (int i = 0; i < darts.length; i++)
        {
            if (darts[i] >= '0' && darts[i] <= '9')
            {
                index++;
                if (darts[i] == '1' && darts[i + 1] == '0')  // 두자릿수 숫자(10)일 때
                {
                    score[index] = 10;
                    i++;
                }
                else
                    score[index] = darts[i] - '0';
            }
            else if (darts[i] == 'D')
                score[index] = (int) Math.pow(score[index], 2);
            else if (darts[i] == 'T')
                score[index] = (int) Math.pow(score[index], 3);
            else if (darts[i] == '*')
            {
                if (index > 0)
                    score[index - 1] *= 2;

                score[index] *= 2;
            }
            else if (darts[i] == '#')
                score[index] *= -1;
        }

        return score[0] + score[1] + score[2];
    }


    public static void main(String[] args)
    {
        String dartResult = "1S2D*3T";
        System.out.println(solution(dartResult)); // 37

        System.out.println(solution("1D2S#10S")); // 9
        System.out.println(solution("1D2S0T")); // 3
        System.out.println(solution("1S*2T*3S")); // 23
        System.out.println(solution("1D#2S*3S")); // 5
        System.out.println(solution("1T2D3D#")); // -4
        System.out.println(solution("1D2S3T*")); // 59
    }
}
