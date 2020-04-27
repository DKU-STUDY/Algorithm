package lessons.lesson02.Arrays.CyclicRotation;

import java.util.Arrays;
import java.util.stream.Collectors;

public class JunilHwang {
  public static int[] solution(int[] A, int K) {
    int len = A.length;
    if (len == 0 || len == K || K == 0) return A;
    int[] newA = new int[A.length];
    K = K % A.length;
    for (int i = 0; i < len; i++) {
      newA[i] = A[(len - K + i) % len];
    }
    System.out.println(Arrays.stream(newA).boxed().collect(Collectors.toList()));
    return newA;
  }

  public static void main(String[] args) {
    int[] A = {3,8,9,7,6};
    int[] Sol = {9,7,6,3,8};
    System.out.println(Arrays.equals(solution(A,3), Sol));

    int[] A2 = {};
    int[] Sol2 = {};
    System.out.println(Arrays.equals(solution(A2,0), Sol2));

    int[] A3 = {5, -1000};
    int[] Sol3 = {-1000, 5};
    System.out.println(Arrays.equals(solution(A3,1), Sol3));
  }
}