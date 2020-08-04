package level01.서울에서_김서방_찾기;

public class HyeonJeong {
    class Solution {
        public String solution(String[] seoul) {
            String answer = "";
            for(int i = 0; i < seoul.length; i++)
                if (seoul [i] == "Kim")
                    answer = "김서방은 i에 있다";

            return answer;
        }
        public void main(String[] args) {
            String [] array = {"Jane","Kim"};
            System.out.println(solution(array) == "김서방은 1에 있다");
        }
    }
}
