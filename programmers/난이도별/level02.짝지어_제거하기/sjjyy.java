import java.util.Stack;

public class sjjyy {
    /*
        @param s : 알파벳 소문자로 이루어진 문자열
        문자열에서 같은 알파벳이 2개 붙어있는 짝을 찾아 제거한 뒤, 앞뒤로 문자열을 이어 붙임
        해당 과정을 반복해서 문자열을 모두 제거하면 종료
        @return 성공적으로 수행하면 1, 아닐 경우 0
    */
    public static int solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == c) // 스택의 맨 위의 항목과 같다면
                stack.pop(); // 제거
            else
                stack.push(c); // 스택이 비어있거나 다른 문자열이면 삽입
        }

        return stack.isEmpty() ? 1 : 0; // 스택이 비었으면 성공적으로 수행했다고 처리
    }

    public static void main(String[] args) {
        System.out.println(solution("baabaa")); // 1
        System.out.println(solution("cdcd")); // 0
    }
}
