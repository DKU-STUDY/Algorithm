import java.util.Arrays;

public class JunilHwang {
  public static int solution(int n) {
    String b = Integer.toBinaryString(n);
    int i = 0, max = 0, len = b.length();
    while (i < len) {
      int idx = b.indexOf("1", i + 1);
      if (idx == -1) break;
      max = Math.max(max, idx - i - 1);
      i = idx;
    }
    return max;
  }
}