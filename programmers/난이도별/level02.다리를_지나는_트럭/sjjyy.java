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
                if (queue.isEmpty()) {
                    queue.offer(i);
                    max += i;
                    answer++;
                    break;
                } else if (queue.size() == bridge_length)
                    max -= queue.poll();
                else {
                    if (max + i > weight) {
                        queue.offer(0);
                        answer++;
                    } else {
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
