public class sjjyy {

    /*
        https://programmers.co.kr/learn/courses/30/lessons/42577
        어떤 번호가 다른 번호의 접두어인지 확인
        @param phone_book 전화번호를 담은 배열
        @return 접두어인 경우 false, 그렇지 않으면 true

    */

    public static boolean solution(String[] phone_book) {
        boolean answer = true;
        int len = phone_book.length;

        for (int i = 0 ; i < len ; i++) {
            for (int j = 0 ; j < len ; j++) {
                if (i == j)
                    continue;

                if (phone_book[j].indexOf(phone_book[i]) == 0)
                    answer = false;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] phone_book1 = {"119", "97674223", "1195524421"};
        String[] phone_book2 = {"123", "456", "789"};
        String[] phone_book3 = {"12", "123", "1235", "567", "88"};

        System.out.println(solution(phone_book1)); // false
        System.out.println(solution(phone_book2)); // true
        System.out.println(solution(phone_book3)); // false
    }
}
