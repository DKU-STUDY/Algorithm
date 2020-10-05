import java.util.LinkedList;
import java.util.Queue;

public class sjjyy {
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0, max = 0;
        Queue<Integer> queue = new LinkedList<>();

        for (int i : truck_weights)
        {
            while (true)
            {
                if (queue.isEmpty()) { // 큐가 비었을 때 트럭의 무게 삽입
                    queue.offer(i);
                    max += i;
                    answer++;
                    break;
                } else if (queue.size() == bridge_length) // 트럭이 다리를 다 건너면 큐에서 꺼내 최대 무게에서 뺌
                    max -= queue.poll();
                else { // 큐가 비어있지 않을 때
                    if (max + i > weight) { // 무게가 초과되면 0 삽입
                        queue.offer(0);
                        answer++;
                    } else { // 무게가 초과되지 않으면 트럭의 무게 삽입
                        queue.offer(i);
                        max += i;
                        answer++;
                        break;
                    }

                }
            }
        }

        return answer + bridge_length;
    }

    public static void main(String[] args) {
        int[] w1 = {7, 4, 5, 6};
        int[] w2 = {10};
        int[] w3 = {10, 10, 10, 10, 10, 10, 10, 10, 10, 10};

        System.out.println(solution(2, 10, w1)); // 8
        System.out.println(solution(100, 100, w2)); // 101
        System.out.println(solution(100, 100, w3)); // 110
    }
}
