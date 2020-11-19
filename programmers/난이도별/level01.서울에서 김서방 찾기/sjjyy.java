package 난이도별.level01.서울에서_김서방_찾기;

public class sjjyy
{
    public static String solution(String[] seoul)
    {
        int index = 0;
        for (int i = 0 ; i < seoul.length ; i++)
        {
            if (seoul[i].equals("Kim"))
                index = i;
        }

        return "김서방은 " + index + "에 있다";
    }

    public static void main(String [] args)
    {
        String [] seoul = {"Jane", "Kim"};
        System.out.println(solution(seoul));
    }

}
