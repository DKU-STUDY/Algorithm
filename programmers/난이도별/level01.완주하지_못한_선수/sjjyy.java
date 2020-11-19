package 난이도별.level01.완주하지_못한_선수;

import java.util.Arrays;
import java.util.HashMap;

public class sjjyy
{
    public static String solution(String[] participant, String[] completion)
    {
        Arrays.sort(participant);
        Arrays.sort(completion);

        int len = completion.length, i;

        for (i = 0 ; i < len ; i++)
        {
            if (!participant[i].equals(completion[i]))
                return participant[i];
        }

        return participant[i];
    }

    public static String solution2(String[] participant, String[] completion)
    {
        HashMap<String, Integer> map = new HashMap<>();

        for (String name :
                completion) {
            map.put(name, map.getOrDefault(name, 0) + 1);
            // getOrDefault() : 찾는 키가 존재하면 해당 키의 값을 반환하고 없으면 기본값을 반환
        }

        for (String name :
                participant) {
            map.put(name, map.getOrDefault(name, 0) - 1);

            if (map.get(name) < 0)
                return name;
        }

        return "";
    }

    public static void main(String[] args)
    {
        String[] p1 = {"leo", "kiki", "eden"};
        String[] c1 = {"kiki", "eden"};
        String[] p2 = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] c2 = {"marina", "josipa", "nikola", "filipa"};
        String[] p3 = {"mislav", "stanko", "mislav", "ana"};
        String[] c3 = {"stanko", "mislav", "ana"};

        System.out.println(solution(p1,c1)); // leo
        System.out.println(solution(p2,c2)); // vinko
        System.out.println(solution(p3,c3)); // mislav
        System.out.println(solution2(p1,c1)); // leo
        System.out.println(solution2(p2,c2)); // vinko
        System.out.println(solution2(p3,c3)); // mislav
    }
}
