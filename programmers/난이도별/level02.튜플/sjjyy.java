import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/64065
        @param 원소의 개수가 n개인, 중복되는 원소가 없는 튜플을 표현하는 집합이 담긴 문자열 s
        @return s가 표현하는 튜플

    */
    public static int[] solution(String s) {
        s = s.substring(2, s.length()-2).replace("},{", "/"); // 앞뒤 괄호 제거, 튜플별 분리
        String [] str = s.split("/"); // 튜플끼리 배열에 저장

        Arrays.sort(str, new Comparator<String>() {
            @Override
            public int compare(String s, String t1) {
                return s.length() - t1.length();
            }
        }); // 배열 길이 크기대로 정렬

        ArrayList<Integer> arrayList = new ArrayList<>();

        for (String s1 : str) {
            String [] arr = s1.split(","); // 튜플 값 각각 저장

            for (String value : arr) {
                int number = Integer.parseInt(value); // String -> int

                if (!arrayList.contains(number)) // 중복된 값 제외
                    arrayList.add(number);
            }
        }

        int [] answer = new int[arrayList.size()];
        for (int i = 0 ; i < arrayList.size() ; i++)
            answer[i] = arrayList.get(i);

        return answer;
    }

    public static void main(String [] args) {
        System.out.println(Arrays.toString(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))); // [2, 1, 3, 4]
        System.out.println(Arrays.toString(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))); // [2, 1, 3, 4]
        System.out.println(Arrays.toString(solution("{{20,111},{111}}"))); // [111, 20]
        System.out.println(Arrays.toString(solution("{{123}}"))); // [123]
        System.out.println(Arrays.toString(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))); // [3, 2, 4, 1]
    }
}
