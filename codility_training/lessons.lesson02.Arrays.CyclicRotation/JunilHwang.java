package lessons.lesson02.Arrays.CyclicRotation;

import java.util.Arrays;

public class JunilHwang {
  public static int[] solution(int[] A, int K) {
    int len = A.length;
    int[] newA = new int[A.length];
    for (int i = 0; i < len; i++) {
      newA[i] = A[(len - K + i) % len];
    }
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

    int[] A4 = {3,8,9,7,6};
    int[] Sol4 = {3,8,9,7,6};
    System.out.println(Arrays.equals(solution(A4,5), Sol4));

    int[] A5 = {3,8,9,7,6};
    int[] Sol5 = {3,8,9,7,6};
    System.out.println(Arrays.equals(solution(A5,0), Sol5));
  }
}