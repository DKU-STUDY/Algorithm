public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/42883
        @param number : 1자리 이상, 1,000,000자리 이하의 숫자 문자열
        number에서 k개의 수를 제거했을 떄 얻을 수 있는 가장 큰 숫자 구하기
        @return 가장 큰 숫자 문자열
    */
    public static String solution(String number, int k) {
//        String answer = "";
        StringBuilder stringBuilder = new StringBuilder();

        int index = 0;
        char max;

        if (number.charAt(0) == '0') // 예외처리
            return "0";

        for (int i = 0 ; i < number.length() - k ; i++) { // 반복문 수행
            max = '0';
            for (int j = index ; j <= k + i ; j++) { // 현재 위치부터 뽑음
                if (max < number.charAt(j)) {
                    max = number.charAt(j); // 각 자리 숫자를 뽑을 때마다 최대값 선택
                    index = j + 1;
                }
            }
//            answer += max;
            stringBuilder.append(max);
        }
//        return answer;
         return stringBuilder.toString(); // 시간 초과 처리
    }

    public static void main(String [] args) {
        System.out.println(solution("1924", 2)); // 94
        System.out.println(solution("1231234", 3)); // 3234
        System.out.println(solution("4177252841", 4)); // 775841
    }
}
