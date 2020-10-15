import java.util.Arrays;
import java.util.HashMap;

import static java.util.stream.Collectors.*;

public class sjjyy {
    /*
        * 의상의 종류와 이름이 담긴 2차원 배열이 주어질 때 서로 다른 옷 조합의 수를 리턴
        String[][] clothes = {{의상의 이름, 의상의 종류} ... }
        * 원소 개수는 1개 이상 30개 이하이며 모두 1 이상 20 이하 길이의 문자열로 이루어져 있음
        * 하루에 최소 한 개 이상의 옷을 입어야 함
    */
    public static int solution(String[][] clothes) {
        int answer = 1; // multiple
        HashMap<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < clothes.length; i++)
            hashMap.put(clothes[i][1], hashMap.getOrDefault(clothes[i][1], 0) + 1);
        // 같은 종류의 의상이라면 + 1

        for (int i : hashMap.values())
            answer *= (i + 1);
        // 총 경우의 수 *= (의상 개수 + 입지 않을 경우)

        return answer - 1;
        // 전부 입지 않는 경우 제외
    }

    public static int solution2(String[][] clothes) {
        return Arrays.stream(clothes)
                .collect(groupingBy(p -> p[1], mapping(p -> p[0], counting())))
                .values()
                .stream()
                .collect(reducing(1L, (x, y) -> x * (y + 1))).intValue() - 1;
    } // 다른 사람 풀이

    public static void main(String[] args) {
        String[][] clothes1 = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        String[][] clothes2 = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
        System.out.println(solution(clothes1)); // 5
        System.out.println(solution(clothes2)); // 3
    }
}
