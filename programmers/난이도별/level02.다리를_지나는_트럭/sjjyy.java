import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;

public class sjjyy {
//     public static int solution(int bridge_length, int weight, int[] truck_weights) {
//        int answer = 0, max = 0;
//        Queue<Integer> queue = new LinkedList<>();
//
//        for (int i : truck_weights)
//        {
//            while (true)
//            {
//                if (queue.isEmpty()) { // 큐가 비었을 때 트럭의 무게 삽입
//                    queue.offer(i);
//                    max += i;
//                    answer++;
//                    break;
//                } else if (queue.size() == bridge_length) // 트럭이 다리를 다 건너면 큐에서 꺼내 최대 무게에서 뺌
//                    max -= queue.poll();
//                else { // 큐가 비어있지 않을 때
//                    if (max + i > weight) { // 무게가 초과되면 0 삽입
//                        queue.offer(0);
//                        answer++;
//                    } else { // 무게가 초과되지 않으면 트럭의 무게 삽입
//                        queue.offer(i);
//                        max += i;
//                        answer++;
//                        break;
//                    }
//
//                }
//            }
//        }
//
//        return answer + bridge_length;
//    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;

        Queue<Integer> truck = new LinkedList();
        Queue<Point> bridge = new LinkedList();
        for (int truck_weight : truck_weights)
            truck.add(truck_weight);

        int total = 0;
        while (!truck.isEmpty() || !bridge.isEmpty()) { // 모든 트럭이 다리를 다 건널 때까지
            time++;
            if (!bridge.isEmpty()) { // 다리에 트럭이 올라왔을 때
                Point p = bridge.peek();
                if (time - p.y >= bridge_length) {
                    total -= p.x;
                    bridge.poll();
                }
            }

            if (!truck.isEmpty()) { // 더 올릴 트럭이 남아있을 때
                if (total + truck.peek() <= weight) { // 총 무게를 넘지 않을 때만
                    int tmp = truck.poll();
                    total += tmp;

                    bridge.offer(new Point(tmp, time));
                }
            }
        }

        return time;
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
