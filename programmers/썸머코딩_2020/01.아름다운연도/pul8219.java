import java.util.HashSet;
import java.util.Set;
import java.util.Iterator;
import java.util.stream.Collectors; //solution2()에서 사용

class Solution {
    public int solution(int p) {
        int answer = 0;

        Set<Integer> set = new HashSet<>();

        answer = p + 1;
        for (; ; answer++) {
            set.clear();
            String a_str = Integer.toString(answer);
            int[] a_arr = new int[a_str.length()];
            for (int i = 0; i < a_str.length(); i++) {
                a_arr[i] = a_str.charAt(i) - '0';
                set.add(a_arr[i]);
            }
            //Iterator<Integer> it = set.iterator();

            if (set.size() != 4)
                continue;
            else if (set.size() == 4) {
                // while(it.hasNext())
                //     System.out.println("set: " + it.next());
                break;
            }
        }
        //System.out.println(answer);

        return answer;
    }

    // hwangjunil 풀이
    // 관련 공부하고 이해할 것
    public static int solution2(int p) {
        for (int answer = p + 1; answer < 100000; answer++) {
            String years = Integer.toString(answer);
            Set<Integer> set = new HashSet<Integer>(years.chars().boxed().collect(Collectors.toList()));
            if (set.size() == years.length()) return answer;
        }
        return -1;
    }
}

public class pul8219 {
    public static void main(String[] args){
        int p = 1989;
        Solution s = new Solution();
        System.out.println(s.solution(p));

    }
}
