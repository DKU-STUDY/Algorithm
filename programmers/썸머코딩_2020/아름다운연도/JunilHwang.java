package programmers.썸머코딩_2020.아름다운연도;

import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class JunilHwang {

    public static int solution(int p) {
        for(int answer = p + 1; answer < 100000; answer++){
            String years = Integer.toString(answer);
            Set<Integer> set = new HashSet<Integer>(years.chars().boxed().collect(Collectors.toList()));
            if (set.size() == years.length()) return answer;
        }
        return -1;
    }

    public static void main(String[] args){
        System.out.println(solution(1989) == 2013);
        System.out.println(solution(2015) == 2016);
    }
}
