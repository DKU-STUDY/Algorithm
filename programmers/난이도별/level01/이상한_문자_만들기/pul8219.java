package programmers.난이도별.level01.이상한_문자_만들기;
// 안녕
/*
 * 힌트 참고함
 * split()함수 사용은 생각해냈으나 공백을 기준으로 문자를 자를 생각만 했지 빈 문자열로 각 문자마다 자를 생각은 못했음
 * 공백을 만날시 cnt 변수를 0으로 초기화 함으로써 새로운 단어 시작을 알아차리는 방법 활용
 * */

class Solution{
    public String solution(String s){
        String answer = "";
        int cnt = 0;

        String[] word = s.split(""); // 문자마다 잘라짐

        for(String ss : word){
            cnt = (ss.contains(" ")) ? 0 : cnt + 1;
            // contains(): 대상 문자열에 특정 문자열이 포함되어 있는지 확인하는 함수. boolean을 반환한다.
            // 문자가 공백이면 cnt = 0으로 초기화, 공백이 아닐 경우 cnt++

            // cnt 짝수이면(단어의 홀수번째라는 뜻) 소문자로, cnt 홀수이면(단어의 짝수번째) 대문자로 변환하여 answer 변수에 붙여나감
            answer += (cnt % 2 == 0) ? ss.toLowerCase() : ss.toUpperCase();

        }

        return answer;
    }
}

class pul8219{
    public static void main(String[] args){
        Solution s = new Solution();
        String sen = "try hello world";
        System.out.println(s.solution(sen));
    }
}