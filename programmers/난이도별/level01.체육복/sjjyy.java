package 난이도별.level01.체육복;

public class sjjyy {
    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;

        for (int i = 0; i < lost.length; i++)
        {
            for (int j = 0; j < reserve.length; j++)
            {
                if (lost[i] == reserve[j])
                {
                    answer++;
                    lost[i] = -1;
                    reserve[j] = -1;
                    break;
                }
            }
        } // 여벌을 가진 학생이 도난당했으면 자신만 입을 수 있음

        for (int i = 0; i < lost.length; i++)
        {
            for (int j = 0; j < reserve.length; j++)
            {
                if (lost[i] == reserve[j] + 1 || lost[i] == reserve[j] - 1)
                {
                    answer++;
                    reserve[j] = -1;
                    break;
                }
            }
        } // 여벌의 체욱복을 가진 학생이 잃어버린 학생의 앞/뒷번호일 때 빌려줌

        return answer;
    }

    public static void main(String[] args)
    {
        int[] lost1 = {2, 4};
        int[] reserve1 = {1, 3, 5};
        System.out.println(solution(5, lost1, reserve1)); // 5

        int[] lost2 = {2, 4};
        int[] reserve2 = {3};
        System.out.println(solution(5, lost2, reserve2)); // 4

        int[] lost3 = {3};
        int[] reserve3 = {1};
        System.out.println(solution(3, lost3, reserve3)); // 2

    }

}

