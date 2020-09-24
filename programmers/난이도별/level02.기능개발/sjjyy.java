import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class sjjyy {
    public static int[] solution(int[] progresses, int[] speeds) {
        int len = progresses.length;
        Queue<Integer> queue = new LinkedList<>();
        int index = 0, count = 0;

        while (index < len)
        {
            for (int i = 0; i < len; i++)
                progresses[i] += speeds[i]; // 하루 작업 진도

            if (progresses[index] >= 100) // 작업 배포가 가능할 때
            {
                while (index < len && progresses[index] >= 100) // 같이 배포가 가능한 개수
                {
                    count++;
                    index++;
                }

                queue.offer(count); // 배포된 개수 저장
                count = 0;
            }
        }

        int[] answer = new int[queue.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = queue.poll();

        return answer;

//        실패
//        Queue<Integer> queue = new LinkedList<>();
//        ArrayList<Integer> answerList = new ArrayList<>();
//
//        for (int i = 0 ; i < progresses.length ; i++)
//        {
//            int day = 0;
//            while (progresses[i] < 100) {
//                progresses[i] += speeds[i];
//                day++;
//            }
//
//            queue.add(day);
//        }
//
//            int rest;
//            for (int i = 0; i < progresses.length; i++) {
//                rest = 100 - progresses[i];
//                if(rest % speeds[i] == 0) queue.add(rest / speeds[i]);
//                else queue.add(rest / speeds[i] + 1);
//            }
//
//            while (!queue.isEmpty()) {
//            int j = queue.peek();
//            int count = 0;
//
//            while (queue.peek() <= j) {
//                count++;
//                queue.poll();
//                if (queue.isEmpty())
//                    break;
//            }
//
//            answerList.add(count);
//        }
//
//        int[] answer = new int[answerList.size()];
//        for (int i = 0 ; i < answerList.size() ; i++)
//            answer[i] = answerList.get(i);
//
//        return answer;
    }

    public static void main(String[] args) {
        int[] p1 = {93, 30, 55}, s1 = {1, 30, 5};
        int[] p2 = {95, 90, 99, 99, 80, 99}, s2 = {1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(solution(p1, s1))); // [2, 1]
        System.out.println(Arrays.toString(solution(p2, s2))); // [1, 3, 2]
    }
}
