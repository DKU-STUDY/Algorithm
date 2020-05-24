import java.util.HashSet;
import java.util.Set;
import java.util.Iterator;

class Solution {
    public int solution(int p) {
        int answer = 0;

        Set<Integer> set = new HashSet<>();

        answer = p + 1;
        for(;; answer++){
            set.clear();
            String a_str = Integer.toString(answer);
            int[] a_arr = new int[a_str.length()];
            for(int i = 0; i < a_str.length(); i++){
                a_arr[i] = a_str.charAt(i) - '0';
                set.add(a_arr[i]);
            }
            //Iterator<Integer> it = set.iterator();

            if(set.size() != 4)
                continue;
            else if(set.size() == 4){
                // while(it.hasNext())
                //     System.out.println("set: " + it.next());
                break;
            }
        }
        //System.out.println(answer);

        return answer;
    }
}

public class pul8219 {
    public static void main(String[] args){
        int p = 1989;
        Solution s = new Solution();
        System.out.println(s.solution(p));

    }
}
