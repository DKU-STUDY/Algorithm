import java.util.PriorityQueue;

public class sjjyy {

    /*
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
     */

    public static int solution(int[] scoville, int K) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        int answer = 0;

        for (int i : scoville)
            queue.add(i);

        while (queue.peek() <= K) {
            if (queue.size() <= 1) { // 예외처리
                answer = -1;
                break;
            }

            int first = queue.poll();
            int second = queue.poll();
            int mix = first + second * 2;
            answer++;
            queue.add(mix);
        }

        return answer;

    }

    public static void main(String[] args) {
        int[] scovile = {1, 2, 3, 9, 10, 12};
        System.out.println(solution(scovile, 7)); // 2
    }
}
