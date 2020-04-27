package lessons.lesson01.Iterations.BinaryGap;

public class JunilHwang {
  public static int solution(int n) {
    String b = Integer.toBinaryString(n);
    int i = 0, max = 0, len = b.length(), idx; // idx는 일단 정의만
    while (i < len) { // 반복 횟수를 최대한 줄이기
      idx = b.indexOf("1", i + 1);
      if (idx == -1) break;
      max = Math.max(max, idx - i - 1);
      i = idx;
    }
    return max;
  }

  public static void main(String[] args) {
    System.out.println(solution(32) == 0);
    System.out.println(solution(1041) == 5);
    System.out.println(solution(9) == 2);
    System.out.println(solution(529) == 4);
    System.out.println(solution(20) == 1);
    System.out.println(solution(15) == 0);
  }
}
