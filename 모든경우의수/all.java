package 모든경우의수;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class all {

  public static void f (List<Integer> stack, List<Integer> list) {
    if (stack.size() == list.size()) {
      System.out.println(stack);
      return;
    }
    for (int v : list) {
      if (!stack.contains(v)) {
        List<Integer> temp = stack.stream().collect(Collectors.toList());
        temp.add(v);
        f(temp, list);
      }
    }
  }

  public static void solution (int[] arr) {
    List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList());
    List<Integer> stack = new ArrayList();
    f(stack, list);
  }

  public static void main(String[] args) {
    int[] arr = { 1, 2, 3 };
    solution(arr);
    /* answer
      [ 1, 2, 3 ]
      [ 1, 3, 2 ]
      [ 2, 1, 3 ]
      [ 2, 3, 1 ]
      [ 3, 1, 2 ]
      [ 3, 2, 1 ]
    */
  }
}
