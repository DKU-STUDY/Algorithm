import java.util.Arrays;

public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/12939
        @param s : 공백으로 구분된 숫자 문자열, 둘 이상의 정수가 공백으로 구분되어 있음
        숫자 중 최소값, 최대값을 찾기
        @return "최소값 최대값" 형태로 반환
    */
    public static String solution(String s) {
        String [] str = s.split(" "); // 숫자 문자열 배열로 저장
        int len = str.length;
        int [] numbers = new int[len];

        for (int i = 0 ; i < len ; i++)
            numbers[i] = Integer.parseInt(str[i]); // Integer 타입으로 변환

        Arrays.sort(numbers); // 오름차순 정렬

        return numbers[0] + " " + numbers[len - 1]; // 최소값 최대값 형태로 반환
    }

    public static void main(String [] args) {
        System.out.println(solution("1 2 3 4")); // 1 4
        System.out.println(solution("-1 -2 -3 -4")); // -4 -1
        System.out.println(solution("-1 -1")); // -1 -1
    }
}
