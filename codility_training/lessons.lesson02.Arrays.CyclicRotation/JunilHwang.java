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
     System.out.println(Arrays.equals(solution(new int[]{3, 8,9,7,6},3), new int[]{9,7,6,3,8}));
     System.out.println(Arrays.equals(solution(new int[]{},0), new int[]{}));
     System.out.println(Arrays.equals(solution(new int[]{5, -1000},1), new int[]{-1000, 5}));
     System.out.println(Arrays.equals(solution(new int[]{3,8,9,7,6},5), new int[]{3,8,9,7,6}));
     System.out.println(Arrays.equals(solution(new int[]{3,8,9,7,6},0), new int[]{3,8,9,7,6}));
  }
}