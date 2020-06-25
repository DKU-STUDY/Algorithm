package lessons.lesson15.CaterpillarMethod.AbsDistinct;

import java.util.HashSet;

public class sjjyy
{
    public static int solution(int[] A)
    {
        HashSet<Integer> set = new HashSet<>();

        for(int n : A)
        {
            int abs = Math.abs(n);
            set.add(abs);
        }

        return set.size();
    }

    public static void main(String[] args)
    {
        int[] A = {-5, -3, -1, 0, 3, 6};
        System.out.println(solution(A)); // 5
    }
}
