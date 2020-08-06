package 난이도별.level01.이상한_문자_만들기;

public class sjjyy
{
    public static String solution(String s) {
        StringBuilder answer = new StringBuilder();
        String[] arr = s.split("");
        int index = 0;

        for (String i : arr) {
            index = i.equals(" ") ? 0 : ++index;
            answer.append(index % 2 == 0 ? i.toLowerCase() : i.toUpperCase());
        }

        return answer.toString();
    }

    public static void main(String[] args)
    {
        System.out.println(solution("try hello world")); // TrY HeLlO WoRlD
        System.out.println(solution("sooooo hard")); // SoOoOo HaRd
    }

}
