
import java.util.Arrays;

public class sjjyy
{
    public static String solution(int a, int b)
    {
        int days = 0;
        String [] Day = {"SUN","MON","TUE","WED","THU","FRI","SAT"};

        for(int i = 1 ; i < a ; i++)
        {
            if(i == 2)
                days += 29;
           // else if(i == 4 || i == 6 || i == 9 || i == 11)
            else if(Arrays.asList(4,6,9,11).contains(i))
                days += 30;
            else
                days += 31;
        }

        days += 4 + b;

        return Day[days % 7];


    }

    public static void main(String[] args)
    {
        int a = 5;
        int b = 24;
        System.out.println(solution(a,b)); // TUE
    }
}
