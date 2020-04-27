package lessons.lesson02.Arrays.CyclicRotation;

import java.util.Arrays;
import java.util.stream.Collectors;

public class JunilHwang {
  public static int[] solution(int[] A, int K) {
    K = K % A.length;
    int len = A.length;
    int[] newA = new int[A.length];
    for (int i = 0, j = K - 1; i < K; i++, j++) newA[i] = A[j];
    for (int i = K, j = 0; i < len; i++, j++) newA[i] = A[j];
    System.out.println( Arrays.stream(newA).boxed().collect(Collectors.toList()));
    return newA;
  }

  public static void main(String[] args) {
    int[] A = {3,8,9,7,6};
    int[] Sol = {9,7,6,3,8};
    System.out.println(Arrays.equals(solution(A,3), Sol));
  }
}