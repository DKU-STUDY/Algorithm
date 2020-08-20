package 난이도별.level01.가운데_글자_가져오기;

public class sjjyy
{
    public static String solution(String s)
    {
        int len = s.length();

//        if (len % 2 == 0)
//            return s.substring(len/2 - 1 , len/2 + 1);
//        else
//            return s.substring(len/2, len/2 + 1);


//        return len % 2 == 0 ? s.substring(len/2 -1 , len/2 + 1) : s.substring(len/2, len/2 +1);

        return s.substring(len/2 - (len % 2 == 0 ? 1 : 0), len/2 + 1);
    }

    public static void  main(String[] args){
        System.out.println(solution("abcde")); // c
        System.out.println(solution("qwer")); // we
    }
}
