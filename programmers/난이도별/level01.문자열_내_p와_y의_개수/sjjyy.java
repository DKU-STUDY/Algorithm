package 난이도별.level01.문자열_내_p와_y의_개수;

public class sjjyy {
    public static boolean solution(String s)
    {

        // int p = s.toLowerCase().split("p").length;
        // int y = s.toLowerCase().split("y").length;

        return s.toLowerCase().chars().filter(i -> 'p' == i).count() == s.toLowerCase().chars().filter(i -> 'y' == i).count();
    }

    public static boolean solution2(String s)
    {
        int p = 0, y = 0;
        s = s.toLowerCase();

        for (int i = 0 ; i < s.length(); i++)
        {
            if (s.charAt(i) == 'p')
                p++;
            if(s.charAt(i) == 'y')
                y++;
        }

        return p == y;
    }

    public static void main(String[] args)
    {
        String s = "Pyy";
        System.out.println(solution(s)); // false
        System.out.println(solution("pPoooyY")); // true
        System.out.println(solution("oooo")); // true

        System.out.println(solution2("PypY")); // true
        System.out.println(solution2("oooo")); // true
        System.out.println(solution2("pPoooyY")); // true
    }
}
