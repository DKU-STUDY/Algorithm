public class HyeonJeong {
    public static boolean solution(String s) {
        int count = 0;
        char[] array = s.toUpperCase().toCharArray();
        for (int i = 0; i < s.length(); i++) {
            if (array[i] == 'P')
                count += 1;
            else if (array[i] == 'Y')
                count -= 1;
        }
        return count == 0;
    }

    public static void main(String[] args) {
        System.out.println(solution("pPoooyY")); //true
        System.out.println(solution("Pyy")); //false
    }
}
