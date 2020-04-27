package lessons.lesson02.Arrays.CyclicRotation;

import java.util.Arrays;
import java.util.stream.Collectors;

public class sjjyy {

    public static int[] solution(int[] A, int K) {
        int len = A.length;
        int[] B = new int[len];

        for(int i = 0 ; i < len ; i++)
        B[(i+K) % len] = A[i];

        return B;
    }

    public static void main(String[] args) {
        int[] A = {3,8,9,7,6};
        int[] Sol = {9,7,6,3,8};
        System.out.println(Arrays.equals(solution(A,3), Sol));
    }
}
