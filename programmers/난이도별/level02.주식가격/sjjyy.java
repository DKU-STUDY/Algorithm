import java.util.Arrays;

/*
    @param prices[] : 초 단위로 기록된 주식 가격이 담긴 배열
    각 가격은 1 이상 10,000 이하인 자연수, 배열의 길이는 2 이상 100,000 이하
    @ return 가격이 떨어지지 않은 기간 (초)
*/

public class sjjyy {
    public static int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int count = 0, len = answer.length;

        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                count++;
                if (prices[i] > prices[j]) // 다음 가격이 더 크면 가격이 오른 것이므로 break
                    break;
            }
            answer[i] = count; // 떨어지지 않은 초시간 저장
            count = 0;
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] prices = new int[]{1, 2, 3, 2, 3};
        System.out.println(Arrays.toString(solution(prices))); // [4, 3, 1, 1, 0]
    }
}
