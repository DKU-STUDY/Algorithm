package 난이도별.level02.구명보트;

import java.util.Arrays;

public class sjjyy {
    public static int solution(int[] people, int limit) {
        int answer = people.length;

        Arrays.sort(people);
        int i = 0, j = people.length - 1;

        while (i < j) {
            if (people[i] + people[j] <= limit) {
                answer--;
                i++;
            }
            j--;
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] p1 = {70, 50, 80, 50};
        int[] p2 = {70, 50, 80};
        int[] p3 = {70, 10, 80, 20};
        System.out.println(solution(p1, 100)); // 3
        System.out.println(solution(p2, 100)); // 3
        System.out.println(solution(p3, 100)); // 2

    }
}
