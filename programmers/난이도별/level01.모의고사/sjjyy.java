package 난이도별.level01.모의고사;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class sjjyy {
    public static int[] solution(int[] answers) {
        int[] ans1 = {1, 2, 3, 4, 5};
        int[] ans2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5,};
        int a = 0, b = 0, c = 0;

        int len = answers.length;

        for (int i = 0; i < len; i++) {
            if (answers[i] == ans1[i % 5])
                a++;
            if (answers[i] == ans2[i % 8])
                b++;
            if (answers[i] == ans3[i % 10])
                c++;
        }

        int max = Math.max(a, Math.max(b, c));

        List<Integer> list = new ArrayList<>();
        if (max == a)
            list.add(1);
        if (max == b)
            list.add(2);
        if (max == c)
            list.add(3);

        int[] answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }

    public static int[] solution2(int[] answers) {
        int[] ans1 = {1, 2, 3, 4, 5};
        int[] ans2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5,};
        int[] score = new int[3];

        int len = answers.length;

        for (int i = 0; i < len; i++) {
            if (answers[i] == ans1[i % 5])
                score[0]++;
            if (answers[i] == ans2[i % 8])
                score[1]++;
            if (answers[i] == ans3[i % 10])
                score[2]++;
        }

        int max = Math.max(score[0], Math.max(score[1], score[2]));

        List<Integer> list = new ArrayList<>();
        if (max == score[0])
            list.add(1);
        if (max == score[1])
            list.add(2);
        if (max == score[2])
            list.add(3);

        int[] answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }

    public static int[] solution3(int[] answers) {
        int[][] ans = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int[] score = new int[3];

        int len = answers.length;

        for (int i = 0; i < len; i++) {
            if (answers[i] == ans[0][i % 5])
                score[0]++;
            if (answers[i] == ans[1][i % 8])
                score[1]++;
            if (answers[i] == ans[2][i % 10])
                score[2]++;
        }

        int max = Math.max(score[0], Math.max(score[1], score[2]));

        return IntStream.rangeClosed(1, 3)
                .filter(i -> score[i - 1] == max)
                .toArray();

        /*
        List<Integer> list = new ArrayList<>();
        if (max == score[0])
            list.add(1);
        if (max == score[1])
            list.add(2);
        if (max == score[2])
            list.add(3);

        return list.stream().mapToInt(i -> i).toArray();
        */
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 4, 5}))); // [1]
        System.out.println(Arrays.toString(solution(new int[]{1, 3, 2, 4, 2}))); // [1, 2, 3]

        System.out.println(Arrays.toString(solution2(new int[]{1, 2, 3, 4, 5})));
        System.out.println(Arrays.toString(solution2(new int[]{1, 3, 2, 4, 2})));

        System.out.println(Arrays.toString(solution3(new int[]{1, 2, 3, 4, 5})));
        System.out.println(Arrays.toString(solution3(new int[]{1, 3, 2, 4, 2})));
    }
}
