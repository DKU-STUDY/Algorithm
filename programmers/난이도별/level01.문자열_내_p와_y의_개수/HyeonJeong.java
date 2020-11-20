package 난이도별.level01.문자열_내_p와_y의_개수;

public class HyeonJeong {
    public static boolean solution(String s) {
        return s.chars()
                .reduce(0, (count, c) -> {
                    if (c == 'P' || c == 'p') return count + 1;
                    if (c == 'Y' || c == 'y') return count - 1;
                    return count;
                }) == 0;
    }

    public static void main(String[] args) {
        System.out.println(solution("pPoooyY")); //true
        System.out.println(solution("Pyy")); //false
    }
}
