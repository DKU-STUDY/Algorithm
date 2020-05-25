package codility_training.lessons.lesson08.Leader.Dominator;

import java.util.Stack;
import java.util.stream.Stream;

public class JunilHwang {
  public static int solution(int [] A) {
    Stack<Integer> stack = new Stack<>();
    int len = A.length;
    for (int a : A) {
      if (stack.isEmpty() || stack.peek() == a) stack.push(a);
      else stack.pop();
    }
    if (stack.size() == 0) return -1;
    int peek = stack.peek();
    for (int j = 0, max_cnt = 0; j < len; j++) {
      if (peek == A[j]) max_cnt++;
      if (max_cnt > len / 2) return j;
    }
    return -1;
  }

  public static void main(String[] args)
  {
    Stream.of(
      solution(new int[]{3, 4, 3, 2, 3, -1, 3, 3}),
      solution(new int[]{2, 1, 1, 3, 4}),
      solution(new int[]{1, 2, 1}),
      solution(new int[]{3, 2, 1}),
      solution(new int[]{3, 2, 1, 4}),
      solution(new int[]{2147483647})
    ).forEach(System.out::println);
  }
}
