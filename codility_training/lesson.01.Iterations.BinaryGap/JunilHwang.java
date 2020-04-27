import java.util.Arrays;

public class JunilHwang {
    public int solution(int n) {
      if (n == 1) return 0; // 1 = 0

      int tempGap[] = { 0, 0 };

      /*return Arrays
        .asList(Integer.toBinaryString(n).toCharArray()) // binary로 변환 후 char[] 배열 생성 및 List로 변환
        .stream()
        .reduce(tempGap, (start, v) -> { // reduce 내부에서는 외부 변수를 사용할 수 없음
          if(v.equals('0')) {
              start[0] += 1; // count 0
          }
          else if(v.equals('1')) // end
          {
              start[1] = Math.max(start[0], start[1]);
              start[0] = 0;
          }
          return start;
        })*/
      return 0;
    }
}