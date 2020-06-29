package lessons.lesson13.FibonacciNumbers.FibFrog;

import java.util.*;

public class sjjyy
{
    public static int solution(int[] A) // 83%
    {
        int aLen = A.length;
        List<Integer> jmp = new ArrayList<>();
        jmp.add(1);
        jmp.add(1);

        int next = 0;

        while (next < aLen -1)
        {
            next = jmp.get(jmp.size()-1) + jmp.get(jmp.size()-2);
            jmp.add(next);
        } // fibonacci

        int[] min = new int[aLen + 2];

        Arrays.fill(min, Integer.MAX_VALUE);
        min[0] = 0;
        int mLen = min.length;

        for(int i = 0 ; i < mLen ; i++)
        {
            if(!(i == 0 || i == mLen - 1 || A[i-1] == 1)) continue;

                for(int j : jmp)
                {
                    if(j > i)
                        break;
                    min[i] = (int) Math.min(min[i], (long) min[i-j]+1);
                }

        }

        if(min[mLen-1] == Integer.MAX_VALUE)
            return -1;

        return min[mLen-1];
    }

    public static int solution2(int[] A) // modify
    {
        int aLen = A.length;
        if(aLen == 0) return 1;

        List<Integer> jmp = new ArrayList<>();
        jmp.add(1);
        jmp.add(1);

        int next = 1;
        while (jmp.get(next) <= aLen)
        {
            jmp.add(jmp.get(next) + jmp.get(next-1));
            next++;
        }

        // github mkki님 참고
        Collections.reverse(jmp);

        Queue<Pair> q = new LinkedList<>();
        boolean[] check = new boolean[aLen+1];
        q.add(new Pair(-1, 0));

        while(!q.isEmpty())
        {
            Pair current = q.poll();

            for(int f : jmp)
            {
                int n = current.x + f;

                if(n == aLen)
                    return current.y + 1;
                if(n < aLen && n >= 0 && A[n] == 1 && !check[n] )
                {
                        check[n] = true;
                        q.add(new Pair(n, current.y + 1));
                }
            }
        }

        return -1;
    }


    public static void main(String[] args)
    {
        int[] A = {0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0};
        System.out.println(solution(A)); // 3
        System.out.println(solution2(A)); // 3
    }
}


class Pair
{
    int x, y;

    public Pair(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}

